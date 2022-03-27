from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('review/', views.review, name='review'),
    path('contact/', views.contact, name='contact'), 
    path('price/', views.price, name='price'), 
    path('course/', views.course, name='course'), 
    path('teacher/', views.teacher, name='teacher'),
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
    path('dashboard/', views.dashboard, name="dashboard"),  
    path('logout/', views.logoutUser, name="logout"),
    #path('price/home/', views.price, name='price/home'),
    #path('price/course/', views.course, name='price/course'), 
    #path('price/price/', views.price, name='price/price'), 
    #path('price/review/', views.review, name='price/review'), 
    #path('price/contact/', views.contact, name='price/contact'), 
]