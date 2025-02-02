from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.brand


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_bland')
    factory_year = models.IntegerField()
    model_year = models.IntegerField()
    plate = models.CharField(max_length=150, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='car/')
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.model


class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.cars_count} {self.cars_value}'
