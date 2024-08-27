# from django import forms
# from .models import *

# # class Ragistration(forms.Form):
# #     fname=forms.CharField(max_length=50,label="first name")
# #     lname=forms.CharField(max_length=20,label="last name")
# #     email=forms.EmailField(label="email")
# #     contact=forms.IntegerField(label="contact")

# class  RegistrationForm(forms.ModelForm):
#     class Meta:
#         model=Registration
#         fields='__all__'

# class LoginForm(forms.ModelForm):
#     class Meta:
#         model=Registration
#         fields=('email','contact')



from django import forms
from .models import *

class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(
        max_length=100, 
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirm Password"
    )
    class Meta:
        model = StudentModel
        fields = ('stu_name', 'stu_email', 'stu_city', 'stu_mobile', 'stu_password')
        widgets = {
            'stu_name': forms.TextInput(attrs={'class': 'form-control'}),
            'stu_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'stu_city': forms.TextInput(attrs={'class': 'form-control'}),
            'stu_mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'stu_password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }



class LoginForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = ('stu_email','stu_password')
        widgets = {
            'stu_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'stu_password':forms.PasswordInput(attrs={'class': 'form-control'}),
        }
