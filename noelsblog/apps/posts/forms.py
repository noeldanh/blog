from django import forms
from pagedown.widgets import PagedownWidget
from .models import Post


class PostForm(forms.ModelForm):
    body = forms.CharField(widget=PagedownWidget)
    publish = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Post
        fields = [
            "title",
            "body",
            "image",
            "draft",
            "publish"
        ]
        widgets = {
            'text': forms.TextInput(
                attrs={'id': 'post-text', 'required': True,
                       'placeholder': 'Say something...'}
            ),
        }
