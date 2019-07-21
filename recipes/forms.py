from django import forms
from recipes.models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('name', 'img', )
