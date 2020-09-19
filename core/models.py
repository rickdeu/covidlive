from django.db import models
from django.db.models import Avg, Count
from datetime import date, timedelta


#Model da provincia
class Provincia(models.Model):
    class Meta:
        verbose_name = 'Província'
        verbose_name_plural = 'Pronvíncias'
        ordering = ['-nome_provincia']

    nome_provincia = models.CharField(
        max_length=100, 
        verbose_name='Provincia',
        null=True,
        blank=False,
        help_text='Informe o nome da província'
        )
    lat = models.CharField(
        max_length=100, 
        verbose_name='Latitude',
        null=True,
        blank=True,
        help_text='Latitude'
        )
    lon = models.CharField(
        max_length=100, 
        verbose_name='Longitude',
        null=True,
        blank=True,
        help_text='Longitude'
        )
 
    def __str__(self):
        return self.nome_provincia

#Model do municipio
class Municipio(models.Model):
    class Meta:
        verbose_name = 'Município'
        verbose_name_plural = 'Municípios' 
        ordering = ['-nome_municipio']

    nome_municipio = models.CharField(
        max_length=100, 
        verbose_name='Município',
        null=True,
        blank=False,
        help_text='Informe o nome do município'
        )
    provincia = models.ForeignKey(
        Provincia, 
        verbose_name='Província',
        on_delete=models.CASCADE
        )
    lat = models.CharField(
        max_length=100, 
        verbose_name='Latitude',
        null=True,
        blank=True,
        help_text='Latitude'
        )
    lon = models.CharField(
        max_length=100, 
        verbose_name='Longitude',
        null=True,
        blank=True,
        help_text='Longitude'
        )
    def __str__(self):
        return self.nome_municipio

 
 #Informações do paciente
class Paciente(models.Model):
    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering = ['nome_paciente']
    
    nome_paciente = models.CharField(
        max_length=100, 
        verbose_name='Nome',
        null=True,
        blank=True,
        help_text='Informe seu nome'
        )
    sobrenome = models.CharField(
        max_length=100, 
        verbose_name='Sobrenome',
        null=True,
        blank=True,
        help_text='Informe seu Sobrenome'
        )
    birthdate = models.DateField(
        blank=True,
        null=True,
        verbose_name='Data de nascimento',
        help_text='Informe sua data de nascimento',
        #format=settings.DATE_INPUT_FORMATS
        )
    municipio = models.ForeignKey(
        Municipio, 
        verbose_name='Município',
        on_delete=models.CASCADE
        )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        null=True,
        blank=True,
        verbose_name='Criado em'
        )
    sexoChoices =(
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        )
    
    sexo = models.CharField(
        verbose_name='Género',
        max_length=20,
        choices=sexoChoices,
        null=True,
        blank=True,
        )
    def __str__(self):
        return str(self.nome_paciente) + ' '+str(self.sobrenome)

class Caso(models.Model):
    class Meta:
        verbose_name = 'Caso'
        verbose_name_plural = 'Casos'
        ordering = ['paciente']
        unique_together = (('estado_caso', 'paciente'),)
    paciente = models.ForeignKey(
        Paciente, 
        verbose_name='Paciente',
        on_delete=models.CASCADE,
        help_text='Selecione o nome do paciente '
        )
    descricao=models.TextField(
        max_length=250, 
        verbose_name='Descrição do Caso',
        null=True,
        blank=True,
        help_text='Possiveis descrições sobre o caso'
        )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name='Criado em'
        ) 
    estado =(
        ('Positivo', 'Positivo'),
        ('Recuperado', 'Recuperado'),
        ('Morto', 'Morto'),
        )

    estado_caso = models.CharField(
        verbose_name='Estado',
        max_length=50,
        choices=estado,
        null=True,
        blank=True,
        )
   
    #Contador dos casos por provincias
    def casos_positivos(self, provincia):
        total=Caso.objects.filter(paciente__municipio__provincia__nome_provincia=provincia, estado_caso='Positivo').annotate(count=Count('estado_caso'))
        return total
    def casos_recuperados(self, provincia):
        total=Caso.objects.filter(paciente__municipio__provincia__nome_provincia=provincia, estado_caso='Recuperado').annotate(count=Count('estado_caso'))
        return total
    def casos_mortes(self, provincia):
        total=Caso.objects.filter(paciente__municipio__provincia__nome_provincia=provincia, estado_caso='Morto').annotate(count=Count('estado_caso'))
        return total
    def total_provincia(self, provincia):
        total=Caso.objects.filter(paciente__municipio__provincia__nome_provincia=provincia).annotate(count=Count('estado_caso'))
        return total


    def nome_mes(self):
        if(self.created_at.month==1):
            mes="Jan"
        elif(self.created_at.month==2):
             mes="Fev"
        elif(self.created_at.month==3):
             mes="Mar"
        elif(self.created_at.month==4):
             mes="Abr"
        elif(self.created_at.month==5):
             mes="Mai"
        elif(self.created_at.month==6):
             mes="Jun"
        elif(self.created_at.month==7):
             mes="Jul"
        elif(self.created_at.month==8):
             mes="Ago"
        elif(self.created_at.month==9):
             mes="Set"
        elif(self.created_at.month==10):
             mes="Out"
        elif(self.created_at.month==11):
             mes="Nov"
        elif(self.created_at.month==12):
             mes="Dez"
        return mes
    #Contador dos casos por mês
    def casos_positivos_mes(self, mes):
        total=Caso.objects.filter(created_at__month=mes, estado_caso='Positivo').annotate(count=Count('estado_caso'))
        return total
    def casos_recuperados_mes(self, mes):
        total=Caso.objects.filter(created_at__month=mes, estado_caso='Recuperado').annotate(count=Count('estado_caso'))
        return total
    def casos_mortes_mes(self, mes):
        total=Caso.objects.filter(created_at__month=mes, estado_caso='Morto').annotate(count=Count('estado_caso'))
        return total
