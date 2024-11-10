from django import forms

class YouTubeForm(forms.Form):
    url = forms.URLField(widget=forms.URLInput(attrs={'placeholder': 'Enter YouTube video URL here'}))

