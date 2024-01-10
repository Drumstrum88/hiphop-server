"""hiphop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from codecs import register_error
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from hiphopapi.views import OrderView, ItemView
from hiphopapi.views.auth import check_user
from hiphopapi.views.order_items_views import OrderItemView
from hiphopapi.views.order_type_views import OrderTypeView
from hiphopapi.views.payment_type_views import PaymentTypeView




router = routers.DefaultRouter(trailing_slash=False)
router.register(r'orders', OrderView, 'order')
router.register(r'items', ItemView, 'item')
router.register(r'orderitems', OrderItemView, 'orderitem')
router.register(r'ordertypes', OrderTypeView, 'ordertype')
router.register(r'paymenttypes', PaymentTypeView, 'paymenttype')


urlpatterns = [
    path('admin/', admin.site.urls),
   path('', include(router.urls)),
     path('register', register_error),
    path('checkuser', check_user),
]
