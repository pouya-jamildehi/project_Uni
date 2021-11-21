from django import forms
from django.contrib.auth.models import User
from django.core import validators


class Login_User_Form(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(attrs={'placeholder':'نام کاربری خودرا وارد کنید'}),
        label = 'نام کاربری'
                               )
    password = forms.CharField(
        widget = forms.PasswordInput(attrs={'placeholder':'رمزعبور خودرا وارد کنید'}),
        label = 'رمزعبور'
                                )
    # def clean_username(self):
    #     username = self.cleaned_data.get('useranme')
    #     is_exists_username = User.objects.filter(username=username).exists()
    #     if is_exists_username :
    #         raise forms.ValidationError('نام کاربری یا رمزعبور اشتباه است')
    #     return username

class Register_User_Form(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام کاربری خودرا وارد کنید'}),
        label = 'نام کاربری'
    )
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'placeholder': 'ایمیل خودرا وارد کنید'}),
        label = 'ایمیل'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'رمزعبور خودرا وارد کنید'}),
        label = 'رمزعبور'
    )
    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'تکراررمزعبور خودرا وارد کنید'}),
        label = 'تکراررمزعبور'
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        is_exists_username = User.objects.filter(username=username).exists()
        if is_exists_username:
            raise forms.ValidationError('این کاربر قبلا ثبت نام کرده است')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exists_email = User.objects.filter(email=email).exists()
        if is_exists_email:
            raise forms.ValidationError('این ایمیل قبلا ثبت شده است')
        return email

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password != re_password:
            raise forms.ValidationError('رمز عبور با تکرار آن مغایرت ارد')
        return re_password