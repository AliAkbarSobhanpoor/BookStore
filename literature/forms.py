from django import forms

from literature.models import Book
from django.forms import formset_factory

class BookForm(forms.Form):
    name = forms.CharField(
        label="Book Name",
        widget=forms.TextInput(attrs={
            "class": "form-control mx-2",
            "placeholder": "Enter Book Name here",
            }
        ),
    )
    isbn_number = forms.CharField(
        label="Book ISBN",
        widget=forms.TextInput(attrs={
            "class": "form-control mx-2",
            "placeholder": "Enter Book ISBN here",
            }
        ),
    )

BookFormSet = formset_factory(BookForm, extra=1)