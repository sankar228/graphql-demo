from django.db import models

# Create your models here.
class EnbOM(models.Model):
    enb  = models.IntegerField(primary_key=True) 
    key  = models.CharField(max_length=500, null=False)
    om10 = models.DecimalField(blank=True, decimal_places=50, max_digits=1000)
    om11 = models.DecimalField(blank=True, decimal_places=50, max_digits=1000)
    om12 = models.DecimalField(blank=True, decimal_places=50, max_digits=1000)
    
class CellOM(models.Model):
    cellid = models.IntegerField(primary_key=True) 
    key = models.CharField(max_length=500, null=False)
    om1 = models.DecimalField(blank=True, decimal_places=50, max_digits=1000)
    om2 = models.DecimalField(blank=True, decimal_places=50, max_digits=1000)
    om3 = models.DecimalField(blank=True, decimal_places=50, max_digits=1000)    
    om4 = models.DecimalField(blank=True, decimal_places=50, max_digits=1000)
    om5 = models.DecimalField(blank=True, decimal_places=50, max_digits=1000)
    
    enb = models.ForeignKey(EnbOM, on_delete=models.CASCADE)