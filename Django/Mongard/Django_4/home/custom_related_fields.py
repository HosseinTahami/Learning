'''custom_related_fields'''

from rest_framework import serializers

class UsernameEmailRelationalField(serializers.RelatedField):
    
    def to_representation(self, value):
        return f'{value.username} || {value.email}'