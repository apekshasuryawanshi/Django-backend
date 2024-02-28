from django.contrib import admin

# Register your models here.
from .models import books


class booksAdmin(admin.ModelAdmin):


    list_display  = ['book_name','subject']

admin.site.register(books,booksAdmin)