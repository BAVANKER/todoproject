from django.urls import path
from . import views
app_name = 'todoapp'
# ENV NAME: todo, ADMIN NAME: todo, PASSWORD: 1234, DATABASE NAME: newtodo
# you can only view the home by entering http://127.0.0.1:8000/cbvhome
urlpatterns = [
    path('', views.add, name='add'),
    path('delete/<int:task_id>/', views.delete, name='delete'),
    path('update/<int:task_id>/', views.update, name='update'),

]
