from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.http.request import QueryDict
# Create your views here.

from django.shortcuts import redirect, render
from .forms import BookFormSet
from .models import Book

def create_book_normal(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        formset: BookFormSet = BookFormSet(request.GET or None)
    elif request.method == "POST":
        formset: BookFormSet = BookFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                name: str | None = form.cleaned_data.get("name", None)

                if name:
                    Book.objects.create(name=name)

            return redirect("create_book_normal")

    return render(
        request, 'literature/boob_formset.html', {
            "formset": formset, # all request to this page are get or post no other method approved
            "header": "create book from FormSet"
        }
    )

