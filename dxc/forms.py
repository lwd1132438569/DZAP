from django import forms


class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()

class Form1(forms.Form):
    user = forms.CharField()
    pwd = forms.CharField()

class Dxc_input(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    weight = forms.IntegerField()