from rest_framework import routers
from django.conf.urls import url, include
from course.models import Course
from course.views import CourseView

routers = routers.DefaultRouter()
routers.register('Course', CourseView)

urlpatterns = [
    url(r'^', include(routers.urls)),

]
