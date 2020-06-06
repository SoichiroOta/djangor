from django import forms

from djangor.entries.models import Entry


class EntryCreationForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('title', 'text')
