from django.forms import ModelForm, TextInput
from weather.models.models import City 

class CityForm(ModelForm):
    class Meta:
        model = City 
        fields = ['name']
        widgets = {'name' : TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'})}