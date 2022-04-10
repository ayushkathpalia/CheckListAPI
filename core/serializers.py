from dataclasses import fields
from pyexpat import model
from turtle import title
from rest_framework import serializers
from core.models import CheckList,CheckListItem

class CheckListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckList
        fields = '__all__'

class CheckListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckListItem
        fields = '__all__'