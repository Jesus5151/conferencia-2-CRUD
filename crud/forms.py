from django import forms
from .models import Book, Author


class BookForm(forms.ModelForm):
    titulo = forms.CharField(widget=forms.TextInput(attrs={'class': 'field form-control'}))
    autor = forms.ModelChoiceField(queryset=Author.objects.all(), widget=forms.Select(attrs={'class': 'field form-control'}))
    precio = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'field form-control', 'type': 'number' }))
    
    class Meta:
        model = Book
        fields = ['titulo','autor', 'precio']

    