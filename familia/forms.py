from django import forms

class PersonaForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellido = forms.CharField(label="Apellido", max_length=100)
    email = forms.EmailField(label="Correo Electronico")
    fecha_nacimiento = forms.DateField(label="fecha_nacimiento", input_formats=["%d/%m/%Y"],
    widget=forms.TextInput(attrs={'placeholder': '01/01/2004'}))
    altura = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': "1.85 m"}))

class BuscarPersonasForm(forms.Form):
    palabra_a_buscar = forms.CharField(label="Buscar")

class MascotaForm(forms.Form):
    animal = forms.CharField(label="Animal", max_length=100)
    edad =  forms.IntegerField(label="Edad")

class VehiculoForm(forms.Form):
    Marca = forms.CharField(label="Marca", max_length=100)
    dueño = forms.CharField(label="Dueño", max_length=100)




