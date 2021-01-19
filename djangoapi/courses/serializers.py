from rest_framework import serializers
from.models import Course

class CourseSerializer(serializers.ModelSerializers):
    class Meta:
      model = Course
      fields = ('id', 'name', 'language', 'price')