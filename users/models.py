from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify 
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    avatar = models.ImageField(default='avatars/default.png', upload_to='avatars')
    slug = models.SlugField(unique=True, null=True)
    skill = models.CharField(default="", max_length=50)

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("users:user_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.user.username)
        return super().save(*args, **kwargs)