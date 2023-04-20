from django import forms

class Topicforms(forms.Form):
    topic_name=forms.CharField(max_length=100)

class Webpageform(forms.Form):
    topic_name=forms.CharField(max_length=100)
    name=forms.CharField(max_length=100)
    url=forms.URLField()
    email=forms.EmailField()

class Accessrecordform(forms.Form):
    name=forms.CharField(max_length=100)
    author=forms.CharField(max_length=100)
    date=forms.DateField()