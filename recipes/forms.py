from django.forms import ModelForm
from .models import Dish

class DishForm(ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'owner', 'rating', 'difficulty']

# class EntryForm(ModelForm):
#     class Meta:
#         model = Entry
#         fields = "__all__"
#         exclude = None
#         widgets = {'directions': forms.Textarea(attrs={'cols':80})}
#         error_messages = {
#             'name':{'requried': 'dish name can\'t be null '},
#             'ingredients':{'requried': 'ingredients can\'t be null '},
#             'directions':{'requried': 'directions can\'t be null '},
#         }
