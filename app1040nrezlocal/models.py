from django.db import models

# Create your models here.
class model1040NREZ(models.Model):
    refnum = models.IntegerField("Reference Number", default=0)
    INFOL01 = models.CharField("Your first name and initial", max_length=128)
    INFOL02 = models.CharField("Last name", max_length=128)
    F1040NREZL03 = models.IntegerField("Wages, salaries, tips, etc. Attach Form(s) W-2", default=0)
    F1040NREZL04 = models.IntegerField("Taxable refunds, credits, or offsets of state and local income taxes", default=0)
    F1040NREZL05 = models.IntegerField("Scholarship and fellowship grants. Attach Form(s) 1042-S or required statement", default=0)
    F1040NREZL06 = models.IntegerField("Total income exempt by a treaty from page 2, Item J(1)(e)", default=0)
    F1040NREZL07 = models.IntegerField("Add lines 3, 4, and 5", default=0)

    def __unicode__(self):
        return self.INFOL01 + " " + self.INFOL02
        
class modelInput(models.Model):
   
    # text input
    A01 = models.CharField("First Name", max_length=128, blank=True, null = True)
    A02 = models.CharField("Last Name", max_length=128, blank=True, null = True)
    
    # choose one
    CHOICES_Q01 = (("a", "Current Year"), ("b", "Prior Year(s)"),)
    Q01 = models.CharField("Please select tax year", max_length=128, choices = CHOICES_Q01, blank=True, null = True)
    
    # choose one
    CHOICES_Q01_01 = (("a", "2010"), ("b", "2011"), ("c", "2012"),)
    Q01_01 = models.CharField("Please select a prior tax year", max_length=128, choices = CHOICES_Q01_01, blank=True, null = True)
    
    # choose one
    CHOICES_Q02 = (("a", "Nonresident Tax Return"), ("b", "Social Security & Medicare Tax Refunds"),)
    Q02 = models.CharField("Please select your service need:", max_length=128, choices = CHOICES_Q02, blank=True, null = True)
	
    # choose one
    CHOICES_Q02_01 = (("a", "China"), ("b", "Mexico"),)
    Q02_01 = models.CharField("Please select your country of origin: ", max_length=128, choices = CHOICES_Q02_01, blank=True, null = True)
	
    # read-only
    Q02_01_01 = models.IntegerField("Tax Treaty Amount:", max_length=128, blank=True, null = True)
	
    # choose one
    CHOICES_Q03 = (("a", "1040NR-EZ"), ("b", "1040NR"),)
    Q03 = models.CharField("Please select your forms:", max_length=128, choices = CHOICES_Q03, blank=True, null = True)
	
    # choose one
    CHOICES_Q03_01 = (("a", "Single"), ("b", "Married"),)
    Q03_01 = models.CharField("What do you want to file as?", max_length=128, choices = CHOICES_Q03_01, blank=True, null = True)
    
    # read-only
    Q03_01_01 = models.IntegerField("Personal Exemption:", max_length=128, blank=True, null = True)
    
    # read-only
    Q03_01_02 = models.IntegerField("Standard Deviation:", max_length=128, blank=True, null = True)

    # choose many
    Q04 = models.CharField("Please select source of income:", max_length=128, blank=True, null = True)
    Q04_a = models.BooleanField("W2 - check to expand", max_length=128, default=True)
    Q04_b = models.BooleanField("1099G - check to expand", max_length=128, default=False)

    Q04_01_BOX1 = models.IntegerField("Box 1: Wages, tips, other comp.", blank=True, null = True)
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
        
        