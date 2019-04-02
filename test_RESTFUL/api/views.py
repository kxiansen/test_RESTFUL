from django.shortcuts import render

# Create your views here.


from rest_framework import viewsets, generics
from .models import Student
from .serializers import StudentSerializers, test01



# class StudentViewSet(viewsets.ModelViewSet):
# 指定结果集并设置排序
# queryset = Student.objects.all().order_by('-pk')
# 指定序列化的类
# serializer_class = StudentSerializers

# class StudentViewSet(generics.ListAPIView):
class StudentViewSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
    queryset = Student.objects.all().order_by('pk')
    # 指定序列化的类
    serializer_class = StudentSerializers


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # 指定结果集并设置排序
    queryset = Student.objects.all().order_by('pk')
    # 指定序列化的类
    serializer_class = test01


