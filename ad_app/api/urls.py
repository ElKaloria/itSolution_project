from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = "ad_app"

router = DefaultRouter()
router.register('ads', views.AdViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
