from . import views
from django.urls import include, re_path



urlpatterns = [
    re_path(r'^chart/$', views.ChartView.as_view(), name='chart_info'),
    re_path(r'^index/$', views.IndexView.as_view(), name='single_cohort'),
]

