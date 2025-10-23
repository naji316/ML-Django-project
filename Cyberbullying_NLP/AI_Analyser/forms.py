from django import forms
from .models import AnalysisRequest

class AnalysisForm(forms.ModelForm):
    class Meta:
        model = AnalysisRequest
        fields = ['model_type', 'input_text', 'file']
        widgets = {
            'model_type':forms.Select(attrs={
                "class":"form-contro"
            }),
            'input_text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your text or comment here...',
                'rows': 4,
            }),
            'file': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }
    
    def clean_input_file(self):
        file = self.cleaned_data.get('file')
        if file and not file.name.endswith('.csv'):
            raise forms.ValidationError("Only CSV files are allowed.")
        return file