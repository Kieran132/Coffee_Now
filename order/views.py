from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CoffeeBean
from .forms import BeanForm


def coffee_list(request):
    coffee_beans = CoffeeBean.objects.all()
    return render(
        request, 'coffee_list.html', {'coffee_beans': coffee_beans})


def coffee_detail(request, id):
    coffee = get_object_or_404(CoffeeBean, pk=id)
    form = BeanForm()

    context = {
        'coffee': coffee,
        'form': form
    }
    return render(request, 'coffee_detail.html', context)


@login_required
def add_product(request):
    form = BeanForm
    if request.method == 'POST':
        form = BeanForm(request.POST, request.FILES)
        print("errors in form", form.errors)
        if form.is_valid():
            print("Form submitted")
            form.save()
            return redirect('coffee_list')
        else:
            messages.error(
                request,
                'Error adding product, please check the the form is valid')     
    return render(request, 'add_product.html', {'form': form})


@login_required
def edit_product(request, coffee_id):
    coffee = get_object_or_404(CoffeeBean, pk=coffee_id)
    form = BeanForm(instance=coffee)
    if request.method == 'POST':
        form = BeanForm(request.POST, request.FILES, instance=coffee)
        if form.is_valid():
            print("Form submitted")
            form.save()
            return redirect('coffee_list')
        else:
            messages.error(
                request,
                'Error adding product, please check the the form is valid')
    else:
        form = BeanForm(instance=coffee)
    
    context = {
        'form': form,
        'coffee': coffee
    }
       
    return render(request, 'edit_product.html', context)
