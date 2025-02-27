from  django import forms

from blog.models import Post


class AjouForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'contener']
