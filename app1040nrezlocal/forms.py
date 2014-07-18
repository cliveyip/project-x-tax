from django import forms
from app1040nrezlocal.models import modelInput

class TaxModelForm(forms.ModelForm):
    CHOICES_Q01 = (("a", "First Year Tax"), ("b", "Prior Year Tax"),)
    Q01 = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), label="Please select tax year", choices = CHOICES_Q01, required=False)
    
    CHOICES_Q01_01 = (("a", "2010"), ("b", "2011"), ("c", "2012"),)
    Q01_01 = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), label="Please select a prior tax year", choices = CHOICES_Q01_01, required=False)
    
    CHOICES_Q02 = (("a", "Nonresident Tax Return"), ("b", "Social Security & Medicare Tax Refunds"),)
    Q02 = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), label="Please select your service need:", choices = CHOICES_Q02, required=False)
	
    CHOICES_Q02_01 = (("a", "China"), ("b", "Mexico"),)
    Q02_01 = forms.ChoiceField(widget=forms.RadioSelect(), label="Please select your country of origin: ", choices = CHOICES_Q02_01, required=False)
	
    Q02_01_01 = forms.IntegerField(widget=forms.NumberInput(attrs={'readonly':'readonly'}), label="Tax Treaty Amount:", required=False)
	
    CHOICES_Q03 = (("a", "1040NR-EZ"), ("b", "1040NR"),)
    Q03 = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), label="Please select your forms:", choices = CHOICES_Q03, required=False)
	
    CHOICES_Q03_01 = (("a", "Single"), ("b", "Married"),)
    Q03_01 = forms.ChoiceField(widget=forms.RadioSelect(), label="What do you want to file as?", choices = CHOICES_Q03_01, required=False)
    
    Q03_01_01 = forms.IntegerField(widget=forms.NumberInput(attrs={'readonly':'readonly'}), label="Personal Exemption:", required=False)
    
    Q03_01_02 = forms.IntegerField(widget=forms.NumberInput(attrs={'readonly':'readonly'}), label="Standard Deviation:", required=False)

    CHOICES_Q04 = (("a", "W2"), ("b", "1099G"),)
    Q04 = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), label="Please select source of income:", choices = CHOICES_Q04, required=False)
    Q04_01_BOX1 = forms.IntegerField(label="Box 1: Wages, tips, other comp.", required=False)
    Q04_01_BOX2 = forms.IntegerField(label="Box 2: Federal income tax withheld", required=False)
    Q04_01_BOX3 = forms.IntegerField(label="Box 3: Social security wages", required=False)
    Q04_01_BOX4 = forms.IntegerField(label="Box 4: Social security tax withheld", required=False)
    Q04_01_BOX5 = forms.IntegerField(label="Box 5: Medicare wages and tips", required=False)
    Q04_01_BOX6 = forms.IntegerField(label="Box 6: Medicare tax withheld", required=False)
    Q04_01_BOX12a = forms.IntegerField(label="Box 12a: Enter code and amount", required=False)
    Q04_01_BOX12b = forms.IntegerField(label="Box 12b: Enter code and amount", required=False)
    Q04_01_BOX13 = forms.IntegerField(label="Box 13: Check boxes:", required=False)
    Q04_01_BOX15 = forms.IntegerField(label="Box 15: State", required=False)
    Q04_01_BOX16 = forms.IntegerField(label="Box 16: State wages, tips, etc.", required=False)
    Q04_01_BOX17 = forms.IntegerField(label="Box 17: State income tax", required=False)
    Q04_01_BOX18 = forms.IntegerField(label="Box 18: Local wages, tips, etc.", required=False)
    Q04_01_BOX19 = forms.IntegerField(label="Box 19: Local income tax", required=False)
    Q04_01_BOX20 = forms.IntegerField(label="Box 20: Locality name", required=False)

    A01 = forms.CharField(max_length=128, label="Your first name and initial", required=False)
    A02 = forms.CharField(max_length=128, label="Last name", required=False)

	# An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = modelInput
        fields = ('A01', 
        'A02',
        'Q04_01_BOX1',
        'Q04_01_BOX2',
        'Q04_01_BOX3',
        'Q04_01_BOX4',
        'Q04_01_BOX5',
        'Q04_01_BOX6',
        'Q04_01_BOX12a',
        'Q04_01_BOX12b',
        'Q04_01_BOX13',
        'Q04_01_BOX15',
        'Q04_01_BOX16',
        'Q04_01_BOX17',
        'Q04_01_BOX18',
        'Q04_01_BOX19',
        'Q04_01_BOX20',)
