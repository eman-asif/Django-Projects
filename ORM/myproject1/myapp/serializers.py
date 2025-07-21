from rest_framework import serializers
from myapp.models import Book, Author, Profile, Store

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)

    class Meta:
        model = Store
        fields = '__all__'

