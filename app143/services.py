from .models import Book

def get_books1():
	return list(Book.objects.all())