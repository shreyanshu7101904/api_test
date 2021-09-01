from .models import TblUsers
from rest_framework.serializers import ModelSerializer


class TblUserSerializer(ModelSerializer):
    """Model Serializers for user"""
    class Meta:
        model = TblUsers
        exclude = []
