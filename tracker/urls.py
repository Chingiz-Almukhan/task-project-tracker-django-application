from django.urls import path

from tracker.views.add import AddView
from tracker.views.base import IndexView
from tracker.views.delete import Delete
from tracker.views.edit import EditView
from tracker.views.task_view import TaskView

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
    path('task/<int:pk>', TaskView.as_view(), name='task'),
    path('add/', AddView.as_view(), name='add'),
    path('edit/<int:pk>', EditView.as_view(), name='edit'),
    path('delete/confirm/<int:pk>', Delete.as_view(), name='delete')
]