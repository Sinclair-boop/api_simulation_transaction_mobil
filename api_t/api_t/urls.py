# monprojet/urls.py
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from transaction.views import UtilisateurViewSet

router = routers.DefaultRouter()
router.register(r'utilisateurs', UtilisateurViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
