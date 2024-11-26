from rest_framework import serializers
from .models import KPI, AssetKPI

class KPISerializer(serializers.ModelSerializer):
    class Meta:
        model = KPI
        fields = ['id', 'name', 'expression', 'description']

class AssetKPISerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetKPI
        fields = ['id', 'kpi', 'asset_id']
