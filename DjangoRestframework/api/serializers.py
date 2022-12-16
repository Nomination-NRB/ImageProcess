import api.models as models
from rest_framework.serializers import ModelSerializer


class ImageSerializer(ModelSerializer):
    class Meta:
        model = models.Image
        fields = "__all__"