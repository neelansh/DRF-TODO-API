from django.shortcuts import render
from .models import Task
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import CreateAPIView
from .serializer import TaskSerializer, UserSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from django.contrib.auth import get_user_model

# Create your views here.


from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class TaskViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated, ) 
	model = Task;
	serializer_class = TaskSerializer;
	filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter, )
	filter_fields = ('completed', )
	ordering = ('-date_created', )
	search_fields = ('task_name', )

	def get_queryset(self):
		queryset = self.model.objects.all().filter(user = self.request.user);
		return queryset

	def perform_create(self, serializer):
		return serializer.save(user = self.request.user);


# class CreateUserView(CreateAPIView):
# 	model = get_user_model();
# 	permission_classes = (AllowAny, )
# 	serializer_class = UserSerializer
