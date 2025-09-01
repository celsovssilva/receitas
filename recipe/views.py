from django.shortcuts import render
from .models import Receita
from django.shortcuts import redirect
# Create your views here.
def home(request):
    return render(request, 'recipe/home.html')


def inserir(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        ingredients = request.POST.get('ingredients')
        preparationmethod = request.POST.get('preparationmethod')
        preparationtime = request.POST.get('preparationtime')
        
        
        Receita.objects.create(
            name=name,
            ingredients=ingredients,
            preparationmethod=preparationmethod,
            preparationtime=preparationtime
        )
        
        return redirect('home')
    
    return render(request, 'recipe/inserirreceita.html')

def procurar(request):
    query= request.GET.get('q')

    if query:
        receitas= Receita.objects.filter(name__icontains=query)
    else:    
        receitas= Receita.objects.all()
    return render(request, 'recipe/procurar.html', {'receitas': receitas})

def recipe(request, pk):
    receita = Receita.objects.get(pk=pk)
    return render(request, 'recipe/recipe_detail.html', {'receita': receita})