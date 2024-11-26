from django.urls import path
from .views import KPIListCreateView, AssetKPILinkView

urlpatterns = [
    path('kpi/', KPIListCreateView.as_view(), name='kpi-list-create'),
    path('kpi/link/', AssetKPILinkView.as_view(), name='kpi-link'),
]
