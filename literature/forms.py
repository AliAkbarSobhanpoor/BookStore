from django import forms

from literature.models import Book
from django.forms import formset_factory

class BookForm(forms.Form):
    name = forms.CharField(
        label="Book Name",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Book Name here",
            }
        ),
    )

BookFormSet = formset_factory(BookForm, extra=1)