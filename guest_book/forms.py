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


CHOICES = [('username', 'username'),
           ('text', 'text'),
           ('email', 'email'),
           ('homepage', 'homepage')]


class RadioForm(forms.Form):
    sort = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, initial='username')
