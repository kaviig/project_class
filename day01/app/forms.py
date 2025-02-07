from django import forms
from .models import Category, unit, Item, Supplier, Order, Employee

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'  

class unitForm(forms.ModelForm):
    class Meta:
        model = unit
        fields = '__all__'

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__' 

class OrderForm(forms.ModelForm):
    class  Meta:
        model = Order
        fields = '__all__'

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'