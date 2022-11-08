from django.db import models
from django.core.exceptions import ValidationError

class Model_Submodels(models.Model):

    FUEL_SYSTEM_TYPES = [('Patrol', 'p'), ('Disel', 'd'), ('Gas', 'g')]
    TRANSMISSION_SYSTEM_TYPES = [('Four-speed automatic transmission', '4A'), ('Five-speed automatic transmission', '5A'),
    ('Six-speed automatic transmission', '6A'), ('Four-speed manual transmission', '4M'), ('Five-speed manual transmission', '5M'),
    ('Six-speed manual transmission', '6M')]
    
    vehicle = models.CharField(max_length=10, blank=False)
    vehicle_model = models.CharField(max_length=20, blank=False)
    engine_capacity = models.DecimalField(max_digits=2, decimal_places=1, blank=False)
    transmission_type = models.CharField(choices=TRANSMISSION_SYSTEM_TYPES, max_length=50)
    fuel_system_type = models.CharField(choices=FUEL_SYSTEM_TYPES, max_length=10)
    fuel_consumption_requirements = models.DecimalField(max_digits=2, decimal_places=1, blank=False)
    fuel_cost_without_taxes = models.DecimalField(max_digits=3, decimal_places=2, blank=False)
    market_prise = models.IntegerField(blank=False)
    avarege_to_prise = models.IntegerField(blank=False)
    avarege_battery_prise = models.IntegerField(blank=False)
    avarege_tires_prise = models.IntegerField(blank=False)
    avarege_maintenance_prise = models.DecimalField(max_digits=3, decimal_places=2, blank=False)
    amortization_period = models.IntegerField(blank=False)
    image = models.ImageField(upload_to='uploads')
    submodel_description = models.CharField(max_length=100, blank=False)