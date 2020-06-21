from django import forms
from .models import ProjectBoard

class NewBoard(forms.ModelForm):
    title = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}))
    description = forms.CharField(max_length=100,widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Description','rows':'5'}))

    class Meta:
        model = ProjectBoard
        fields = ['title','description']