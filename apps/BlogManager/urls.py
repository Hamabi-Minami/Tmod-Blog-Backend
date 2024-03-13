from django.urls import path
from apps.BlogManager.api import blog_api

urlpatterns = [
    path('blog/', blog_api.BlogListCreateAPIView.as_view()),
    path('blog/<int:article_id>', blog_api.BlogRetrieveUpdateAPIView.as_view()),
    path('blog/<int:article_id>/features', blog_api.FeatureRetrieveUpdateAPIView.as_view()),
    path('feature/', blog_api.FeaturesListCreateAPIView.as_view()),
]
