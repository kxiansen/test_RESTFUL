from django.conf.urls import include, url
from rest_framework import routers
from api import views
from django.urls import path

# 定义路由地址
route = routers.DefaultRouter()
# 注册新的路由地址
route.register(r'', views.StudentViewSet)
# route.register(r'test01', views.test01ViewSet)

# 注册上一级的路由地址并添加
urlpatterns = [
    path('', include(route.urls)),
    # path('', views.StudentViewSet.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
]
