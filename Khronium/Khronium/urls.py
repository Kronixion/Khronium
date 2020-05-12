from django.contrib import admin
from django.urls import path

from landingPage.views import landingPage, additionalInfo, dashboard
from Account.views import signUp, signIn, signOut
from psychologicalManagement.views import psychologicalDashboard, madrs, keds
from projectManagement.views import boards, addBoard, viewBoard, addList, addItem

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
    path('boards/',boards,name='boards'),
    path('/boards/add/',addBoard,name="addBoard"),
    path('boards/<int:id>/',viewBoard,name="viewBoard"),
    path('boards/<int:id>/addList',addList,name="addList"),
    path('boards/<int:id>/addItem',addItem,name="addItem"),

]