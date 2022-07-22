from django.urls import path

from . import views

urlpatterns = [
	path('',views.index,name='index'),
	path('register/',views.registerPage,name="register"),
	path('login/',views.loginPage,name="login"),
	path('logout/',views.LogoutUser,name="logout"),
	path('search/',views.search,name="search"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('products/', views.products, name="products"),
	path('update_item/',views.updateItem,name="update_item")
]