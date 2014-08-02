from django import forms
from django.forms import ModelForm, RadioSelect, CheckboxInput
from app1040nrezlocal.models import modelInput, modelPostTaxInput
from crispy_forms.layout import Layout, Fieldset, Submit, HTML
from crispy_forms.helper import FormHelper

# pretax interview questions
class TaxModelForm(forms.ModelForm):
    
    # radio buttons
    Q01 = forms.ChoiceField(
        label = "1) Please select tax year",
        choices = (('a', "Current Year"),('b', "Prior Year(s)")),
        widget = forms.RadioSelect,
        initial = 'a',
        required = False,
    )   
    Q01_01 = forms.ChoiceField(
        label = "1.1) Please select a prior tax year",
        choices = (("a", "2010"), ("b", "2011"), ("c", "2012")),
        widget = forms.RadioSelect,
        required = False,
    )   
    Q02 = forms.ChoiceField(
        label = "2) Please select your service need:",
        choices = (("a", "Nonresident Tax Return"), ("b", "Social Security & Medicare Tax Refunds")),
        widget = forms.RadioSelect,
        required = False,
    )   
    Q02_01 = forms.ChoiceField(
        label = "2.1) Please select your country of origin:",
        choices = (("a", "China"), ("b", "Mexico")),
        widget = forms.RadioSelect,
        required = False,
    )   
    Q03 = forms.ChoiceField(
        label = "3) Please select your forms:",
        choices = (("a", "1040NR-EZ"), ("b", "1040NR")),
        widget = forms.RadioSelect,
        required = False,
    )   
    Q03_01 = forms.ChoiceField(
        label = "3.1) What do you want to file as?",
        choices = (("a", "Single"), ("b", "Married")),
        widget = forms.RadioSelect,
        required = False,
    )   
    
    def __init__(self, *args, **kwargs):
        super(TaxModelForm, self).__init__(*args, **kwargs)
        # make fields read-only
        self.fields['Q02_01_01'].widget.attrs['readonly'] = True
        self.fields['Q03_01_01'].widget.attrs['readonly'] = True
        self.fields['Q03_01_02'].widget.attrs['readonly'] = True
        # Django crispy form
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_method = 'post'
        self.helper.form_action = '/app/'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-8'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.layout = Layout(
            Fieldset(
                'Pre tax interview questions',
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
                ),
            Fieldset(
                'Income sources',
                HTML("<p><b>4. Please select source(s) of income: </b></p>"),
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
                'F1099GL11A',
                ),
            )
                

    class Meta:
        # associate with ModelInput for automatically generated fields
        model = modelInput


            
class postTaxInputForm(forms.ModelForm):
    
    #Change widget of boolean field from checkbox to RadioSelect
    #TODO: refractor to a function
    SCHOILC = forms.TypedChoiceField(
        label = "C. Have you ever applied to be a green card holder (lawful permanent resident) of the United States?",
        choices = ((1, "Yes"), (0, "No")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '0',
        required = True,
    )
    
    SCHOILD1 = forms.TypedChoiceField(
        label = "1. A U.S. citizen?",
        choices = ((1, "Yes"), (0, "No")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '0',
        required = True,
    )
    
    SCHOILD2 = forms.TypedChoiceField(
        label = "2. A green card holder (lawful permanent resident) of the United States?",
        choices = ((1, "Yes"), (0, "No")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '0',
        required = True,
    )
        
    SCHOILF = forms.TypedChoiceField(
        label = "F. Have you ever changed your visa type (nonimmigrant status) or U.S. immigration status?",
        choices = ((1, "Yes"), (0, "No")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '0',
        required = True,
    )
    
    SCHOILI = forms.TypedChoiceField(
        label = "I. Did you file a U.S. income tax return for any prior year?",
        choices = ((1, "Yes"), (0, "No")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '0',
        required = True,
    )
    
    def __init__(self, *args, **kwargs):
        super(postTaxInputForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_method = 'post'
        self.helper.form_action = '/app/postTax/'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-8'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.layout = Layout(
            Fieldset(
                'Schedule OI questions',
                'SCHOILA',
                'SCHOILB',
                'SCHOILC',
                HTML("<p><b>D. Were you ever:</b></p>"),
                'SCHOILD1',
                'SCHOILD2',
                'SCHOILE',
                'SCHOILF',
                'SCHOILFc',
                HTML("<p><b>G. List all dates you entered and left the United States during 2013 (see instructions).</b></p>"),                
                HTML("<b>Note. If you are a resident of Canada or Mexico AND commute to work in the United States at frequent intervals,</b></br>"),                
                HTML("<b>check the box for Canada or Mexico and skip to item H</b></br>"),                
                'SCHOILGa',
                'SCHOILGb',
                'SCHOILGc',
                'SCHOILGd',
                HTML("<p><b>H. Give number of days (including vacation, nonworkdays, and partial days) you were present in the United States during:</b></p>"),
                'SCHOILHa',
                'SCHOILHb',
                'SCHOILHc',
                'SCHOILI',
                'SCHOILIc',
                HTML("<b>J. Income Exempt from Tax-If you are claiming exemption from income tax under a U.S. income tax treaty with a foreign country,</b></br>"),
                HTML("<b>complete (1) and (2) below. See Pub. 901 for more information on tax treaties.</b></br>"),
                HTML("</br>"),
            ),
            Fieldset(
                'F8843 questions',
                HTML("<b>Part I: General Information</b></br>"),
                'F8843L01A',
                'F8843L01B',
                'F8843L02',
                'F8843L03A',
                'F8843L03B',
                'F8843L04Aa',
                'F8843L04Ab',
                'F8843L04Ac',
                'F8843L04B',
                HTML("<b>Part II: Please check all that applies to you:</b></br>"),
                'F8843Teachers',
                'F8843Students',                
                'F8843Athletes',
                'F8843Medical',
                'F8843TeachersL05',
                'F8843TeachersL06',
                'F8843TeachersL07a',
                'F8843TeachersL07b',
                'F8843TeachersL07c',
                'F8843TeachersL07d',
                'F8843TeachersL07e',
                'F8843TeachersL07f',
                'F8843TeachersL08',
                'F8843StudentsL09',
                'F8843StudentsL10',
                'F8843StudentsL11a',
                'F8843StudentsL11b',
                'F8843StudentsL11c',
                'F8843StudentsL11d',
                'F8843StudentsL11e',
                'F8843StudentsL11f',
                'F8843StudentsL12',
                'F8843StudentsL13',
                'F8843StudentsL14',
                'F8843AthletesL15',
                'F8843AthletesL16',
                'F8843AthletesL16a',
                'F8843AthletesL17A',
                'F8843AthletesL17B',
                'F8843AthletesL17C',
                'F8843MedicalL18a',
                'F8843MedicalL18b',
                'F8843MedicalL18c',
            )
        )
    
        
    class Meta:
        model = modelPostTaxInput

