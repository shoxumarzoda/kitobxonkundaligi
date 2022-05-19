from PIL import Image
from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Bo'limlar nomi", db_index=True)
    description = models.TextField(max_length=500, verbose_name="bo'lim  izohi")
    slug = models.SlugField(max_length=200, verbose_name="slug")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Bo'lim"
        verbose_name_plural = "Bo'limlar"


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    name = models.CharField(max_length=200, verbose_name="Asar nomi")
    author_name = models.CharField(max_length=200, verbose_name="Muallaif  nomi")
    description = models.TextField(max_length=500, verbose_name="Asar syujeti ")
    book_heroes = models.TextField(max_length=500, verbose_name="Asar qahramonlari ")
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="yaratilgan vaqti")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Yangilangan vaqti")
    comment = models.TextField(max_length=500, verbose_name="Asar hadida fikringiz")
    complete = models.BooleanField(default=False, null=True, verbose_name="O'qilgan/O'qilmagan")
    image = models.ImageField(upload_to='book/', verbose_name='rasm')
    file = models.FileField(upload_to='book_pdf', verbose_name="PDFfayl")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Bo'lim nomi")

    # slug = models.SlugField(verbose_name="URl", db_index=True, unique=True, max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kitob"
        verbose_name_plural = "Kitoblar"


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")

    profile_pic = models.ImageField(upload_to='user_pic/', default='user-img.png', null=True, blank=True,
                                    verbose_name="Foydalanuvchi rasmi")
    date_created = models.DateTimeField(auto_now_add=True, null=True, verbose_name="yaratilgan vaqti")
    interesting = models.CharField(max_length=200, null=True, verbose_name="qiziqishlari")

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.profile_pic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"
