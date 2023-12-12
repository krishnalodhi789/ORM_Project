from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Buyer,Product,Buyer_wallet
# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {"products":products})

def buyersignup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2 :            
            user = User.objects.create_user(username=username,email=email,password=password1)
            buyer = Buyer.objects.create(user=user, phone=phone, city=city, full_name=full_name)
            buyer.save()            
            return redirect("buyerlogin")
        else:
            return redirect("buyersignup")
            
    return render  (request, 'signup.html')


def buyerlogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        seller = authenticate(username = username, password=password)
        print(seller)
        if seller :
            login(request, seller)
            return redirect('index')
        else:
            return redirect('buyerlogin')
    return render  (request, 'login.html')


def buyerlogout(request):
    logout(request)
    return redirect("buyerlogin")

@login_required(login_url="buyerlogin")
def userbuy(request,id):
    product = Product.objects.get(id=id)
    buyer = Buyer.objects.get(user_id=request.user.id)
    print(buyer.id)
    product.buyer_id =buyer.id
    product.save()
    buyer_wallet = Buyer_wallet(buyer=buyer,product=product)
    buyer_wallet.save()
    return redirect('buyerwallet')
  
@login_required(login_url="buyerlogin")   
def buyerwallet(request):
    buyer = Buyer.objects.get(user_id=request.user.id)
    data = Buyer_wallet.objects.filter(buyer_id=buyer.id)
    print(data)
    return render(request, 'wallet.html',{'data':data})