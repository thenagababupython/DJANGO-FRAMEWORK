from django import forms

class EmpForm(forms.Form):
    name=forms.CharField(
        label='Enter Your Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placehloder':'Enter Name'
            }
        )
    )
    email=forms.EmailField(
        label='Enter Your email',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placehloder':'Enter Email'
            }
        )
    )
    salary=forms.IntegerField(
        label='Enter Your salary',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placehloder':'Enter salary'
            }
        )
    )
    location=forms.CharField(
        label='Enter Your location',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placehloder':'Enter location'
            }
        )
    )
