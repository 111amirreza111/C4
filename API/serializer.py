from rest_framework import serializers
from .models import PrototypeToken
from .models import PrototypeRequestDB

class serializer(serializers.ModelSerializer):
    class Meta:
        model = PrototypeToken
        fields = "__all__"


class serializerRequsetDB(serializers.ModelSerializer):
    class Meta:
        model = PrototypeRequestDB
        fields = "__all__"        