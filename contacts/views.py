from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Contact
from .serializers import ContactSerializer

# Create your views here.

class ContactDisplayView(ListCreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ContactEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)



    