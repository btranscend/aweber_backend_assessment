from django.contrib.auth.models import User, Group
from rest_framework import serializers
from crud_rest_api.models import Widgets

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        
class WidgetsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Widgets
        fields = ['name', 'number_of_parts', 'created_date', 'updated_date']