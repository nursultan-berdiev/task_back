from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from todo.views import TaskViewSet, UserCreateView


router = DefaultRouter()
router.register('task', TaskViewSet, basename='task')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/user/create/', UserCreateView.as_view()),
    path('api/user/get_token/', obtain_auth_token),
    path('api/auth/', include('rest_framework.urls'))
]
