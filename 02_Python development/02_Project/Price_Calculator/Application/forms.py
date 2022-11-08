from django import forms
from .models import Model_Submodels
from django.core.exceptions import ValidationError

class AddPost(forms.Form):
    
    vehicle = forms.CharField(max_length=10)
    vehicle_model = forms.CharField(max_length=20)
    engine_capacity = forms.DecimalField(max_digits=2, decimal_places=1)
    transmission_type = forms.ChoiceField(choices=Model_Submodels.TRANSMISSION_SYSTEM_TYPES)
    fuel_system_type = forms.ChoiceField(choices=Model_Submodels.FUEL_SYSTEM_TYPES)
    fuel_consumption_requirements = forms.DecimalField(max_digits=2, decimal_places=1)
    fuel_cost_without_taxes = forms.DecimalField(max_digits=3, decimal_places=2)
    market_prise = forms.IntegerField()
    avarege_to_prise = forms.IntegerField()
    avarege_battery_prise = forms.IntegerField()
    avarege_tires_prise = forms.IntegerField()
    avarege_maintenance_prise = forms.DecimalField(max_digits=3, decimal_places=2)
    amortization_period = forms.IntegerField()
    image = forms.ImageField()
    submodel_description = forms.CharField(widget=forms.Textarea())