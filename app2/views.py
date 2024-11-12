from django.shortcuts import render,redirect, get_object_or_404
from .models import Products,QuickLink,UserDetail,Phonenumber
import urllib.parse
from django.db.models import Q
from django.contrib import messages
# Create your views here.



def cartItem(request):
  phone_number = list(Phonenumber.objects.values_list('phone_number', flat=True))


  if request.method == 'POST':
    name = request.POST['name']
    email = request.POST['email']

    if (name == "" or  email==""):
      messages.error(request, 'All Field Required ')
    else:
      if (UserDetail.objects.filter(name = name, email= email).exists()):
        messages.warning(request, 'Your details Already recorded')
        return redirect('cart-cart-items')
      else:
        user_detail = UserDetail.objects.create(name=name, email=email)
        user_detail.save()
        messages.success(request, 'Thank You Your details recorded')
        return redirect('cart-cart-items')
  return render(request, 'cart.html',{'phone_number':phone_number})


def home(request):
  all_link = QuickLink.objects.all()

  if request.method == 'POST':
    name = request.POST.get('name')
    phone_number = request.POST.get('phone')
    comment = request.POST.get('comment')

    message = (
      f"Thougth:- \n"
      f"Name :  {name}\n"
      f"phone number: {phone_number}\n"
      f"\nComment: '{comment}' "
       )

    whatsupp_number = '+255715292253'
    encode_message = urllib.parse.quote(message)
    whatsupp_url = f"https://wa.me/{whatsupp_number}?text={encode_message}"
    return redirect(whatsupp_url)
  

  product = Products.objects.filter(this_product_available=True)[:8]
  show_inslider = Products.objects.filter(this_product_available= True)[:4]

  context = {'product':product,'all_link':all_link,'show_inslider':show_inslider}
  return render(request, 'home-web.html',context)

def all_product(request):
  all_prod = Products.objects.filter(this_product_available =True)
  context = {'all_prod':all_prod}
  return render(request,'product.html',context)

def searchResult(request):
  query = request.GET.get('q')
  result = []
  if query:
    result = Products.objects.filter(Q(product_name__icontains=query)|Q(selling_price__icontains=query))
  return render(request, 'search.html',{'query':query,'result':result})
