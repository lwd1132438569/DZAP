from django import forms


class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()

class Form1(forms.Form):
    user = forms.CharField()
    pwd = forms.CharField()