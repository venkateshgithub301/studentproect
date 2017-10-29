from django.contrib import admin

# Register your models here.
from .models import Book,MultipleBooks,MultiAuthoeBooks,Student,Bookname,Students

admin.site.register(Book)
admin.site.register(Students)
admin.site.register(Student)
admin.site.register(Bookname)
admin.site.register(MultipleBooks)
admin.site.register(MultiAuthoeBooks)
