from django import forms
from .models import Article


# Create your forms here.

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = ("category", "tags", "title", "image", "content",)

        

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        
        self.fields['category'].widget.attrs['class'] = 'form-control form-select'
        self.fields['tags'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['class'] = 'form-control mb-2'
        self.fields['content'].widget.attrs['class'] = 'form-control mb-2'
        #self.fields['video'].widget.attrs['class'] = 'form-control'

    