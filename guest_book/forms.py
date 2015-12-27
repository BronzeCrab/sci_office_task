from django.forms import ModelForm
from django import forms
from guest_book.models import Entry


class EntryForm(ModelForm):
    homepage = forms.URLField(required=False)
    email = forms.CharField(required=False)
    text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Entry
        fields = ['username', 'text', 'email', 'homepage']
