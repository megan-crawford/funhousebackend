from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import FunhouseSerializer      # add this
from .models import Funhouse                     # add this

class FunhouseView(viewsets.ModelViewSet):       # add this
    serializer_class = FunhouseSerializer          # add this
    queryset = Funhouse.objects.all()


