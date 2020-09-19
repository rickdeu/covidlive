from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from core.models import *
from datetime import date, timedelta
from django.utils import timezone





def home(request):
    positovos=Caso.objects.filter(estado_caso='Positivo').count()
    recuperado=Caso.objects.filter(estado_caso='Recuperado').count()
    falecido=Caso.objects.filter(estado_caso='Morto').count()
    ativo= positovos-(recuperado+falecido)
    caso_provincia = Caso.objects.all().order_by('paciente__municipio__provincia__nome_provincia')#[:5]
    caso_mes = Caso.objects.all().order_by('created_at__month')#[:5]
    data = timezone.now()




    #Dicionario de dados, para os casos por provincias
    casos_estados = []
    provincias = set()
    for x in caso_provincia:
        if x.paciente.municipio.provincia.nome_provincia not in provincias:
            provincias.add(x.paciente.municipio.provincia.nome_provincia)
            provincia = {
                'numero': x.paciente.municipio.provincia.pk,
                'lat': x.paciente.municipio.provincia.lat,
                'lon': x.paciente.municipio.provincia.lon,
                'nome_provincia': x.paciente.municipio.provincia.nome_provincia,
                'positivo': x.casos_positivos(x.paciente.municipio.provincia.nome_provincia),
                'recuperado': x.casos_recuperados(x.paciente.municipio.provincia.nome_provincia),
			    'morte': x.casos_mortes(x.paciente.municipio.provincia.nome_provincia),
                'ativo':x.casos_positivos(x.paciente.municipio.provincia.nome_provincia).count()-(x.casos_recuperados(x.paciente.municipio.provincia.nome_provincia).count()+x.casos_mortes(x.paciente.municipio.provincia.nome_provincia).count()),
                'total_provincia': x.total_provincia(x.paciente.municipio.provincia.nome_provincia),
            }
            # Guardamos o dicionario de casos por provincia na nossa lista
            #Append: Insere um item no final da lista.
            casos_estados.append(provincia)
     
    #Dicionario de dados, para os casos por mês
    casos_estados_mes = []
    meses = set()
    for x in caso_mes:
        if x.created_at.month not in meses:
            meses.add(x.created_at.month)
            mes = {
                'mes': x.created_at.month,
                'nome_mes':x.nome_mes,
                'positivo': x.casos_positivos_mes(x.created_at.month),
                    'recuperado': x.casos_recuperados_mes(x.created_at.month),
			    'morte': x.casos_mortes_mes(x.created_at.month),
                'ativo':x.casos_positivos_mes(x.created_at.month).count()-(x.casos_recuperados_mes(x.created_at.month).count()+x.casos_mortes_mes(x.created_at.month).count()),
            }
            # Guardamos o dicionario de casos na nossa lista
            casos_estados_mes.append(mes)
  
    template_name = 'core/dashboard.html'
    context = {'positovos':positovos, 'recuperado':recuperado, 
    'falecido':falecido, 'ativo':ativo,
     'casos_estados':casos_estados, 'casos_estados_mes':casos_estados_mes, 'data':data}
    return render(request, template_name, context)
