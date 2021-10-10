from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('CompanyName','Difficulty','department','ctc','Experience')
        widgets={
            'CompanyName':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter compant Name'}),
            'Difficulty':forms.Select(attrs={'class':'form-control','placeholder':'Chose the difficulty'}),
            'department':forms.Select(attrs={'class':'form-control','placeholder':'Chose Department'}),
            'ctc':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Salary'}),
            'Experience':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter the experience'}),

        }