# monprojet/urls.py
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from transaction.urls import router as transaction_router
# from transaction.views import UtilisateurViewSet, UtilisateurViewSetRetrait, UtilisateurViewSetDepot

router = routers.DefaultRouter()
router.registry.extend(transaction_router.registry)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
