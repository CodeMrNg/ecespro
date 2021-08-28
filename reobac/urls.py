from django.contrib import admin
from django.urls import path, include
from  reo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,  name='home'),
    path("serie/", views.serie, name="serie"),
    path("result/", views.result, name="result"),
    path("A/", views.serieA, name="serieA"),
    path("D/", views.serieD, name="serieD"),
    path("E/", views.serieE, name="serieE"),
]
