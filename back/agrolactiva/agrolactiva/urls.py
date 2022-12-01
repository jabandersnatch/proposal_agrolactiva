"""agrolactiva URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

# Swagger API documentation view for the API available at /api/docs only for authenticated users
schema_view = get_swagger_view(title='Agrolactiva API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('product_control.urls', namespace='product_control')),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/docs/', schema_view)
]
