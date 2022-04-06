from django import forms
from django.contrib.auth.models import User
from . import models

from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model=models.Book
        fields=['name','author','category']


class BookDeleteForm(forms.ModelForm):
    class Meta:
        model=models.Book
        fields=['name']