"""
URL configuration for Test_API project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, re_path
from rest_framework_swagger.views import get_swagger_view
from .views import hello_world
# from .views import upload_resume
from .views import FileUploadView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_swagger_view(title='OPEN VOICE API ')
# schema_view = get_schema_view(
#     openapi.Info(
#         title="My Custom API",
#         default_version='v1',
#         description="My awesome API documentation",
#         terms_of_service="https://www.example.com/terms/",
#         contact=openapi.Contact(email="contact@example.com"),
#         license=openapi.License(name="BSD License"),
#     ),
#     public=True,
# )
urlpatterns = [
    re_path(r'^$', schema_view),
    path('hello/', hello_world, name='hello-world'),
    # path('upload/', upload_resume, name='upload-resume'),
    path('upload/', FileUploadView.as_view(), name='upload-file'),
]
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

