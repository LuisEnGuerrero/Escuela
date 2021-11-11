"""biblioteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from autores.views import mi_vista, AutoresView, AutorDetailView
#from editoriales.views import EditorialesGenericView, EditorialesNuevoView, EditorialDetailView, EditorialDetailViewApi, EditorialGenericView
from editoriales.views import EditorialViewSet

router = DefaultRouter()
router.register('editoriales', EditorialViewSet)


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('admin/', admin.site.urls),
    path('autores/', AutoresView.as_view()),
    path('autores/<pk>/', AutorDetailView.as_view()),
] + router.urls

"""
path('editoriales/', EditorialesGenericView.as_view()),
path('editoriales/nuevo/', EditorialesNuevoView.as_view()),
path('editoriales/<pk>/', EditorialDetailView.as_view()),
path('editorial/nuevo/', EditorialDetailView.as_view()),
path('editorial/<pk>/', EditorialDetailViewApi.as_view()),
"""
