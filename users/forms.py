from django import forms



class UserForm(forms.Form):
    email = forms.EmailField(max_length=100)
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)

    