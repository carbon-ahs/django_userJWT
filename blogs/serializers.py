from rest_framework import serializers

from blogs.models import Blogger


class BloggerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogger
        fields = [
            "id",
            "user_id",
            "phone",
        ]
