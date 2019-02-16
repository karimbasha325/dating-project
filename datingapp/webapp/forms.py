from django import forms
from webapp.models import Booktickets
from django.contrib.auth.models import User

class FormModel(forms.ModelForm):
    class Meta:
        model=Booktickets
        fields='__all__'

    date = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y',),
        input_formats=('%d/%m/%Y',)
        )

class SignupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']
        widgets={'password':forms.PasswordInput(),}

        def __str__(self):
            return self.username

        def get_absolute_url(self):
            return reverse('detail',kwargs={'pk':self.pk})

class EmailForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(required=False,widget=forms.Textarea)
