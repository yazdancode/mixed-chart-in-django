from django.urls import path
from dashboard.views import index_view


urlpatterns = [path("index/", index_view, name='index')]