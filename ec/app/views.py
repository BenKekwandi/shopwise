from django.db.models import Count
from django.shortcuts import render,redirect
from django.views import View
from .models import Link,Customer,Wish
from .forms import CustomerRegistrationForm,CustomerProfileForm
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.
def home(request):
    return render(request,"app/home.html")
class CategoryView(View):
    def get(self,request,val):
        products=Link.objects.filter(category=val)
        titles=Link.objects.filter(category=val).values('name')
        return render(request,"app/category.html",{'products': products, 'titles': titles})
    
class CustomerRegistrationView(View):
    def get(self,request):
        form= CustomerRegistrationForm()
        return render(request,'app/customerregistration.html',locals())
    def post(self,request):
        form= CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations!User Register Successfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request,'app/customerregistration.html',locals())

class ProfileView(View):
    def get(self,request):
        form= CustomerProfileForm()
        return render(request,'app/profile.html',locals())
    def post(self,request):
        form= CustomerProfileForm(request.POST)
        if form.is_valid():
            user=request.user
            name=form.cleaned_data['name']
            city=form.cleaned_data['city']
            mobile=form.cleaned_data['mobile']

            reg=Customer(user=user,city=city,mobile=mobile)
            reg.save()
            messages.success(request,"congratulations!Profile is saved successfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request,'app/profile.html',locals())

class WishListView(LoginRequiredMixin, View):
    login_url = '/accounts/login'
    redirect_field_name='next'
    def get(self, request):
        wishes = Wish.objects.filter(user=request.user)
        products=[]
        titles = []
        for wish in wishes:
            products.append(wish.product)
            titles.append(wish.product.name)
        return render(request, 'app/wishlist.html', {'products': products, 'titles':titles})
    
@login_required(login_url='/accounts/login')
def addToWishList(request,id):
    wish=Wish()
    wish.user=request.user
    wish.product=Link.objects.get(id=id)
    wish.save()
    return redirect('/wishlist')


@login_required(login_url='/accounts/login')
def removeFromWishList(request, id):
    wishes = Wish.objects.filter(product=Link.objects.get(id=id))
    for wish in wishes:
        wish.delete()
    return redirect('/wishlist')

def search(request):
    query = request.GET.get('query', '')
    results = Link.objects.filter(name__icontains=query).values('id', 'name') if query else []
    data = list(results) 
    return JsonResponse(data, safe=False)

def showProduct(request, id):
    product = Link.objects.get(id=id)
    return render(request, 'app/product.html', {'product': product})

def showAllProducts(request):
    products = Link.objects.all()
    return render(request, 'app/all_products.html', {'products': products})

def logout(request):
    auth_logout(request)
    return redirect('/account/login')