from django.contrib.auth.models import User
from rest_framework import serializers

from pytils.translit import slugify

from .models import Category, News, Comments


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(allow_null=True, required=False)

    class Meta:
        model = Category
        fields = ['pk', 'title', 'slug']

    def create(self, validated_data):
        validated_data['slug'] = slugify(validated_data['title'])
        return Category.objects.create(**validated_data)


class NewsSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(allow_null=True, required=False)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = News
        fields = ['pk', 'title', 'user', 'category', 'category_id', 'text', 'created', 'updated', 'is_published', 'slug']
        depth = 1

    def create(self, validated_data):
        validated_data['slug'] = slugify(validated_data['title'])
        return News.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.category = validated_data.get('category', instance.category_id)
        instance.text = validated_data.get('text', instance.text)
        instance.updated = validated_data.get('updated', instance.updated)
        instance.is_published = validated_data.get('is_published', instance.is_published)
        instance.slug = slugify(instance.title)
        instance.save()
        return instance


class CommentsSerializer(serializers.ModelSerializer):
    user_pk = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True, source='user')
    news_pk = serializers.PrimaryKeyRelatedField(queryset=News.objects.all(), write_only=True, source='news')

    class Meta:
        model = Comments
        fields = ['pk', 'user', 'user_pk', 'news', 'news_pk', 'text', 'created']
        depth = 1


