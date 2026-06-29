from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/station/", include("station.urls", namespace="station")),
    path("api/user/", include("accounts.urls", namespace="accounts")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/doc/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]
