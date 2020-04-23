from django.contrib import admin
from django.urls import path

from landingPage.views import landingPage, additionalInfo
from Account.views import signUp, signIn, signOut

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',landingPage, name='landingPage'),
    path('additionalInfo/',additionalInfo,name='additionalInfo'),
    path('signUp/', signUp, name='signUp'),
    path('signIn/',signIn,name='signIn'),
    path('signOut/',signOut,name='signOut')
]
