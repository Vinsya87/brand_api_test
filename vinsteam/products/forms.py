from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Название'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Описание'}),
            'price': forms.NumberInput(attrs={
                'class': 'form-control', 'placeholder': 'Цена'}),
        }
        labels = {
            'name': 'Название',
            'description': 'Описание',
            'price': 'Цена',
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name.strip():
            raise forms.ValidationError(
                "Название не должно быть пустым.")
        return name

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError(
                "Цена должна быть положительной.")
        return price
