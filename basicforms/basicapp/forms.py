from django import forms
from django.core import validators

# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError('NAME NEED TO START WITH Z')


class FormName(forms.Form):
    # name = forms.CharField(validators=[check_for_z])
    name = forms.CharField()
    email = forms.EmailField()
    verifyEmail = forms.EmailField(label="Email Field")
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        print('asidj')
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verifyEmail']

        if email != vmail:
            raise forms.ValidationError('Do not match email')
