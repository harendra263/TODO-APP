from email.charset import add_codec
from django.urls import path
from .views import home, login, signup, add_todo, signout, delete_todo, change_status

urlpatterns = [
    path('',home, name= 'home'),
    path('login', login, name = 'login'),
    path('signup/', signup, name = 'signup'),
    path('delete-todo/<int:id>', delete_todo, name = 'delete_todo'),
    path('add-todo/', add_todo),
    path('logout/', signout),
    path('change-status/<int:id>/<str:status>', change_status),
]
