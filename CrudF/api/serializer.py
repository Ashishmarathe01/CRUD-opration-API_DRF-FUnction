from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    email = serializers.EmailField()

    #for creating or adding new data in databse
    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    # for update
    def update(self, instance, validated_data): # instance contain old data
        instance.name=validated_data.get('name',instance.name)# if new data come save /instance.name =save old data
        instance.age = validated_data.get('age', instance.age)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
