from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import KPI, AssetKPI
from .serializers import KPISerializer, AssetKPISerializer

class KPIListCreateView(generics.ListCreateAPIView):
    queryset = KPI.objects.all()
    serializer_class = KPISerializer

class AssetKPILinkView(generics.CreateAPIView):
    queryset = AssetKPI.objects.all()
    serializer_class = AssetKPISerializer
