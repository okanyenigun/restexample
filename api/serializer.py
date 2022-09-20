
from rest_framework import serializers
from django.forms import ValidationError
from api.models import Movie




# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=250)
#     duration = serializers.IntegerField()
#     release_date = serializers.DateField()
#     rating = serializers.IntegerField()
    
#     def create(self,data):
#         return Movie.objects.create(**data)

#     def update(self, instance, data):
#         instance.title = data.get("title", instance.title)
#         instance.duration = data.get("duration", instance.duration)
#         instance.release_date = data.get("release_date", instance.release_date)
#         instance.rating = data.get("rating", instance.rating)
#         instance.save()
#         return instance
      
class MovieSerializer(serializers.ModelSerializer):

    description = serializers.SerializerMethodField()
    
    class Meta:
        model = Movie
        fields = "__all__"

    def validate_title(self, val):
        if val == "Dexter":
            raise ValidationError("Cannot accept TV Series.")
        return val

    def validate(self, data):
        if data["duration"] > 600:
            raise ValidationError("Cannot accept movies longer than 10 hours!")
        return data

    def get_description(self, data):
        return f"Movie: {data.title} and Rating: {data.rating}"