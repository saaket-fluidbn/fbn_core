from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('tutorial', views.tutorial),
    path('act', views.act),

]
