from django.contrib import admin
from core.models import *
from django.forms import TextInput 



class MunicipioInlne(admin.TabularInline):
    model = Municipio
    extra = 1
class ProvinciaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Provincias',               {'fields': ['nome_provincia', 'lat', 'lon']}), ]
    inlines = [MunicipioInlne]
    list_display=('nome_provincia', 'lat', 'lon')
    list_display_links=('nome_provincia', 'lat', 'lon')
    list_filter = ['nome_provincia']
    search_fields = ['nome_provincia']
    list_per_page = 30
    save_on_top = True

class CasoInlne(admin.TabularInline):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '13'})},
        #models.ModelChoiceField:{'widget': Dropdown(attrs={'size':'4'})}
        }
    model = Caso
    extra = 1
    exclude=['descricao',]

class PacienteAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Dados pessoais',               {'fields': ['nome_paciente', 'sobrenome', 'birthdate']}),
         ('',               {'fields': ['municipio','sexo']}), ]
    inlines = [CasoInlne]
    list_display=('nome_paciente','sobrenome','birthdate','sexo', 'municipio')
    list_display_links=('nome_paciente','sobrenome','birthdate','sexo', 'municipio')
    list_filter = ['municipio__provincia','municipio']
    search_fields = ['nome_paciente','sobrenome']
    list_per_page = 30
    save_on_top = True


admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Caso)
admin.site.register(Municipio)





