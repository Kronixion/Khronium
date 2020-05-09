from django.contrib import admin
from django.urls import path

from landingPage.views import landingPage, additionalInfo, dashboard
from Account.views import signUp, signIn, signOut
from psychologicalManagement.views import psychologicalDashboard, madrs, keds

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',landingPage, name='landingPage'),
    path('additionalInfo/',additionalInfo,name='additionalInfo'),
    path('signUp/', signUp, name='signUp'),
    path('signIn/',signIn,name='signIn'),
    path('signOut/',signOut,name='signOut'),
    path('dashboard/',dashboard,name='dashboard'),
    path('psychologicalDashboard/',psychologicalDashboard, name="psychologicalDashboard"),
    path('madrs/',madrs,name='madrs'),
    path('keds/',keds,name='keds'),
]
