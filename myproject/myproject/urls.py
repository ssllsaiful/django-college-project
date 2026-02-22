from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from api.views import students_list, teachers_list
from api.views import subjects_list


  # make sure correct path

schema_view = get_schema_view(
   openapi.Info(
      title="College API",
      default_version='v1',
      description="API for Students and Teachers",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # include your app URLs
    path('api/v2/students/', students_list),
    path('api/v2/teachers/', teachers_list),
    path('api/v2/subjects/', subjects_list),

    # Swagger UI
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]