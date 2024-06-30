from rest_framework import serializers
from apps.patient_portal.models import AIdiagnosis, Product, Order
from apps.doctor_portal.models import Appointment

class AIdiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIdiagnosis
        fields = ['id', 'patient', 'symptoms', 'diagnosis', 'treatment_plan', 'created_at']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'stock_quantity']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'total_amount', 'status', 'created_at']

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'patient', 'doctor', 'appointment_date', 'status', 'created_at']