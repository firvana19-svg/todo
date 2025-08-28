from django.urls import path
from . import views

urlpatterns = [
    # Add Feature
    path('addTask/', views.addTask, name='addTask'),

    # mark as Done Feature
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),

    # Mark as Undone Feature
    path('undone/<int:pk>/', views.undone, name='undone'),

    # Edit Feature
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),

    #delete Feature
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
]