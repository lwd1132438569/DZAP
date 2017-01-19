from django import forms

class Empi_input(forms.Form):
    name = forms.CharField()
    sex = forms.CharField()
    addr = forms.CharField()

class Empi_input_jb(forms.Form):
    name = forms.CharField()
    sex = forms.CharField()
    addr = forms.CharField()

class Empi_input_f(forms.Form):
    name = forms.CharField()
    sex = forms.CharField()
    addr = forms.CharField()