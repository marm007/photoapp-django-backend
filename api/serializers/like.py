from rest_framework import serializers

from api.models import Like, UserMeta, User, Post


class UserMetaSerializer(serializers.ModelSerializer):
    avatar_thumbnail = serializers.ImageField(read_only=True)

    class Meta:
        model = UserMeta
        fields = ('avatar', 'avatar_thumbnail')


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id',)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id',)


class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer

    class Meta:
        model = Like
        fields = ('user', )


