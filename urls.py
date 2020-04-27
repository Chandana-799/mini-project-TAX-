from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',views.indexView,name="home"),
    path('taxpage/',views.taxpageView,name="taxpage_url"),
    path('login/',LoginView.as_view(),name="login_url"),
    path('register/',views.registerView,name="register_ url"),
    path('commonpage/',views.commonpageView,name="commonpage_url"),
    path('payment/',views.paymentView,name="payment_url"),
    
    path('logout/',LogoutView.as_view(next_page='taxpage'),name="logout"),
    ]

# Create your views here.
