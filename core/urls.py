from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework.permissions import AllowAny

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(

    openapi.Info(

        title="Job Portal API",

        default_version='v1',

        description="DRF Job Portal API",

    ),

    public=True,

    permission_classes=[AllowAny],
)

urlpatterns = [

    path('admin/', admin.site.urls),

    path('api/users/', include('users.urls')),

    path('api/candidate/', include('candidate.urls')),

    path('api/employer/', include('employer.urls')),

    path('api/jobs/', include('jobs.urls')),

    path('api/applications/', include('applications.urls')),

    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)