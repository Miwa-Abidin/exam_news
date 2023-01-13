
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from news import views

from account import views as acc_view
from rest_framework.routers import DefaultRouter


acc_router = DefaultRouter()
acc_router.register('register', acc_view.AuthorRegisterApiView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/', include(acc_router.urls)),
    path('api/auth/', include('rest_framework.urls')),
    path('api/account/token/', obtain_auth_token),
    path('api/news/', views.NewsCreateApiView.as_view()),
    path('api/news/<int:pk>/', views.NewsCreateRetrieveUpdateDestroyApiView.as_view()),
    path('api/news/<int:pk>/comments/', views.CommentCreateViewSet.as_view()),

]
