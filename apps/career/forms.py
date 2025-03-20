from django import forms
from .models import Quarter, Level, Career

input_class = 'border border-gray-400 p-1 rounded-xl mt-2'

class QuarterForm(forms.ModelForm):
    class Meta:
        model = Quarter
        fields = ['quarter', 'quarter_name']
        widgets = {
            'quarter': forms.TextInput(attrs={'type':'number','class': input_class}),
            'quarter_name': forms.TextInput(attrs={'class': input_class})
        }
        
class LevelForm(forms.ModelForm):
    class Meta:
        model = Level
        fields = ['name', 'short_name']
        widgets = {
            'name': forms.TextInput(attrs={'class':input_class}),
            'short_name': forms.TextInput(attrs={'class':input_class})
        }
        
class CareerForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = ['name', 'short_name', 'level', 'is_active', 'principal', 'year']
        widgets = {
            'name': forms.TextInput(attrs={'class':input_class}),
            'short_name': forms.TextInput(attrs={'class':input_class}),
            'level': forms.Select(attrs={'class':input_class}),
            'is_active': forms.CheckboxInput(attrs={'class':input_class}),
            'principal': forms.Select(attrs={'class':input_class}),
            'year': forms.TextInput(attrs={'class':input_class})
        }