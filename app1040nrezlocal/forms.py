from django import forms
from django.forms import ModelForm, RadioSelect, CheckboxInput
from app1040nrezlocal.models import modelInput

class TaxModelForm(forms.ModelForm):

    # override fields from ModelInput for custom behaviour
    # select one - radio buttons
    Q01 = forms.CharField(required=False, widget=RadioSelect(choices=modelInput.CHOICES_Q01), label="Please select tax year: ")
    Q01_01 = forms.CharField(required=False, widget=RadioSelect(choices=modelInput.CHOICES_Q01_01), label="Please select a prior tax year: ")
    Q02 = forms.CharField(required=False, widget=RadioSelect(choices=modelInput.CHOICES_Q02), label="Please select your service need:")
    Q02_01 = forms.CharField(required=False, widget=RadioSelect(choices=modelInput.CHOICES_Q02_01), label="Please select your country of origin: ")
    Q03 = forms.CharField(required=False, widget=RadioSelect(choices=modelInput.CHOICES_Q03), label="Please select your forms:")
    Q03_01 = forms.CharField(required=False, widget=RadioSelect(choices=modelInput.CHOICES_Q03_01), label="What do you want to file as?")

    class Meta:
        # associate with ModelInput for automatically generated fields
        model = modelInput
        # order of fields
        fields = (
            'A01', 
            'A02',
            'Q01',
            'Q01_01',
            'Q02',
            'Q02_01',
            'Q02_01_01',
            'Q03',
            'Q03_01',
            'Q03_01_01',
            'Q03_01_02',
            #W2
            'Q04_a',
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
            'Q04_01_BOX20',
            #1099
            'Q04_b',)
