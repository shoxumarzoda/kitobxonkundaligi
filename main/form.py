from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *


class AddBookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "bo'lim tanlanmadi"

    class Meta:
        model = Book
        fields = ['name', 'author_name', 'book_heroes', 'description', 'comment', 'complete', 'image', 'file',
                  'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'box'}),
            'author_name': forms.TextInput(attrs={'class': 'box'}),
            'book_heroes': forms.TextInput(attrs={'class': 'box'}),
            'comment': forms.Textarea(attrs={'cols': 30, 'rows': 10, 'class': 'box'}),
            'description': forms.Textarea(attrs={'cols': 30, 'rows': 10, 'class': 'box'}),
        }


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['profile_pic', 'interesting']
