from django import forms
from django.contrib.auth.models import User
from .models import Review, Comment


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        exclude = ['author', 'pub_date', 'id']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ['date_added', 'author', 'review']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['text'].required = False
