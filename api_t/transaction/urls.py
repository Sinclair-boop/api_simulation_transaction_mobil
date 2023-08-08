from rest_framework import routers

from transaction.views import UtilisateurViewSet,  UtilisateurViewSetDepot

    # ReceiveEmailResponseView
    # UtilisateurViewSetRetrait,
router = routers.DefaultRouter()
router.register(r'utilisateurs', UtilisateurViewSet)
# router.register(r'isfraud', ReceiveEmailResponseView)
# router.register(r'receive-email-response/', ReceiveEmailResponseView, basename='MyModel')
# router.register(r'utilisateurs/utilisateur', UtilisateurViewSet)
# router.register(r'utilisateurs/utilisateur/retrait', UtilisateurViewSetRetrait)
router.register(r'utilisateurs/depot', UtilisateurViewSetDepot)