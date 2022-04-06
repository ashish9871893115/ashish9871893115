from tokenize import Name
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .models import Book
from django.db import models
from .forms import BookForm,BookDeleteForm
from . import forms,models

def register(request):
    if request.method == 'POST':
        user_creation_form = UserCreationForm(request.POST)
        if user_creation_form.is_valid():
            print('valid')
            user_creation_form.save()
            return redirect('/login/')
        else:
            user_creation_form = UserCreationForm()
            print('invalid')
            return render(request, 'signup.html', {'form': user_creation_form})
    else:
        user_creation_form = UserCreationForm()
        return render(request, 'signup.html', {'form': user_creation_form})

def log_in(request):
    if request.method=='POST':
        auth_form = AuthenticationForm(request=request, data=request.POST)
        if auth_form.is_valid():
            uname = auth_form.cleaned_data['username']
            upass = auth_form.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return redirect('/')
        else:
            return render(request,'login.html',{'auth_form':auth_form}) 
    else:
        auth_form = AuthenticationForm()
        return render(request,'login.html',{'auth_form':auth_form})
        

def log_out(request):
    logout(request)
    return redirect('homepage')


def homepage(request):
    context = {'book_list': Book.objects.all()}
    print(Book.objects.all())
    return render(request,'homepage.html', context)

def addbook_view(request):
    form=forms.BookForm()
    if request.method=='POST':
        form=forms.BookForm(request.POST)
        if form.is_valid():
            user=form.save()
    return render(request,'addbook.html',{'form':form})

def viewbook_view(request):
    books=models.Book.objects.all()
    return render(request,'viewbook.html',{'books':books})

def delete(request):
    form1=forms.BookDeleteForm()
    if request.method=='POST':
        form1=forms.BookForm(request.POST)
        records = Book.objects.all()
        records.delete()
    return render(request,'delete.html',{'form1':form1})

    