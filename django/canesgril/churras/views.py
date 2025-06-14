from django.shortcuts import render

# Create your views here.
def index(request):
    dados ={'lista_pratos':
            {
            '1':'Picanha',
            '2':'Costela',
            '3':'Cupim',
            '4':'Fraldinha',
            '5':'Fraldinha na Mostarda',
            '6':'Contra Filé'
            }
    }
    return render(request, 'index.html', dados)
def churrasco(request):
    return render(request, 'churrasco.html')
def contato(request):
    return render(request, 'contato.html')
