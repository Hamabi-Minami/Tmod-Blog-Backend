from rest_framework import generics
from rest_framework import serializers

import django_filters
from django_filters.rest_framework import FilterSet
from apps.UserManager.models.user import UserModel


class UserFilter(FilterSet):

    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    account = django_filters.CharFilter(field_name='account', lookup_expr='exact')
    gender = django_filters.CharFilter(field_name='gender', lookup_expr='exact')
    email = django_filters.CharFilter(field_name='email', lookup_expr='exact')

    class Meta:
        model = UserModel
        fields = {
            'name': ['icontains'],
            'account': ['exact'],
            'gender': ['exact'],
            'email': ['exact']
        }


class UserSerializer(serializers.ModelSerializer):
    pk = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = UserModel

        fields = [
            'pk',
            'name',
            'account',
            'password',
            'email',
            'gender'
        ]


class UserListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    filterset_class = UserFilter

    filter_fields = [
        'name',
        'account',
        'gender',
        'email'
    ]

    queryset = UserModel.objects.all()


class UserRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    lookup_url_kwarg = 'user_id'
