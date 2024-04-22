from rest_framework import serializers
from django.contrib.auth.models import User

from post.models import Post

"""
class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    content = serializers.CharField(max_length=240)
"""


class PostUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'date_joined'
        ]

class PostSerializer(serializers.ModelSerializer):
    #user_username = serializers.SerializerMethodField()
    user = PostUserSerializer()
    url = serializers.HyperlinkedIdentityField(
        view_name='post:detail',
        lookup_field='slug'
    )
    username = serializers.SerializerMethodField(method_name='get_user_username')

    class Meta:
        model = Post
        fields = [
            'id',
            'username',
            'title',
            'image',
            'url',
            'content',
            'user',
            'draft',
            'created_date',
            'modified_date',
            'modified_by',
            #TODO: username in yerini değiştirince serializer hata veriyor, neden?
        ]
        depth = 2

    def get_user_username(self, obj):
        # get_user_username fonksiyonu, kullanıcının username'ini döndürecektir.
        return obj.user.username

class PostUpdateCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
        ]

    def validate(self, value):
        if value == "Bomb":
            raise serializers.ValidationError("Title için geçersiz bir değer.")
        return value





