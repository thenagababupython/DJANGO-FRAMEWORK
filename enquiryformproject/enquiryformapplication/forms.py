from django import forms
from multiselectfield import MultiSelectFormField

class EnquiryForm(forms.Form):
    name=forms.CharField(
        label="Enter your Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )
    mobile=forms.IntegerField(
        label="Enter your Mobile Number",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Mobile Number'
            }
        )
    )
    email=forms.EmailField(
        label="Enter your Email",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Email'
            }
        )
    )

    SKILLS_CHOICES = (('py', 'Python'),
                      ('dj', 'Django'),
                      ('fl', 'Flask'),
                      ('ri', 'RestApi'))
    skills = MultiSelectFormField(max_length=200, choices=SKILLS_CHOICES)

    LOCATIONS_CHOICES = (('hy', 'HYDERBAD'),
                         ('bg', 'BANGALORE'),
                         ('ch', 'CHENNI'),
                         ('mu', 'MUMBAI'))
    locations = MultiSelectFormField(max_length=200, choices=LOCATIONS_CHOICES)

    GENDER_CHOICES=(('m','Male'),
                    ('f','Female'))
    gender=forms.ChoiceField(
        label="Select Your Gender",
        widget=forms.RadioSelect,choices=GENDER_CHOICES
    )

    y=range(1980,2020)

    date=forms.DateField(
        label="Select Your Date",
        widget=forms.SelectDateWidget(years=y)
    )