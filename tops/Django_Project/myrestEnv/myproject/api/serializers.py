from rest_framework import serializers
class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    email=serializers.EmailField(max_length=100)
    city=serializers.CharField(max_length=30)

