from rest_framework import serializers

from pytils.translit import slugify

from .models import Category, News


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(allow_null=True, required=False)

    class Meta:
        model = Category
        fields = ['pk', 'title', 'slug']

    def create(self, validated_data):
        validated_data['slug'] = slugify(validated_data['title'])
        return Category.objects.create(**validated_data)


class NewsSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField()

    class Meta:
        model = News
        fields = ['pk', 'title', 'category_id', 'text', 'created', 'updated', 'is_published']
        depth = 1

    def create(self, validated_data):
        return News.objects.create(**validated_data)
