from urllib import request
from django.shortcuts import render, redirect
from .models import Model_Submodels
from .forms import AddPost

def home(request):
    return render(request, 'home.html')

def posts(request):
    all_posts = Model_Submodels.objects.all()
    return render(request, 'posts.html', {'posts': all_posts})

def post(request, id):
    try:
        post = Model_Submodels.objects.get(id=id)
    except:
        post = 'No Such Post'
    return render(request, 'post.html', {'post': post})

def add_post(request):

    if request.method == 'POST':
        new_form = AddPost(request.POST, request.FILES)

        if new_form.is_valid():
            post = Model_Submodels()
            post.vehicle = new_form.cleaned_data['vehicle']
            post.vehicle_model = new_form.cleaned_data['vehicle_model']
            post.engine_capacity = new_form.cleaned_data['engine_capacity']
            post.transmission_type = new_form.cleaned_data['transmission_type']
            post.fuel_system_type = new_form.cleaned_data['fuel_system_type']
            post.fuel_consumption_requirements = new_form.cleaned_data['fuel_consumption_requirements']
            post.fuel_cost_without_taxes = new_form.cleaned_data['fuel_cost_without_taxes']
            post.market_prise = new_form.cleaned_data['market_prise']
            post.avarege_to_prise = new_form.cleaned_data['avarege_to_prise']
            post.avarege_battery_prise = new_form.cleaned_data['avarege_battery_prise']
            post.avarege_tires_prise = new_form.cleaned_data['avarege_tires_prise']
            post.avarege_maintenance_prise = new_form.cleaned_data['avarege_maintenance_prise']
            post.amortization_period = new_form.cleaned_data['amortization_period']
            post.image = new_form.cleaned_data['image']
            post.submodel_description = new_form.cleaned_data['submodel_description']
            post.save()

            return redirect('posts')

    else:
        new_form = AddPost()
    return render(request, 'add_post.html', {'new_form': new_form})