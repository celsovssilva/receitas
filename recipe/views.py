from django.shortcuts import render
from .models import Receita
from django.shortcuts import redirect
from .forms import ReceitaForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):
    return render(request, 'recipe/home.html')

@login_required
def inserir(request):
    if request.method == 'POST':
       form= ReceitaForm(request.POST, request.FILES)
       if form.is_valid():
           form.save()
           return redirect('home')
    else:
        form= ReceitaForm()
    return render(request, 'recipe/inserirreceita.html', {'form': form})

@login_required
def procurar(request):
    query= request.GET.get('q')
    receitas= []

    if query:
        receitas= Receita.objects.filter(name__icontains=query)
    context = {
        'receitas': receitas,
        'query': query,
    }
    return render(request, 'recipe/procurar.html', context)
@login_required
def recipe(request, pk):
    receita = Receita.objects.get(pk=pk)
    return render(request, 'recipe/receita.html', {'receita': receita})


