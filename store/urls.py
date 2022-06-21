import checkout as checkout
from django.urls import path

from store.controller import authview, cart, checkout, order
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('collections', views.collections, name="collections"),
    path('collections/<str:slug>', views.collectionsview, name='collectionsview'),
    path('collections/<str:cate_slug>/<str:prod_slug>', views.productview, name='productview'),
    path('about.html', views.about, name='about'),
    path('register/', authview.register, name='register'),
    path('login/', authview.loginpage, name='loginpage'),
    path('logout/', authview.logoutpage, name='logoutpage'),

    path('add-to-cart', cart.addtocart, name='addtocart'),
    path('cart', cart.viewcart, name='cart'),
    path('update-cart', cart.updatecart, name='updatecart'),
    path('delete-cart-item', cart.deletecartitem, name='deletecartitem'),

    path('checkout', checkout.index, name='checkout'),
    path('placeorder', checkout.placeorder, name='placeorder'),

    path('my-orders', order.index, name='myorders'),
    path('view-order/<str:t_no>', order.vieworder, name='orderview'),

    # path('all_blogs', views.all_blogs, name='all_blogs'),
    # path('<int:blog_id>/', views.detail, name='detail'),

]
