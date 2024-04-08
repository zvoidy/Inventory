from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import *
import os

# Create your views here.
def home(request):
    return render(request,'index.html')

def add(request):
    return render(request, 'add.html')
def add_item(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        
        # Check if the item already exists
        existing_item = InventoryItem.objects.filter(item_name=item_name).first()
        if existing_item:
            # Update the existing item
            existing_item.quantity += int(quantity)
            existing_item.price = price
            existing_item.save()
            messages.success(request, 'Item updated successfully!')
        else:
            # Create a new InventoryItem object and save it to the database
            new_item = InventoryItem.objects.create(
                item_name=item_name,
                quantity=quantity,
                price=price
            )
            messages.success(request, 'Item added successfully!')
        
        # Redirect to a success page or any other page as needed
        return render(request, 'index.html')  # Assuming 'index' is the name of the homepage URL pattern
    else:
        # Handle GET requests if needed
        pass


def sell(request):
    return render(request, 'sell.html')
def sell_item(request):
    if request.method == 'POST':
        # Get form data
        item_name = request.POST.get('item_name')
        quantity = int(request.POST.get('quantity'))
        
        # Check if item already exists in the database
        try:
            item = InventoryItem.objects.get(item_name=item_name)
            quan = get_object_or_404(InventoryItem, item_name=item_name)
            quan=quan.quantity
            # If item exists, update its quantity by subtracting the provided quantity
            if quan>=1:
                item.quantity -= quantity
                item.save()

                itemm = get_object_or_404(InventoryItem, item_name=item_name)
                # Get the price of the item
                price = itemm.price

                sale = Sales.objects.create(
                    item_name=item_name,
                    quantity=quantity,
                    price=price*quantity
                )
            else:
                return render(request, 'er1.html')

        except:
            return render(request, 'er1.html')
        
        return redirect('home')  # Redirect to the home page or any other page
        
    return render(request, 'add.html')  # Render the add.html template for GET requests


def update(request):
    return render(request, 'update.html')
def update_item(request):
    if request.method == 'POST':
        # Get form data
        item_name = request.POST.get('item_name')
        quantity = int(request.POST.get('quantity'))
        price = request.POST.get('price')
        
        # Check if item already exists in the database
        try:
            item = InventoryItem.objects.get(item_name=item_name)
            # If item exists, update its quantity by subtracting the provided quantity
            
            item.quantity = quantity
            item.price = price
            item.save()
        except:
            return render(request, 'er2.html')
        
        return redirect('home')  # Redirect to the home page or any other page
        
    return render(request, 'add.html')  # Render the add.html template for GET requests

def remove(request):
    return render(request, 'remove.html')
def remove_item(request):
    if request.method == 'POST':
        # Get form data
        item_name = request.POST.get('item_name')
        
        # Check if item already exists in the database
        try:
            item = InventoryItem.objects.get(item_name=item_name)
            # If item exists, update its quantity by subtracting the provided quantity
            item.delete()

        except:
            return render(request, 'er2.html')
        
        return redirect('home')  # Redirect to the home page or any other page
        
    return render(request, 'add.html')  # Render the add.html template for GET requests

def transac(request):
    items = Sales.objects.all()
    return render(request, 'transac.html', {'items': items})

def display(request):
    items = InventoryItem.objects.all()
    return render(request, 'display.html', {'items':items})
