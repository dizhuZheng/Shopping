from django import forms
from .models import Recipe
# from django.forms.extras.widgets import Select

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        exclude = ['rating']
        labels = {
            'name': 'Dish\'s Name',

        }
        widgets = {'ingredients': forms.Textarea(attrs={'cols':50}),
        'directions': forms.Textarea(attrs={'cols': 100})}
        error_messages = {
            'name':{'requried': 'can not be bull', 'invalid':'wrong format', 'max_length':'length has to be less than 5'},
        }
