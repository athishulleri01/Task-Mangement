from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer

User = get_user_model()


class TaskCreateView(generics.CreateAPIView):
    """
    API to create a new task.
    Allows users to create tasks by providing a name and description.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskAssignView(APIView):
    """
    API to assign a task to one or multiple users.
    Requires a list of user IDs in the request body.
    """
    
    def post(self, request, task_id):
        try:
            # Fetch the task by ID
            task = Task.objects.get(id=task_id)
            user_ids = request.data.get("user_ids", [])

            # Fetch users by given IDs
            users = User.objects.filter(id__in=user_ids)

            if not users:
                return Response({"error": "No valid users found."}, status=status.HTTP_400_BAD_REQUEST)

            # Assign users to the task
            task.assigned_users.set(users)
            task.save()

            return Response({"message": "Task assigned successfully!"}, status=status.HTTP_200_OK)

        except Task.DoesNotExist:
            return Response({"error": "Task not found."}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserTasksView(APIView):
    """
    API to fetch all tasks assigned to a specific user.
    Requires user ID in the URL.
    """
    # permission_classes = [IsAuthenticated]  # Uncomment if authentication is needed

    def get(self, request, user_id):
        try:
            # Fetch user by ID
            user = User.objects.get(id=user_id)

            # Fetch all tasks assigned to this user
            tasks = Task.objects.filter(assigned_users=user)
            serializer = TaskSerializer(tasks, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
