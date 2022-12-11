from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from django.shortcuts import render
from familia.forms import PersonaForm, BuscarPersonasForm, MascotaForm, VehiculoForm

from familia.models import Persona, Mascota, Vehiculo

def index(request):
    personas = Persona.objects.all()
    mascota = Mascota.objects.all()
    vehiculo = Vehiculo.objects.all()
    template = loader.get_template('familia/lista_familiares.html')
    context = {
        'personas': personas,
        "mascota": mascota,
        "vehiculo": vehiculo,
    }
    return HttpResponse(template.render(context, request))


def agregar(request):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue cargada con éxito
    '''

    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            altura = form.cleaned_data['altura']
            Persona(nombre=nombre, apellido=apellido, email=email, fecha_nacimiento=fecha_nacimiento, altura=altura).save()

            return HttpResponseRedirect("/")
    elif request.method == "GET":
        form = PersonaForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

    
    return render(request, 'familia/form_carga.html', {'form': form})

def mascota(request):
     if request.method == "POST":
        form = MascotaForm(request.POST)
        if form.is_valid():

            animal = form.cleaned_data['animal']
            edad = form.cleaned_data['edad']
            Mascota(animal=animal, edad=edad).save()

            return HttpResponseRedirect("/")
     elif request.method == "GET":
        form = MascotaForm()
     else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

     return render(request, 'familia/form_mascota.html', {'form': form})
     
def vehiculo(request):
    if request.method == "POST":
        form = VehiculoForm(request.POST)
        if form.is_valid():

            Marca = form.cleaned_data['Marca']
            dueño = form.cleaned_data['dueño']
            Vehiculo(Marca=Marca, dueño=dueño).save()

            return HttpResponseRedirect("/")
    elif request.method == "GET":
        form = VehiculoForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

    return render(request, 'familia/form_vehiculo.html', {'form': form})


def borrar(request, identificador):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue eliminada con éxito        
    '''
    if request.method == "GET":
        persona = Persona.objects.filter(id=int(identificador)).first()
        mascota = Mascota.objects.filter(id=int(identificador)).first()
        vehiculo = Vehiculo.objects.filter(id=int(identificador)).first()
        if persona:
            persona.delete()
        elif mascota:
            mascota.delete()
        elif vehiculo:
            vehiculo.delete()

        return HttpResponseRedirect("/")
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")


def actualizar(request, identificador):
    '''
    TODO: implementar una vista para actualización
    '''
    pass


def buscar(request):
    if request.method == "GET":
        form_busqueda = BuscarPersonasForm()
        return render(request, 'familia/form_busqueda.html', {"form_busqueda": form_busqueda})

    elif request.method == "POST":
        form_busqueda = BuscarPersonasForm(request.POST)
        if form_busqueda.is_valid():
            palabra_a_buscar = form_busqueda.cleaned_data['palabra_a_buscar']
            personas = Persona.objects.filter(nombre__icontains=palabra_a_buscar)
            mascota = Mascota.objects.filter(animal__icontains=palabra_a_buscar)
            vehiculo = Vehiculo.objects.filter(Marca__icontains=palabra_a_buscar)

        return  render(request, 'familia/listar_resultados.html', {'mascota': mascota,'personas': personas, 'vehiculo': vehiculo})
    