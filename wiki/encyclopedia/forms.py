from django import forms

class PageForm(forms.Form):
    title=forms.CharField(
        label="title", 
        max_length=50, 
        min_length=1, 
        error_messages = {'required': "Input a valid title"}
        )
    body=forms.CharField(
        label="body", 
        max_length=1000,
        min_length=10,
        error_messages = {'required': "Input a valid body"}
        )

class SubmitForm(forms.Form):
    value=forms.BooleanField(
        label="value"
    )