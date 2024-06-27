# forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    def __init__(self, *args, **kwargs):
            super(RegisterForm, self).__init__(*args, **kwargs)
            # 自定义初始化代码，比如设置placeholder
            self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
            self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
            self.fields['password1'].widget.attrs.update({'placeholder': 'Password'})
            self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm Password'})


# forms.py
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    # 如果需要自定义，可以在这里添加
    pass


# forms.py
# class EmailForm(forms.Form):
#     email = forms.EmailField(label='Your Email Address', required=True)

from .models import Remark
class RemarkForm(forms.ModelForm):
    class Meta:
        model = Remark
        fields = ["title","content"]
    def __init__(self, *args, **kwargs):
            super(RemarkForm, self).__init__(*args, **kwargs)
            # 自定义初始化代码，比如设置placeholder
            self.fields['title'].widget.attrs.update({'placeholder': '标题'})
            self.fields['content'].widget.attrs.update({'placeholder': '内容'})


class RemarkForm_(forms.ModelForm):
     class Meta:
          model=Remark
          fields=["title","content"]