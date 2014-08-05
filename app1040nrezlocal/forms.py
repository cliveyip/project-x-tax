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
                HTML("<p>4. Please select source(s) of income: </p>"),
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
        label = "A U.S. citizen?",
        choices = ((1, "Yes"), (0, "No")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '0',
        required = True,
    )
    
    SCHOILD2 = forms.TypedChoiceField(
        label = "A green card holder (lawful permanent resident) of the United States?",
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
    
    F8843TeachersL08 = forms.TypedChoiceField(
        label = "8. Were you present in the United States as a teacher, trainee, or student for any part of 2 of the 6 prior calendar years (2007 through 2012)?",
        choices = ((1, "Yes"), (0, "No")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '0',
        required = True,
    )
    
    F8843StudentsL12 = forms.TypedChoiceField(
        label = "12. Were you present in the United States as a teacher, trainee, or student for any part of more than 5 calendar years?",
        choices = ((1, "Yes"), (0, "No")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '0',
        required = True,
    )
    
    F8843StudentsL13 = forms.TypedChoiceField(
        label = "13. During 2013, did you apply for, or take other affirmative steps to apply for, lawful permanent resident status",
        choices = ((1, "Yes"), (0, "No")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '0',
        required = True,
    )
    
    F8843AthletesL16a = forms.TypedChoiceField(
        label = "Agreed",
        choices = ((1, "Yes"), (0, "No")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '0',
        required = True,
    )
    
    INFOL09 = forms.TypedChoiceField(
        label = "Select appropriate:",
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
                HTML("<p>D. Were you ever:</p>"),
                'SCHOILD1',
                'SCHOILD2',
                'SCHOILE',
                'SCHOILF',
                'SCHOILFc',
                HTML("<p>G. List all dates you entered and left the United States during 2013 (see instructions).</p>"),                
                HTML("Note. If you are a resident of Canada or Mexico AND commute to work in the United States at frequent intervals,</br>"),                
                HTML("check the box for Canada or Mexico and skip to item H</br>"),                
                'SCHOILGa',
                'SCHOILGb',
                'SCHOILGc',
                'SCHOILGd',
                HTML("<p>H. Give number of days (including vacation, nonworkdays, and partial days) you were present in the United States during:</p>"),
                'SCHOILHa',
                'SCHOILHb',
                'SCHOILHc',
                'SCHOILI',
                'SCHOILIc',
                HTML("J. Income Exempt from Tax-If you are claiming exemption from income tax under a U.S. income tax treaty with a foreign country,</br>"),
                HTML("complete (1) and (2) below. See Pub. 901 for more information on tax treaties.</br>"),
                HTML("</br>"),
            ),
            Fieldset(
                'F8843 questions',
                Fieldset(
                'F8843 Part I: General Information',
                'F8843L01A',
                'F8843L01B',
                'F8843L02',
                'F8843L03A',
                'F8843L03B',
                HTML("<p>4a. Enter the number of days in 2013 you claim you can exclude for purposes of the substantial presence test</p>"),
                'F8843L04Aa',
                'F8843L04Ab',
                'F8843L04Ac',
                'F8843L04B',
                ),
                Fieldset(
                'Please check all that applies to you:',
                'F8843Teachers',
                'F8843Students',                
                'F8843Athletes',
                'F8843Medical',
                ),
                Fieldset(
                'Part II - Teachers and Trainees',
                HTML("<div id='F8843Teachers_fieldset_div'></div>"),
                'F8843TeachersL05',
                'F8843TeachersL06',
                HTML("<p>7. Enter the type of U.S. visa (J or Q) you held during:</p>"),
                'F8843TeachersL07a',
                'F8843TeachersL07b',
                'F8843TeachersL07c',
                'F8843TeachersL07d',
                'F8843TeachersL07e',
                'F8843TeachersL07f',
                HTML("<p>If the type of visa you held during any of these years changed, attach a statement showing the new visa type and the date it was acquired.</p>"),
                'F8843TeachersL08',
                HTML("<p>If you checked the 'Yes' box on line 8, you cannot exclude days of presence as a teacher or trainee unless you meet the Exception explained in the instructions.</p>"),
                ),
                Fieldset(
                'Part III - Students',
                HTML("<div id='F8843Students_fieldset_div'></div>"),
                'F8843StudentsL09',
                'F8843StudentsL10',
                HTML("<p>11. Enter the type of U.S. visa (F, J, M, or Q) you held during:</p>"),
                'F8843StudentsL11a',
                'F8843StudentsL11b',
                'F8843StudentsL11c',
                'F8843StudentsL11d',
                'F8843StudentsL11e',
                'F8843StudentsL11f',
                HTML("<p>If the type of visa you held during any of these years changed, attach a statement showing the new visa type and the date it was acquired.</p>"),
                'F8843StudentsL12',
                HTML("<p>If you checked the 'Yes' box on line 12, you must provide sufficient facts on an attached statement to establish that you do not intend to reside permanently in the United States.</p>"),
                'F8843StudentsL13',
                'F8843StudentsL14',
                ),
                Fieldset(
                'Part IV - Professional Athletes',
                HTML("<div id='F8843Athletes_fieldset_div'></div>"),
                'F8843AthletesL15',
                'F8843AthletesL16',
                HTML("<p>16a. Note. You must attach a statement to verify that all of the net proceeds of the sports event(s) were contributed to the charitable organization(s) listed on line 16.</p>"),
                'F8843AthletesL16a',
                ),
                Fieldset(
                'Part V - Individuals With a Medical Condition or Medical Problem',
                HTML("<div id='F8843Medical_fieldset_div'></div>"),
                'F8843MedicalL17A',
                'F8843MedicalL17B',
                'F8843MedicalL17C',
                HTML("<p>18. Physcian's Statement</p>"),
                'F8843MedicalL18a',
                HTML("<p>was unable to leave the United States on the date shown on line 17b because of the medical condition or medical problem was unable to leave the United States on the date shown on line 17b because of the medical condition or medical problem</p>"),
                'F8843MedicalL18b',
                'F8843MedicalL18c',
                ),
            ),
            Fieldset(
                'General Information',
                HTML("<p>1. Please enter your present home address</p>"),
                'INFOL04',
                'INFOL05',
                HTML("<p>2. Please enter your foreign address</p>"),
                'INFOL06',
                'INFOL07',
                'INFOL08',
                HTML("<p>3. Do you want to allow another person to discuss this return with the IRS?</p>"),
                'INFOL09',
                HTML("<p id='label_id_INFO3_1'>3.1 Please enter the person's information:</p>"),
                'INFOL10',
                'INFOL11',
                'INFOL12',                
                HTML("<p>4. What is your occupation in the United States?</p>"),
                'INFOL15',
                HTML("<p>5. If the IRS sent you an Identity Protection PIN, enter it here</p>"),
                'INFOL16',
            ),
        )
    
        
    class Meta:
        model = modelPostTaxInput

