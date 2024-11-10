from django import forms

class YouTubeForm(forms.Form):
    url = forms.URLField(label="YouTube URL", required=True)
