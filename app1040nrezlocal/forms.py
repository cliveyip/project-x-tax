from django import forms
from django.forms import ModelForm, RadioSelect, CheckboxInput
from app1040nrezlocal.models import modelInput, modelPostTaxInput

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
            'W2L01',
            'W2L02',
            'W2L03',
            'W2L04',
            'W2L05',
            'W2L06',
            'W2L12aB',
            'W2L12bB',
            'W2L15aA',
            'W2L15bA',
            'W2L16A',
            'W2L17A',
            'W2L18A',
            'W2L19A',
            'W2L20A',
            'W2L07',
            'W2L08',
            'W2L10',
            'W2L11',
            'W2L14',

            #1099
            'Q04_b',
            'F1099GL01',
            'F1099GL02',
            'F1099GL03',
            'F1099GL04',
            'F1099GL05',
            'F1099GL06',
            'F1099GL07',
            'F1099GL08',
            'F1099GL09',
            'F1099GL10aA',
            'F1099GL10bA',
            'F1099GL11A',)

            
class postTaxInputForm(forms.ModelForm):
    class Meta:
        model = modelPostTaxInput
        