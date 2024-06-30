from django.db import models
from apps.accounts.models import User

class AIdiagnosis(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    symptoms = models.JSONField()
    diagnosis = models.TextField()
    treatment_plan = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    stock_quantity = models.IntegerField()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class HealthMetric(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    metric_name = models.CharField(max_length=100)
    metric_value = models.DecimalField(max_digits=10, decimal_places=2)
    recorded_at = models.DateTimeField(auto_now_add=True)

class ProductUsageLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    usage_date = models.DateField()
    notes = models.TextField(blank=True)