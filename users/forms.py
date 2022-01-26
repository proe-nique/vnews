from django import forms
from .models import Profile


# Create your forms here.

class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ("avatar", "skill",)

        

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        
        #self.fields['category'].widget.attrs['class'] = 'form-control'
        #self.fields['tags'].widget.attrs['class'] = 'form-control'
        self.fields['avatar'].widget.attrs['class'] = 'form-control'
        self.fields['skill'].widget.attrs['class'] = 'form-control mb-2'
        #self.fields['description'].widget.attrs['class'] = 'form-control mb-2'
        #.fields['price'].widget.attrs['class'] = 'form-control'

    #def save(self, commit=True):
    #    Profile = super(ProfileForm, self).save(commit=False)
    #    user.email = self.cleaned_data['email']
    #    if commit:
    #        user.save()
    #    return user