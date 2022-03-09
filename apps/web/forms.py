from django import forms
from django.contrib.auth import authenticate


class OddNumberForm(forms.Form):
    number = forms.IntegerField()


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=60, label="E-Mail")
    password = forms.CharField(
        min_length=6,
        max_length=50,
        label="Passwort eintragen",
        widget=forms.PasswordInput,
    )

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user = authenticate(email=email, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError(
                "Sorry, that login was invalid. Please try again."
            )
        return self.cleaned_data

    def login(self, request):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user = authenticate(email=email, password=password)
        return user
