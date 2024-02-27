from rest_framework import serializers

from .models import ContactModel


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = ['id', 'first_name', 'last_name', 'surname', 'phone', 'address']
