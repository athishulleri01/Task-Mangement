from django.urls import path
from .views import TaskCreateView, TaskAssignView,UserTasksView
from uuid import UUID  

urlpatterns = [
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/assign/<int:task_id>/", TaskAssignView.as_view(), name="task-assign"),
    path("user-tasks/<uuid:user_id>/", UserTasksView.as_view(), name="user-tasks"),
]

