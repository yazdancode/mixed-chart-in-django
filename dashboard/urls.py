from django.urls import path
from dashboard.views import index_view, JsonResponseView


urlpatterns = [
    path("index/", index_view, name="index"),
    path('jsondata/', JsonResponseView,  name="JsonResponseView")
    ]
