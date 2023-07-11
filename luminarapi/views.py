from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,CreateModelMixin,UpdateModelMixin
from rest_framework import authentication,permissions

from django.contrib.auth.models import User
from luminarapi.serializers import UserSerializer,CourseSerializers,DemoSerializers,DetailsSerializer,ModulesSerializer,BatchSerializer,OverviewSerializer,AttendanceSerializer,AssignmentSerializer,AnnouncementSerializer,LiveClassSerializer,VideoScreenSerializer
from luminarapi.models import Courses,DemoClass,Details,Modules,Batch,Overview,Attendance,Assignment,Announcement,LiveClass,VideoScreen
from luminarapi.serializers import TestSerializer,JobPortalSerializer,UserProfileSerializer
from luminarapi.models import Test,JobPortal,Userprofile
class UsersView(ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()
    model=User
    http_method_names=["post","get"]
class CoursesListView(GenericViewSet,ListModelMixin,RetrieveModelMixin,CreateModelMixin):
    queryset=Courses.objects.all()
    serializer_class=CourseSerializers
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    http_method_names=["post","get"]
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers)
class DemoClassListView(GenericViewSet,ListModelMixin,RetrieveModelMixin,CreateModelMixin):
    queryset=DemoClass.objects.all()
    serializer_class=DemoSerializers
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    http_method_names=["post","get"]
    
class DetailsListAPIView(GenericViewSet,ListModelMixin,RetrieveModelMixin,CreateModelMixin):
    queryset = Details.objects.all()
    serializer_class = DetailsSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    http_method_names=["post","get"]
class ModulesAPIView(GenericViewSet,ListModelMixin,RetrieveModelMixin,CreateModelMixin):
    queryset = Modules.objects.all()
    serializer_class =ModulesSerializer 
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    http_method_names=["post","get"]
class BatchListView(GenericViewSet,ListModelMixin,RetrieveModelMixin,CreateModelMixin):
    queryset=Batch.objects.all()
    serializer_class=BatchSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    http_method_names=["post","get"]
class OverDetailView(GenericViewSet,CreateModelMixin,ListModelMixin,RetrieveModelMixin):
    queryset=Overview.objects.all()
    serializer_class=OverviewSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    http_method_names=["post","get"]
class AttendanceView(GenericViewSet,CreateModelMixin,ListModelMixin,RetrieveModelMixin):
    queryset=Attendance.objects.all()
    serializer_class=AttendanceSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    http_method_names=["post","get"]
class AssignmentView(GenericViewSet,CreateModelMixin,ListModelMixin,RetrieveModelMixin):
    queryset=Assignment.objects.all()
    serializer_class=AssignmentSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    http_method_names=["post","get"]
class AnnouncementView(GenericViewSet,CreateModelMixin,ListModelMixin):
    queryset=Announcement.objects.all()
    serializer_class=AnnouncementSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    http_method_names=["post","get"]
class LiveClassView(GenericViewSet,CreateModelMixin,ListModelMixin,RetrieveModelMixin):
    queryset=LiveClass.objects.all()
    serializer_class=LiveClassSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    http_method_names=["get","post"]
class VideoScreenView(GenericViewSet,CreateModelMixin,ListModelMixin,RetrieveModelMixin):
    queryset=VideoScreen.objects.all()
    serializer_class=VideoScreenSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    http_method_names=["get","post"]
class TestView(GenericViewSet,CreateModelMixin,ListModelMixin,RetrieveModelMixin):
    queryset=Test.objects.all()
    serializer_class=TestSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    http_method_names=["get","post"]
class JobPortalView(GenericViewSet,CreateModelMixin,ListModelMixin):
    queryset=JobPortal.objects.all()
    serializer_class=JobPortalSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    http_method_names=["post","get"]
class UserProfileView(GenericViewSet, CreateModelMixin, ListModelMixin,UpdateModelMixin):
    queryset = Userprofile.objects.all()
    serializer_class = UserProfileSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["get", "post","put"]

    # def put(self, request, *args, **kwargs):
    #     return self.update(request,*args,**kwargs)
    
        

    



    
    
   

    


