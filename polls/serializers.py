from django.contrib.auth.models import User,Group
from rest_framework import serializers
from polls import models
class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ('url','username','email','groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
  """docstring for GroupSerializer"""
  class Meta:
    model = Group
    fields = ('url','name')
class QuestionSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = models.Question
    fields = ('url','question_text','pub_date','was_published_recently')