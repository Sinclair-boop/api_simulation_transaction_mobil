# transactions/serializers.py
from rest_framework import serializers
from .models import Utilisateur, IsFraud


class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = '__all__'

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = '__all__'

class IsFraudSerializer(serializers.ModelSerializer):
    class Meta:
        model = IsFraud
        fields = '__all__'


