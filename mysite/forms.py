from django import forms
from django.contrib.auth import get_user_model
from mysite.models.profile_models import Profile


class UserCreationForm(forms.ModelForm):
    password = forms.CharField()

    class Meta:
        model = get_user_model()
        fields = ('email',)

    def clean_password(self):
        password = self.cleaned_data.get("password")
        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'username',
            'zipcode',
            'prefecture',
            'city',
            'address',
            'image',
        )
