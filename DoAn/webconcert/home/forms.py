from django import forms
import re
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
User = get_user_model()
class RegistrationForm(forms.Form):
    username = forms.CharField(label='Tài khoản', max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput())
    #widget=forms.PasswordInput(): giấu mk bằng dấu *.
    password2 = forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput())

    #hàm ktra pas1=pas2
    def clean_password2(self):
        if 'password1'in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError("Mật khẩu không hợp lệ")
    # hàm ktra username
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username): #neu ton tai 1 ky tu trong username thi tra ve:
            raise forms.ValidationError("Tên tài khoản có ký tự đặc biệt")
        #ktra xem username co ton tai hay chua
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Tài khoản đã tồn tại")
    #ham tao ra username
    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password1'])
