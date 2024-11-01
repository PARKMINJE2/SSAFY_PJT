from .models import Actor, Movie, Review
from rest_framework import serializers

class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name',)

class ActorDetailSerializer(serializers.ModelSerializer):

    class MovieListDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)

    movies = MovieListDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'overview',)

class MovieDetailSerializer(serializers.ModelSerializer):

    class ReviewListDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('title', 'content',)

    class ActorListDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('name',)

    actors = ActorListDetailSerializer(many=True)
    review_set = ReviewListDetailSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'content',)

class ReviewDetailSerializer(serializers.ModelSerializer):
    
    class MovieListDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)

    movie = MovieListDetailSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'