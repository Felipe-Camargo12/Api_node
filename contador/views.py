from django.shortcuts import render
from django.views.generic import View
from .models import Dados

class DadosListView(View):
    def get(self, request, *args, **kwargs):
        dados = Dados.objects.all().first()  # Obtém os dados, supondo que só haja um objeto na tabela
        return render(request, 'template.html', {'dados': dados})
    
    def post(self, request, *args, **kwargs):
        dados = Dados.objects.all().first() 
        dados.sensor = request.POST.get('sensor')
        dados.save()
        return render(request, 'template.html', {'dados': dados})