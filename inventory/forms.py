from django import forms
from .models import *


class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = ('price','status','issues')

class DesktopForm(forms.ModelForm):
    class Meta:
        model = Desktop
        fields = ('price','status','issues')

class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = ('price','status','issues')