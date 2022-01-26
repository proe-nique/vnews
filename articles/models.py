from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify 
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Category(models.Model):
    
    name = models.CharField(default="", max_length=50)
    slug = models.SlugField(unique=True, null=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("stories:category_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class Tag(models.Model):
    
    name = models.CharField(default="", max_length=50)
    slug = models.SlugField(unique=True, null=True)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("stories:tag_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class Article(models.Model):

    user = models.ForeignKey(User, related_name='articles', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='articles', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='articles',)
    image = models.ImageField(default='article_images/default.png', upload_to='article_images')
    video = models.FileField(blank=True, null=True, upload_to='article_videos')
    slug = models.SlugField(unique=True, null=True)
    title = models.CharField(default="", max_length=50)
    content = models.TextField(default="")
    published = models.DateTimeField(auto_now=True, auto_now_add=False)
    date = models.DateField(auto_now=True, auto_now_add=False)
    featured = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("stories:article_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.user.username + '/' + self.title)
        else:
            self.slug = slugify(self.user.username + '/' + self.slug)
        return super().save(*args, **kwargs)