from django import forms
from .models import Article
from django.utils.timezone import now

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

class ArticleSearchForm(forms.Form):
    search_text =  forms.CharField(
                    required = False,
                    label='Search title',
                    widget=forms.TextInput(attrs={'placeholder': 'search here!', 'class': 'form-control col-12'})
                  )

    search_date_exact = forms.DateField(
                    required = False,
                    label='Search date (exact match)!',
                    #initial= now ,
                    widget=forms.DateInput(attrs={'placeholder': '2000-01-01', 'class': 'form-control col-12'})
                  )

    search_date_min = forms.DateField(
                    required = False,
                    label='from date',
                    widget=forms.DateInput(attrs={'placeholder': '2000-01-01', 'class': 'form-control col-6'})
                  )


    search_date_max = forms.DateField(
                    required = False,
                    label='to date',
                    widget=forms.DateInput(attrs={'placeholder': '2010-01-01', 'class': 'form-control col-6'})
                  )