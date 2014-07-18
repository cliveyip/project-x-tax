from django.db import models

# Create your models here.
class model1040NREZ(models.Model):
    A01 = models.CharField(max_length=128)
    A02 = models.CharField(max_length=128)
    A03 = models.CharField(max_length=128, blank=True)
    A04 = models.CharField(max_length=128, blank=True)
    A05 = models.CharField(max_length=128, blank=True)
    A06 = models.CharField(max_length=128, blank=True)
    A07 = models.CharField(max_length=128, blank=True)
    A08 = models.CharField(max_length=128, blank=True)
    L03 = models.IntegerField(default=0)
    L04 = models.IntegerField(default=0)
    L05 = models.IntegerField(default=0)
    L06 = models.IntegerField(default=0)
    L07 = models.IntegerField(default=0)
    L08 = models.IntegerField(default=0)
    L09 = models.IntegerField(default=0)
    L10 = models.IntegerField(default=0)
    L11 = models.IntegerField(default=0)
    L12 = models.IntegerField(default=0)
    L13 = models.IntegerField(default=0)
    L14 = models.IntegerField(default=0)
    L15 = models.IntegerField(default=0)
    L16 = models.IntegerField(default=0)
    L17 = models.IntegerField(default=0)
    L18a = models.IntegerField(default=0)
    L18b = models.IntegerField(default=0)
    L19 = models.IntegerField(default=0)
    L20 = models.IntegerField(default=0)
    L21 = models.IntegerField(default=0)
    L22 = models.IntegerField(default=0)
    L23a = models.IntegerField(default=0)
    L24 = models.IntegerField(default=0)
    L25 = models.IntegerField(default=0)
    L26 = models.IntegerField(default=0)

    def __unicode__(self):
        return self.A01 + " " + self.A02
        
class modelInput(models.Model):
    A01 = models.CharField(max_length=128, blank=True, null = True)
    A02 = models.CharField(max_length=128, blank=True, null = True)
    Q04_01_BOX1 = models.IntegerField(blank=True, null = True)
    Q04_01_BOX2 = models.IntegerField(blank=True, null = True)
    Q04_01_BOX3 = models.IntegerField(blank=True, null = True)
    Q04_01_BOX4 = models.IntegerField(blank=True, null = True)
    Q04_01_BOX5 = models.IntegerField(blank=True, null = True)
    Q04_01_BOX6 = models.IntegerField(blank=True, null = True)
    Q04_01_BOX12a = models.IntegerField(blank=True, null = True)
    Q04_01_BOX12b = models.IntegerField(blank=True, null = True)
    Q04_01_BOX13 = models.IntegerField(blank=True, null = True)
    Q04_01_BOX15 = models.IntegerField(blank=True, null = True)
    Q04_01_BOX16 = models.IntegerField(blank=True, null = True)
    Q04_01_BOX17 = models.IntegerField(blank=True, null = True)
    Q04_01_BOX18 = models.IntegerField(blank=True, null = True)
    Q04_01_BOX19 = models.IntegerField(blank=True, null = True)
    Q04_01_BOX20 = models.IntegerField(blank=True, null = True)
		
    def __unicode__(self):
        return self.A01 + " " + self.A02