from django import forms

class VaccineForm(forms.Form):
	vaccine = forms.CharField()
    date = forms.DateField