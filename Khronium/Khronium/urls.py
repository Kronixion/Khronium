from django.contrib import admin
from django.urls import path

from landingPage.views import landingPage, additionalInfo, dashboard
from Account.views import signUp, signIn, signOut, resetPassword
from psychologicalManagement.views import psychologicalDashboard, madrs, keds
from projectManagement.views import boards, addBoard, updateBoard, deleteBoard, viewBoard, addList, deleteList, addItem, updateItem, deleteItem, moveItem

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',landingPage, name='landingPage'),
    path('additionalInfo/',additionalInfo,name='additionalInfo'),
    path('signUp/', signUp, name='signUp'),
    path('signIn/',signIn,name='signIn'),
    path('signOut/',signOut,name='signOut'),
    path('resetPassword/',resetPassword,name='resetPassword'),
    path('dashboard/',dashboard,name='dashboard'),
    path('psychologicalDashboard/',psychologicalDashboard, name="psychologicalDashboard"),
    path('madrs/',madrs,name='madrs'),
    path('keds/',keds,name='keds'),
    path('boards/',boards,name='boards'),
    path('boards/add/',addBoard,name="addBoard"),
    path('boards/update/',updateBoard,name="updateBoard"),
    path('boards/delete/',deleteBoard,name="deleteBoard"),
    path('boards/<int:id>/',viewBoard,name="viewBoard"),
    path('boards/<int:id>/addList/',addList,name="addList"),
    path('boards/<int:id>/deleteList/',deleteList,name="deleteList"),
    path('boards/<int:id>/addItem/',addItem,name="addItem"),    
    path('boards/<int:id>/updateItem/',updateItem,name="updateItem"),
    path('boards/<int:id>/deleteItem/',deleteItem,name="deleteItem"),
    path('boards/<int:id>/moveItem/',moveItem,name="moveItem"),
]