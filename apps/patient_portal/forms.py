from django import forms
from .models import HealthMetric, ProductUsageLog

class HealthMetricForm(forms.ModelForm):
    class Meta:
        model = HealthMetric
        fields = ['metric_name', 'metric_value']

class ProductUsageLogForm(forms.ModelForm):
    class Meta:
        model = ProductUsageLog
        fields = ['product', 'usage_date', 'notes']
        widgets = {
            'usage_date': forms.DateInput(attrs={'type': 'date'}),
        }