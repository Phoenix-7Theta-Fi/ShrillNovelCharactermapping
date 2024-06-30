from django.contrib import admin
from .models import AIdiagnosis, Product, Order, OrderItem, HealthMetric, ProductUsageLog

admin.site.register(AIdiagnosis)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(HealthMetric)
admin.site.register(ProductUsageLog)