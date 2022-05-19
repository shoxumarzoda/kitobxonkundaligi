from django.contrib.auth.views import LogoutView

from django.urls import path


from .views import *

urlpatterns = [

    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', register, name='register'),

    path('', book, name='home'),

    path('Mybooks/', user_book, name='user_books'),
    path('Mybooks/new-book/', add_new_user_book, name='add_new_user_book'),
    path('Mybooks/<int:pk>', user_book_detail, name='user_books_detail'),
    path('Book-update/<int:pk>/yangilash', BookUpdate.as_view(), name='book_update'),
    path('Mybooks/<int:pk>/ochirish/', DeleteViewBook.as_view(), name='delete_view_book'),

    path('boglanish/', contact, name='contact'),

    path('customer-update/', profile, name='customer_update'),



]
