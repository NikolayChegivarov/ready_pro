from django.shortcuts import render
from .models import MyDuffle, Hike, Bike, WaterRafting, BP

from django.shortcuts import render, redirect
from .forms import DuffleForm, CategoryForm, WarehouseForm, HikeForm, BikeForm, WaterRaftingForm, BPForm

def home(request):
    """Домашняя страница представляет собой набор
    кнопок с доступом к различным наборам."""
    return render(request, 'home.html')


def view_equipment(request):  # Все снаряжение.
    equipment = MyDuffle.objects.all()
    return render(request, 'equipment.html', {'equipment': equipment})


def hike(request):  # Пеший поход.
    hike_equipment = Hike.objects.all()
    return render(request, 'hike.html', {'hike_equipment': hike_equipment})


def bike(request):  # Велопоход.
    bike_equipment = Bike.objects.all()
    return render(request, 'bike.html', {'bike_equipment': bike_equipment})


def water_rafting(request):  # Сплав.
    water_rafting_equipment = WaterRafting.objects.all()
    return render(request, 'water_rafting.html', {'water_rafting_equipment': water_rafting_equipment})


def bp(request):  # БП.
    bp_equipment = BP.objects.all()
    return render(request, 'bp.html', {'bp_equipment': bp_equipment})


# Создать снаряжение.
def create_duffle(request):
    if request.method == 'POST':
        form = DuffleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_equipment')
    else:
        form = DuffleForm()
    return render(request, 'create_duffle.html', {'form': form})


# Создать категорию.
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_equipment')
    else:
        form = CategoryForm()
    return render(request, 'create_category.html', {'form': form})


# Создать склад.
def create_warehouse(request):
    if request.method == 'POST':
        form = WarehouseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_equipment')
    else:
        form = WarehouseForm()
    return render(request, 'create_warehouse.html', {'form': form})


# Добавить в поход.
def add_to_hike(request):
    if request.method == 'POST':
        form = HikeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hike')
    else:
        form = HikeForm()
    return render(request, 'add_to_hike.html', {'form': form})


# Добавить в велосипед.
def add_to_bike(request):
    if request.method == 'POST':
        form = BikeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_equipment')
    else:
        form = BikeForm()
    return render(request, 'add_to_bike.html', {'form': form})


# Добавить в сплав.
def add_to_water_rafting(request):
    if request.method == 'POST':
        form = WaterRaftingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_equipment')
    else:
        form = WaterRaftingForm()
    return render(request, 'add_to_water_rafting.html', {'form': form})


# Добавить в БП.
def add_to_bp(request):
    if request.method == 'POST':
        form = BPForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_equipment')
    else:
        form = BPForm()
    return render(request, 'add_to_bp.html', {'form': form})
