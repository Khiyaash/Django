"""from django import forms
from .models import Items

class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['item_name','item_desc','item_price','item_image']
"""

from django import forms
from .models import Items

class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['item_name', 'item_desc', 'item_price', 'item_image']
        widgets = {
            'item_name': forms.TextInput(attrs={'class': 'form-control border-primary fw-bold'}),
            'item_desc': forms.TextInput(attrs={'class': 'form-control border-success fw-bold'}),
            'item_price': forms.NumberInput(attrs={'class': 'form-control border-warning fw-bold'}),
            'item_image': forms.TextInput(attrs={'class': 'form-control border-info fw-bold'}),
        }
