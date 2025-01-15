from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ('text', 'photo')  # Include only existing fields in the Tweet model
