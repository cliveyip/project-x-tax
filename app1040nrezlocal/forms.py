from django import forms
from app1040nrezlocal.models import TaxForm

class TaxModelForm(forms.ModelForm):
    CHOICES_Q01 = (("a", "First Year Tax"), ("b", "Prior Year Tax"),)
    Q01 = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), label="Please select tax year", choices = CHOICES_Q01)
    
    CHOICES_Q01_01 = (("a", "2010"), ("b", "2011"), ("c", "2012"),)
    Q01_01 = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), label="Please select a prior tax year", choices = CHOICES_Q01_01)
    
    CHOICES_Q02 = (("a", "Nonresident Tax Return"), ("b", "Social Security & Medicare Tax Refunds"),)
    Q02 = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), label="Please select your service need:", choices = CHOICES_Q02)
	
    CHOICES_Q02_01 = (("a", "China"), ("b", "Mexico"),)
    Q02_01 = forms.MultipleChoiceField(widget=forms.RadioSelect(), label="Please select your country of origin: ", choices = CHOICES_Q02_01)
	
    Q02_01_01 = forms.IntegerField(widget=forms.NumberInput(attrs={'readonly':'readonly'}), label="Tax Treaty Amount:")
	
    CHOICES_Q03 = (("a", "1040NR-EZ"), ("b", "1040NR"),)
    Q03 = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), label="Please select your forms:", choices = CHOICES_Q03)
	
    CHOICES_Q03_01 = (("a", "Single"), ("b", "Married"),)
    Q03_01 = forms.MultipleChoiceField(widget=forms.RadioSelect(), label="What do you want to file as?", choices = CHOICES_Q03_01)
    
    Q03_01_01 = forms.IntegerField(widget=forms.NumberInput(attrs={'readonly':'readonly'}), label="Personal Exemption:")
    
    Q03_01_02 = forms.IntegerField(widget=forms.NumberInput(attrs={'readonly':'readonly'}), label="Standard Deviation:")

    CHOICES_Q04 = (("a", "W2"), ("b", "1099G"),)
    Q04 = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), label="Please select source of income:", choices = CHOICES_Q04)
    Q04_01_BOX1 = forms.IntegerField(label="Box 1: Wages, tips, other comp.")
    Q04_01_BOX2 = forms.IntegerField(label="Box 2: Federal income tax withheld")
    Q04_01_BOX3 = forms.IntegerField(label="Box 3: Social security wages")
    Q04_01_BOX4 = forms.IntegerField(label="Box 4: Social security tax withheld")
    Q04_01_BOX5 = forms.IntegerField(label="Box 5: Medicare wages and tips")
    Q04_01_BOX6 = forms.IntegerField(label="Box 6: Medicare tax withheld")
    Q04_01_BOX12a = forms.IntegerField(label="Box 12a: Enter code and amount")
    Q04_01_BOX12b = forms.IntegerField(label="Box 12b: Enter code and amount")
    Q04_01_BOX13 = forms.IntegerField(label="Box 13: Check boxes:")
    Q04_01_BOX15 = forms.IntegerField(label="Box 15: State")
    Q04_01_BOX16 = forms.IntegerField(label="Box 16: State wages, tips, etc.")
    Q04_01_BOX17 = forms.IntegerField(label="Box 17: State income tax")
    Q04_01_BOX18 = forms.IntegerField(label="Box 18: Local wages, tips, etc.")
    Q04_01_BOX19 = forms.IntegerField(label="Box 19: Local income tax")
    Q04_01_BOX20 = forms.IntegerField(label="Box 20: Locality name")

    A01 = forms.CharField(max_length=128, label="Your first name and initial")
    A02 = forms.CharField(max_length=128, label="Last name")
    L03 = forms.IntegerField(label="Wages, salaries, tips, etc [Form(s) W-2]")
    L04 = forms.IntegerField(label="Taxable refunds, credits, or offsets of state and local income taxes")
    L05 = forms.IntegerField(label="Scholarship and fellowship grants [Form(s) 1042-S]")
    L06 = forms.IntegerField(label="Total income exempt by a treaty from Page 2, Item J(1)(e)", widget=forms.HiddenInput())	
    L07 = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    L08 = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    L09 = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    L10 = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    L11 = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    L12 = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    L14 = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    L15 = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    L17 = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    L18a = forms.IntegerField(label="Federal income tax withheld from Forms W-2 and 1099-R")	
    L21 = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    L22 = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    L23a = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    L24 = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    L25 = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    L26 = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

	# An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = TaxForm
        fields = ('A01', 'A02', 'L03', 'L04', 'L05', 'L06', 'L18a')