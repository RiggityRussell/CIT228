from django.urls import path
from . import views

app_name='pizzerias'
urlpatterns=[
    #Home Page
    path('', views.index, name='index'),

    #Pizzas
    path('pizzas/', views.pizzas, name='pizzas'),

    #Single Pizza
    path('pizzas/<int:topic_id>/', views.pizza, name='pizza')
]