from django import forms
from .models import MyDuffle, Category, Warehouse, Hike, Bike, WaterRafting, BP


class DuffleForm(forms.ModelForm):
    class Meta:
        model = MyDuffle
        fields = ['name_duffle', 'heft', 'expiration_date', 'category', 'warehouse']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name_category']


class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = ['name_waterhouse']


class HikeForm(forms.ModelForm):
    class Meta:
        model = Hike
        fields = ['id_duffle']


class BikeForm(forms.ModelForm):
    class Meta:
        model = Bike
        fields = ['id_duffle']


class WaterRaftingForm(forms.ModelForm):
    class Meta:
        model = WaterRafting
        fields = ['id_duffle']


class BPForm(forms.ModelForm):
    class Meta:
        model = BP
        fields = ['id_duffle']
