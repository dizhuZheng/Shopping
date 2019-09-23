from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        widgets = {'text': forms.Textarea(attrs={'cols':80})}
        error_messages = {
            'name':{'requried': 'dish name can\'t be null '},
            'ingredients':{'requried': 'ingredients can\'t be null '},
            'directions':{'requried': 'directions can\'t be null '},
        }
