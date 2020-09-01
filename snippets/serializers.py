from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User
from rest_framework import permissions

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        owner = serializers.ReadOnlyField(source='owner.username')
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        permission_classes = [permissions.IsAuthenticatedOrReadOnly] # which will ensure that authenticated requests get read-write access, and unauthenticated requests get read-only access.
        fields = ['id', 'username', 'snippets']