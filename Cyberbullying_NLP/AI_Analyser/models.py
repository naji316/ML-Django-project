from django.db import models

# Create your models here.

class AnalysisRequest(models.Model):
    model_choice = [
        ('lr', 'Logistic Regression'),
        ('svm', 'Support Vector Machine'),
        ('nb', 'Naive Bayes'),
        ('rf', 'Random Forest'),
    ]
    model_type = models.CharField(max_length=200,choices=model_choice)
    input_text = models.CharField(null=True,blank=True)
    file = models.FileField(upload_to="upload/",null=True,blank=True)
    result = models.CharField(max_length=200, null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.model_type} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"