from django.shortcuts import render

from .models import Pizza

def index(request):
    #The home page for Pizzerias
    return render(request, 'pizzerias/index.html')

def pizzas(request):
    #show all Pizzas
    pizzas = Pizza.objects.order_by('date_added')
    context = {'pizzas': pizzas}
    return render(request, 'pizzerias/pizzas.html', context)

def pizza(request, topic_id):
    #show a single Pizza and all its enteries
    pizzaVarName = Pizza.objects.get(id=topic_id)
    print(pizzaVarName)
    entries = pizzaVarName.topping_set.order_by('-date_added')
    print(pizzaVarName.topping_set)
    context = {'pizza': pizzaVarName, 'entries': entries}
    return render(request, 'pizzerias/pizza.html', context)