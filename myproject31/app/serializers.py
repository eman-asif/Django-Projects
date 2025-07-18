from .models import Singer , Song
from rest_framework import serializers


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
        # fields = ["id", "title", "singer","duration"]


class SingerSerializer(serializers.ModelSerializer):
    sungby = SongSerializer(many= True, read_only = True)
    # song = serializers.StringRelatedField(many= True, read_only = True)
    # song = serializers.PrimaryKeyRelatedField(many= True, read_only = True)
    # song = serializers.SlugRelatedField(slug_field = "title", many= True, read_only = True)
    # song = serializers.HyprerlinkedRelatedField(many= True, read_only = True, view_name = "song-detail")
    class Meta:
        model = Singer
        fields = ["id", "name", "gender", "sungby"]