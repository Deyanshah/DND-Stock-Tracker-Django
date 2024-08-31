from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Inventory
# pylint: disable=E1101

# Create your views here.
def home(request):
    return render(request, 'home.html')

# def red_adjust_stock_ad(request):
#     if request.method=="POST":
#         products=Inventory.objects.all()
#         context={
#             'products':products
#         }
#     return render(request, 'admin_page.html',context)

def display_quant(request):
    
    products = Inventory.objects.all()
    context = {
        'products': products
    }
    return render(request, 'customer_page.html', context)

def admin(request):
    products = Inventory.objects.all()
    context = {'products': products}
    return render(request, 'admin_page.html', context)

def update_quant(request):
    if request.method == "POST":
        try:
            action = request.POST.get('action')
            if action:
                action_type, pid = action.split('_')
                pid = int(pid)
                quantity_change = int(request.POST.get(f'quantity_{pid}'))
                product = Inventory.objects.get(pid=pid)
                
                if action_type == 'add':
                    product.quantity += quantity_change
                    product.save()
                    messages.success(request, 'Quantity added successfully.')
                elif action_type == 'sub':
                    if product.quantity >= quantity_change:
                        product.quantity -= quantity_change
                        product.save()
                        messages.success(request, 'Quantity subtracted successfully.')
                    else:
                        messages.error(request, 'Not enough products to reduce.')
            else:
                messages.error(request, 'No action provided.')
        
        except Inventory.DoesNotExist:  # Custom Exception
            messages.error(request, 'Product not found.')
        
        except ValueError:  # Predefined Exception
            messages.error(request, 'Invalid quantity provided.')
        
        except Exception as e:  # Predefined Exception
            messages.error(request, f'An error occurred: {str(e)}')
        
        return redirect('admin')

    return redirect('admin')