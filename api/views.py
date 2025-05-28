# from django.shortcuts import render
from students.models import students
from .serializers import StudentsSerializer, EmployesSerializer
from blogs.serializers import BlogSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employes.models import Employe
from django.http import Http404
from rest_framework import generics, mixins, viewsets
from blogs.models import Blog, Comment

# Create your views here.
@api_view(['GET', 'POST'])
def studentsViews(request):
    if request.method == 'GET':
        students_list = students.objects.all()
        serializer = StudentsSerializer(students_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])    
def studentsDetail(request, pk):
    try:
        student = students.objects.get(student_id=pk)
    except students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentsSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = StudentsSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
    

# class Employes(APIView):
#     def get(self, request):
#         employes = Employe.objects.all()
#         serializer = EmployesSerializer(employes, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request):
#         serializer = EmployesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class EmployesDetails(APIView):
#     def get_object(self, pk):
#         try:
#             return Employe.objects.get(emp_id=pk)
#         except Employe.DoesNotExist:
#             raise Http404
    
#     def get(self, request, pk):
#         employe = self.get_object(pk)
#         if employe is None:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = EmployesSerializer(employe)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put(self, request, pk):
#         employe = self.get_object(pk)
#         if employe is None:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = EmployesSerializer(employe, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         employe = self.get_object(pk)
#         if employe is None:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         employe.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class Employes(generics.ListCreateAPIView):
#     queryset = Employe.objects.all()
#     serializer_class = EmployesSerializer

#     def get(self, request):
#         return self.list(request)
    
#     def post(self, request):
#         return self.create(request)
    
# class EmployesDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Employe.objects.all()
#     serializer_class = EmployesSerializer

#     def get(self, request, pk):
#         return self.retrieve(request, pk=pk)
    
#     def put(self, request, pk):
#         return self.update(request, pk=pk)
    
#     def delete(self, request, pk):
#         return self.destroy(request, pk=pk)

# class EmployeViewset(viewsets.ViewSet):
#     def list(self, request):
#         employes = Employe.objects.all()
#         serializer = EmployesSerializer(employes, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def create(self, request):
#         serializer = EmployesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def retrieve(self, request, pk=None):
#         try:
#             employe = Employe.objects.get(emp_id=pk)
#         except Employe.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
#         serializer = EmployesSerializer(employe)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def update(self, request, pk=None):
#         try:
#             employe = Employe.objects.get(emp_id=pk)
#         except Employe.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#         serializer = EmployesSerializer(employe, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk=None):
#         try:
#             employe = Employe.objects.get(emp_id=pk)
#         except Employe.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#         employe.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
class EmployeViewset(viewsets.ModelViewSet):
    queryset = Employe.objects.all()
    serializer_class = EmployesSerializer

    def get_queryset(self):
        return self.queryset
    
    def perform_create(self, serializer):
        serializer.save()
    
    def perform_update(self, serializer):
        serializer.save()
    
    def perform_destroy(self, instance):
        instance.delete()


class BlogViewset(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class CommentViewset(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class BlogDetailViewset(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    # def get(self, request, pk):
    #     return self.retrieve(request, pk=pk)
    
    # def put(self, request, pk):
    #     return self.update(request, pk=pk)
    
    # def delete(self, request, pk):
    #     return self.destroy(request, pk=pk)
    
class CommentDetailViewset(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    # def get(self, request, pk):
    #     return self.retrieve(request, pk=pk)
    
    # def put(self, request, pk):
    #     return self.update(request, pk=pk)
    
    # def delete(self, request, pk):
    #     return self.destroy(request, pk=pk)    