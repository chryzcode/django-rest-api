from django.urls import path, include
from .views import article_list, article_detail, ArticleApiView, GenericApiView, ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename = 'article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    #path('article/', article_list, name='article_list'),
    path('article/', ArticleApiView.as_view(), name='article_list'),
    path('detail/<int:pk>/', article_detail, name='article_detail'),
    path('generic/article/<int:id>/', GenericApiView.as_view(), name='generic_list_view'),
]
