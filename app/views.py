# Importing Various Requirement
from django.db.models import Count
from urllib import request
from django.shortcuts import render
from .models import Customer, Product
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomerProfileForm, CustomerRegistrationForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"app/home.html");

def about(request):
    return render(request,"app/about.html");

def contact(request):
    return render(request,"app/contact.html");

# Category View
class CategoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request,"app/category.html",locals())
    
# CategoryTitle View
class CategoryTitle(View):
    def get(self,request,val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request,"app/category.html",locals())


# ProductDetail View
class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,"app/productdetail.html",locals())

# CustomerRegistration View        
class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request,"app/customerregistration.html",locals())
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations!, You have been Successfully Registered!")
        else:
            messages.warning(request, "Invalid Data Input!")    
        return render(request,"app/customerregistration.html",locals())    

 
class ProfileView(View):
         def get(self,request):
             form = CustomerProfileForm()
             return render(request,"app/profile.html",locals())
         def post(self,request):
             form = CustomerProfileForm(request.POST) 
             if form.is_valid():
                 user = request.user
                 name = form.cleaned_data['name']
                 locality = form.cleaned_data['locality']
                 city = form.cleaned_data['city']
                 mobile = form.cleaned_data['mobile']
                 zipcode = form.cleaned_data['zipcode']
                 region = form.cleaned_data['region']
                 
                 reg = Customer(user=user,name=name,locality=locality,city=city,mobile=mobile,zipcode=zipcode,region=region)
                 reg.save()
                 messages.success(request, "Congratulations!, Your Profile have been Successfully Saved!")
             else:
                 messages.warning(request,"Invalid Input Data")
             return render(request,"app/profile.html",locals())
         
def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request,"app/address.html",locals())

class updateAddress(View):
    def get(self,request,pk):
           add = Customer.objects.get(pk=pk)
           form = CustomerProfileForm(instance=add)
           return render(request,"app/updateAddress.html",locals())
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data["name"]
            add.locality = form.cleaned_data["locality"]
            add.city = form.cleaned_data["city"]
            add.mobile = form.cleaned_data["mobile"]
            add.zipcode = form.cleaned_data["zipcode"]
            add.region = form.cleaned_data["region"]
            add.save()
            messages.success(request,"Congratulations your Profile have been Updated Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return redirect ("address")    