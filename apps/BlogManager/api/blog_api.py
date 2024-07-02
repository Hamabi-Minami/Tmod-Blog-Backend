from rest_framework import generics
from rest_framework import serializers
from rest_framework.response import Response
import django_filters
from django_filters.rest_framework import FilterSet
from apps.BlogManager.models.atrticle import ArticleModel, FeaturesModel
from apps.BlogManager.models.features import FeatureTypesModel
from apps.UserManager.models.user import UserModel


class BlogFilter(FilterSet):

    topic = django_filters.CharFilter(field_name='topic', lookup_expr='icontains')
    rates = django_filters.CharFilter(field_name='rates', lookup_expr='icontains')
    introduction = django_filters.CharFilter(field_name='introduction', lookup_expr='icontains')
    author = django_filters.CharFilter(field_name='author', lookup_expr='exact')
    created = django_filters.DateFilter(field_name='created', lookup_expr='icontains')

    class Meta:
        model = ArticleModel
        fields = {
            'topic': ['icontains'],
            'rates': ['icontains'],
            'introduction': ['icontains'],
            'author': ['exact'],
            'created': ['icontains']
        }


class BlogSerializer(serializers.ModelSerializer):
    pk = serializers.PrimaryKeyRelatedField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.all(), write_only=True)
    author_name = serializers.SerializerMethodField()

    def get_author_name(self, obj):
        return obj.author.name

    class Meta:
        model = ArticleModel
        fields = [
            'pk',
            'topic',
            'rates',
            'introduction',
            'created',
            'author_name',
            'author',
        ]


class BlogListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = BlogSerializer
    filterset_class = BlogFilter

    filter_fields = [
        'topic',
        'rates',
        'introduction',
        'created',
        'author'
    ]

    queryset = ArticleModel.objects.all()


class BlogRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = BlogSerializer

    queryset = ArticleModel.objects.all()

    lookup_url_kwarg = 'article_id'


class FeaturesSerializer(serializers.ModelSerializer):
    pk = serializers.PrimaryKeyRelatedField(read_only=True)
    feature_type_name = serializers.SerializerMethodField()

    def get_feature_type_name(self, obj):
        return obj.feature_type.name

    class Meta:
        model = FeaturesModel
        many = True

        fields = [
            'pk',
            'feature_type_name',
            'content',
            'index'
        ]


class FeaturesListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = FeaturesSerializer

    queryset = FeaturesModel.objects.all()


class FeatureRetrieveUpdateAPIView(generics.ListAPIView):
    serializer_class = FeaturesSerializer
    queryset = FeaturesModel.objects.all()
    lookup_url_kwarg = 'article_id'

    def get_queryset(self):
        article_id = self.kwargs['article_id']
        queryset = FeaturesModel.objects.filter(article_id=article_id)

        return queryset

"""
pagination
comment
"""