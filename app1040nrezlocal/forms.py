from django import forms
from app1040nrezlocal.models import TaxForm

class TaxModelForm(forms.ModelForm):
    A01 = forms.CharField(max_length=128, help_text="Your first name and initial")
    A02 = forms.CharField(max_length=128, help_text="Last name")
    L03 = forms.IntegerField(help_text="Wages, salaries, tips, etc [Form(s) W-2]")
    L04 = forms.IntegerField(help_text="Taxable refunds, credits, or offsets of state and local income taxes")
    L05 = forms.IntegerField(help_text="Scholarship and fellowship grants [Form(s) 1042-S]")
    L06 = forms.IntegerField(help_text="Total income exempt by a treaty from Page 2, Item J(1)(e)")	
    L07 = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    L08 = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    L09 = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    L10 = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    L11 = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    L12 = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    L14 = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    L15 = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    L17 = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    L18a = forms.IntegerField(help_text="Federal income tax withheld from Forms W-2 and 1099-R")	
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