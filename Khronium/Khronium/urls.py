from django.contrib import admin
from django.urls import path

from landingPage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landingPage, name='landingPage'),
    path('/additionalInfo',views.additionalInfo,name='additionalInfo')
]
