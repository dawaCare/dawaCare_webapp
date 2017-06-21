from django.conf.urls import url
from apps.dashboard import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='patients-dashboard'),
    url(r'^patients$', views.PatientView.as_view(), name='patients-new'),
]
