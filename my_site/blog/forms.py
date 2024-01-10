from django import forms
from django.core.validators import MinLengthValidator
from django.forms import ModelForm, Textarea, CheckboxSelectMultiple, Select
from .models import Post
from django import forms
from .models import *
from .models import Resume,Image
from django.core.validators import MinLengthValidator


class ResumeForm(forms.ModelForm):

   class Meta:
      model = Resume
      fields = ['email','name','file']

class ImageForm(forms.ModelForm):

   class Meta:
      model = Image
      fields = ['title','image']

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


    class Meta:
        model = Post
        fields = ['title', 'anouncement', 'content', 'date_posted', 'tags']
        widgets = {
             'title': Textarea(attrs={'cols': 80, 'rows': 2, 'minlength':5}),
            'anouncement': Textarea(attrs={'cols': 80, 'rows': 2, 'minlength':5}),
            'content': Textarea(attrs={'cols': 80, 'rows': 2, 'minlength':20}),
            'text': Textarea(attrs={'cols': 80, 'rows': 2, 'minlength':100}),
            'tags': CheckboxSelectMultiple(),
    }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']