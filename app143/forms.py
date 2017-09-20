from django import forms
from .models import MultipleBooks,MultiAuthoeBooks
class BookForm(forms.ModelForm):
	class Meta:
		model=MultipleBooks
		fields='__all__'
