from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView

from main.form import AddBookForm, UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from main.models import *


# login user
class CustomLoginView(LoginView):
    template_name = 'main/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    extra_context = {'title': "Kirish"}

    def get_success_url(self):
        return reverse_lazy('home')


# create new user
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'form': form, 'title': "Ro'yhatdan o'tish"})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.customer)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            # messages.success(request, f'Your account has been updated!')
            return redirect('home')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.customer)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'title': 'Profile'
    }

    return render(request, 'main/profil.html', context)


@login_required(login_url='/login/')
def book(request):
    content = {'title': 'Bosh sahifa', 'count': Book.objects.all().filter(user=request.user).count()}

    return render(request, 'main/home.html', content)


@login_required(login_url='/login/')
def user_book(request):
    category = Category.objects.all()
    user_books = Book.objects.all().filter(user=request.user)

    content = {'user_books': user_books, 'category': category,
               'title': "Men o'qigan asarlar",
               'count': Book.objects.all().filter(user=request.user).count()}

    return render(request, 'main/products.html', content)


@login_required(login_url='/login/')
def user_book_detail(request, pk):
    selected_book = get_object_or_404(Book, pk=pk)

    content = {'selected_book': selected_book, 'title': selected_book.name,
               'count': Book.objects.all().filter(user=request.user).count(),
               }

    return render(request, 'main/user_book_detail.html', content)


@login_required(login_url='/login/')
def add_new_user_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST, request.FILES)

        if form.is_valid():
            form.instance.user = request.user
            form.save()
            redirect('user_books')
    else:
        form = AddBookForm()

    content = {'form': form, 'title': "Yangi asar qo'shish"}
    return render(request, 'main/add_new_book.html', content)


@login_required(login_url='/login/')
def contact(request):
    return render(request, 'main/contact.html', {'title': "Bog'lanish"})


class BookUpdate(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['name', 'author_name', 'book_heroes', 'description', 'comment', 'complete', 'image', 'file',
              'category']
    success_url = reverse_lazy('user_books')
    template_name = 'main/update_book.html'
    extra_context = {'title': "Yangilash"}


class DeleteViewBook(LoginRequiredMixin, DeleteView):
    model = Book
    context_object_name = 'book'
    extra_context = {'title': "O'chirish"}
    success_url = reverse_lazy('user_books')
    template_name = 'main/delete_book.html'

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)
