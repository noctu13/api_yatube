from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import PostViewSet, CommentViewSet


router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register(r'posts/(?P<post_id>[0-9]+)/comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('api/v1/', include(router.urls)),
]
