from django.urls import include, path
from rest_framework import routers, permissions
from scraper_api.views import *

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = routers.DefaultRouter()
router.register(r'station', StationsViewSet)
router.register(r'daily', DailyTrafficViewSet)
router.register(r'hourly', HourlyTrafficViewSet)



schema_view = get_schema_view(
    openapi.Info(
        title = "subway-project",
        default_version = "1.1.1",
        description = "Subway API 문서",
        terms_of_service = "https://www.google.com/policies/terms/",
        # contact = openapi.Contact(email = <"your email">), 
        # license = openapi.License(name = <"your name">),
    ),
    public = True,
    permission_classes = [permissions.AllowAny],
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include(router.urls)),
]