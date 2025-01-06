from django.urls import path
from .views import (
    TaskDelete,
    TaskList,
    TaskDetail,
    TaskCreate,
    TaskUpdate,
    CustomLoginView,
    RegisterPage,
    TaskReorder,
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # Authentication URLs
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    # Task Management URLs
    path('', TaskList.as_view(), name='tasks'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', TaskDelete.as_view(), name='task-delete'),
    path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),
]
