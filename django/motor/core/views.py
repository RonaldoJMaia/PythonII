from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def contato(request):
    context = { 
        'nome':'M otorWeb',
        'fone':'17996436097',
        'email':'ronaldojmaia@gmail.com',
        'endereco':'Rua Atalaia, 140',
        'cep':'15802220',
        'cidade':'Catanduva',
        'estado':'SP'
        }
    return render(request, 'contato.html', context)