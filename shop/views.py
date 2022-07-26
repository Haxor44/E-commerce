from django.shortcuts import render,redirect
from .models import Product,Customer,Order,OrderItem
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime
import json
from .forms import CreateUser
from .models import Customer,Product,ShippingAddress


# Create your views here.
def index(request):
	if request.user.is_authenticated:

		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer,complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
		print("Cart item is:",cartItems)

	else:
		items = []
		order = {'get_cart_total':0,'get_cart_items':0}
		cartItems = order['get_cart_items']


	#Products with inventory less than 10
	queryset1 = Product.objects.all()

	return render(request,"shop/index.html", {"products":queryset1,"cartItems":cartItems})

def products(request):
	if request.user.is_authenticated:

		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer,complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
		print("Cart item is:",cartItems)

	else:
		items = []
		order = {'get_cart_total':0,'get_cart_items':0}
		cartItems = order['get_cart_items']

	queryset1 = Product.objects.all()
	return render(request,"shop/products.html", {"products":queryset1,"cartItems":cartItems})

def search(request):
	if request.method == 'POST':
		searched = request.POST['search']

		products = Product.objects.filter(title__icontains=searched)
		return render(request,"shop/search.html",{"products":products,"searched":searched})

	else:
		return render(request,"shop/search.html",{})

def registerPage(request):
	customer = Customer()
	form = CreateUser()


	if request.method == 'POST':
		form = CreateUser(request.POST)
		if form.is_valid():
			#form.save()
			customer.user = form.save()
			customer.save()

			messages.success(request,"Account was created successfully")
			return redirect('login')
	context={'form':form}
	return render(request,'shop/register.html',context)

def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect('index')
		else:
			messages.info(request,"Username or Password is incorrect")
	context = {}
	return render(request,"shop/login.html",context)


def LogoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url="login")
def cart(request):

	if request.user.is_authenticated:

		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer,complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
		print("Cart item is:",cartItems)

	else:
		items = []
		order = {'get_cart_total':0,'get_cart_items':0}
		cartItems = order['get_cart_items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'shop/cart.html', context)

def checkout(request):
	if request.user.is_authenticated:

		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer,complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
		print("Cart item is:",cartItems)

	else:
		items = []
		order = {'get_cart_total':0,'get_cart_items':0}
		cartItems = order['get_cart_items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'shop/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print("Product id is: ", productId)
	print("action id is: ", action)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	#change value of order if it already exists
	order, created = Order.objects.get_or_create(customer=customer,complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order,product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity +1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity-1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()
	return JsonResponse("Item Added",safe=False)

def completeOrder(request):
	print('Data ', request.body)
	data = json.loads(request.body)
	transaction_id = datetime.datetime.now().timestamp()

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer,complete=False)
		total = float(data['shipping']['total'])
		order.transaction_id = transaction_id

		if total == order.get_cart_total:
			order.complete = True
		order.save()

		ShippingAddress.objects.create(customer=customer,order=order,address=data['shipping']['address'],city=data['shipping']['city'],state=data['shipping']['county'],zipcode=data['shipping']['zip'])


	else:
		print("USer is not logged in!!!")

	return JsonResponse("Order Completed!!!", safe=False)
