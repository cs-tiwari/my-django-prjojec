from home import views
from django.urls import path

urlpatterns = [
    path('', views.index,name='home'),  
    path('about/', views.about,name='about'),  
    path('services/', views.services,name='services'),  
    path('contact/', views.contact,name='contact'), 
    # path('update/<pk:int>', views.update,name='update'), 
    

]
