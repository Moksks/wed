from django import forms
from .models import *

class FittingForm(forms.ModelForm):

    class Meta:
        model = Fitting_order
        exclude =[""]