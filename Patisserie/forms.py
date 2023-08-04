from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from .models import Cakes, Cookies, HealthyCookies


class CakesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CakesForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Cakes
        fields = ['title', 'price', 'image', ]

class CookiesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CookiesForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Cookies
        fields = ['title', 'price', 'image', ]


class HealthyCookiesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(HealthyCookiesForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = HealthyCookies
        fields = ['title', 'price', 'image', ]



class SignUpForm(UserCreationForm):
        # class Meta:
        #     model = User
        #     fields = ['username', 'email', 'password1', 'password2']
        #     widgets = {
        #         'username': forms.TextInput(attrs={'class': 'form-control'}),
        #         'email': forms.EmailInput(attrs={'class': 'form-control'}),
        #         'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
        #         'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        #     }
        error_messages = {
            'password_mismatch': _('The two password fields didn’t match.'),
        }

        username = forms.CharField(
            label=_("Username"),
            widget=forms.TextInput(attrs={'class': 'form-control'}),
            max_length=150,  # You can adjust the max_length to your desired value
            help_text="",  # Removing the help_text
        )

        password1 = forms.CharField(
            label=_("Password"),
            strip=False,
            widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
        )
        password2 = forms.CharField(
            label=_("Password confirmation"),
            widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
            strip=False,
        )

        class Meta:
            model = User
            fields = ['username', 'email']
            widgets = {
                'email': forms.EmailInput(attrs={'class': 'form-control'}),
            }

        def clean_password2(self):
            password1 = self.cleaned_data.get('password1')
            password2 = self.cleaned_data.get('password2')
            if password1 and password2 and password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
            return password2


class AddCakeForm(forms.ModelForm):
    class Meta:
        model = Cakes
        fields = ['title', 'ingredients', 'price', 'image']

    def __init__(self, *args, **kwargs):
        super(AddCakeForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

class AddCookieForm(forms.ModelForm):
    class Meta:
        model = Cookies
        fields = ['title', 'ingredients', 'price', 'image']

    def __init__(self, *args, **kwargs):
        super(AddCookieForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

class AddHealthyCookieForm(forms.ModelForm):
    class Meta:
        model = HealthyCookies
        fields = ['title', 'ingredients', 'price', 'image']

    def __init__(self, *args, **kwargs):
        super(AddHealthyCookieForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

# INGREDIENTS_CHOICE=[
#     ('white chocolate','Чипс од бело чоколадо, Несолен путер, Шеќер во прав, Екстракт од ванила, Кошер сол '),
#     ('mint smoothie','Бадемово млеко, Чија семе, Јаворов сируп, Екстракт од ванила, Банана, Зелена спирулина во прав, Листови од нане'),
#     ('almond balls','Урми, Бадеми, Кокосово масло, Сурово какао во прав, Јаворов сируп, Чија семе, Цимет, Брашно од бадем'),
# ]
#
# FORM_CHOICE=[
#     ('square', 'Квадрат'),
#     ('circle', 'Округла'),
#     ('rectangle', 'Правоаголна'),
#
# ]
#
# SIZE_CHOICE=[
#     ('small', 'Мала'),
#     ('middle', 'Средна'),
#     ('big', 'Голема'),
#
# ]
#
# class OrderForm(forms.Form):
#     image = forms.ImageField()
#     ingredients = forms.CharField(widget=forms.Select(choices=INGREDIENTS_CHOICE))
#     form = forms.CharField(widget=forms.Select(choices=FORM_CHOICE))
#     size = forms.CharField(widget=forms.Select(choices=SIZE_CHOICE))

