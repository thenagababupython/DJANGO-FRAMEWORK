from django import forms

class FeedbackForm(forms.Form):
    name=forms.CharField(
        label="Enter your Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your name'
            }
        )
    )
    rating=forms.IntegerField(
        label="Enter your rating",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your rating'
            }
        )
    )
    feedback=forms.CharField(
        label="Enter your feedback",
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Your feedback'
            }
        )
    )