from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("basquet/", admin.site.urls),
    path("", include("core.urls")),
    path("club", include("club.urls")),
]
