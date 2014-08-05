from django.db import models
from swampdragon.models import SelfPublishModel
from .serializers import FooSerializer


class Foo(SelfPublishModel, models.Model):
    serializer_class = FooSerializer
    text = models.CharField(max_length=100)
