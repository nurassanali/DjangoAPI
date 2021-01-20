from django.urls import path
from . import views
from rest_framework import routers
from django.urls import include

router = routers.DefaultRouter()
router.register('courses', views.CourseView)

urlpatterns = [
    path('', include(router.urls)),
]
