from rest_framework import serializers
from students.models import students

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = students
        fields = "__all__"
# This serializer converts the students model into a format that can be easily rendered into JSON or XML.