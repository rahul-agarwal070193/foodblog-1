from django import forms
from .models import make


class upload_form(forms.ModelForm):
    class Meta:
        model = make
        fields = ('recipe_name', 'author', 'short_description', "thumbnail_image", "Recipe_video",
                  'difficulty', 'preparation_time', 'food_type', 'serve', 'menu', 'ingredients', 'procedure', 'tags')
        widgets = {
            'recipe_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "What's the name of your recipe? Eg: Tomato Soup"}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'hidden', 'type': 'hidden'}),
            'short_description': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Describe your recipe. What's so special about it?"}),
            "thumbnail_image": forms.FileInput(attrs={'class': 'form-control-file'}),
            "Recipe_video": forms.FileInput(attrs={'class': 'form-control-file'}),
            'difficulty': forms.Select(attrs={'class': 'form-control'}),
            'food_type': forms.Select(attrs={'class': 'form-control'}),
            'serve': forms.NumberInput(attrs={'class': 'form-control', "placeholder": "No. Of people serve"}),
            'preparation_time': forms.NumberInput(attrs={'class': 'form-control', "placeholder": "Total time required in Mins"}),
            'menu': forms.Select(attrs={'class': 'form-control'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control', "placeholder": "Eg: 100 gms tomatoes, chopped"}),
            'procedure': forms.Textarea(attrs={'class': 'form-control', "placeholder": " Eg: In a pan, heat oil."}),
            'tags': forms.TextInput(attrs={'data-role': 'tagsinput'})
        }


class update_form(forms.ModelForm):
    class Meta:
        model = make
        fields = ('recipe_name', 'short_description', "thumbnail_image", "Recipe_video",
                  'difficulty', 'preparation_time', 'food_type', 'serve', 'menu', 'ingredients', 'procedure', 'tags')
        widgets = {
            'recipe_name': forms.TextInput(attrs={'class': 'form-control'}),
            'short_description': forms.TextInput(attrs={'class': 'form-control'}),
            'difficulty': forms.Select(attrs={'class': 'form-control'}),
            "thumbnail_image": forms.FileInput(attrs={'class': 'form-control-file'}),
            "Recipe_video": forms.FileInput(attrs={'class': 'form-control-file'}),
            'food_type': forms.Select(attrs={'class': 'form-control'}),
            'serve': forms.NumberInput(attrs={'class': 'form-control'}),
            'preparation_time': forms.NumberInput(attrs={'class': 'form-control'}),
            'menu': forms.Select(attrs={'class': 'form-control'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control'}),
            'procedure': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'data-role': "tagsinput"})
        }
