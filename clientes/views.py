from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente, Carro
import re
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def clientes(request):
    if request.method == 'GET':
        return  render(request,'clientes.html')
    elif request.method == 'POST':
        nome=request.POST.get('nome')
        sobrenome=request.POST.get('sobrenome')
        email=request.POST.get('email')
        cpf=request.POST.get('cpf')
        carros=request.POST.getlist('carros')
        placas=request.POST.getlist('placas')
        anos = request.POST.getlist('ano')
        
        cliente = Cliente.objects.filter(cpf=cpf)
        
        if cliente.exists():
            return render (request, 'clientes.html',{'nome':nome,'sobrenome':sobrenome,'email':email })
            
        if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
            return render (request, 'clientes.html',{'nome':nome,'sobrenome':sobrenome,'cpf':cpf })

        cliente = Cliente(
            nome = nome,
            sobrenome = sobrenome,
            email = email,
            cpf = cpf
        )

        for carro, placa, ano in zip(carros,placas,anos):
            car =  Carro(carro=carro, placa=placa, ano=ano, cliente=cliente)
            car.save()

        return HttpResponse('teste')
