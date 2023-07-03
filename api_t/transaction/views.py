# transactions/views.py
import decimal

from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Utilisateur
from .serializers import UtilisateurSerializer

class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer

# PUT todos/{id}/
    def update(self, request, pk):

        utilisateur = self.get_object()
        montant = float(request.data["solde"])
        solde = float(utilisateur.solde)
        if montant is None:
            return Response({'message': 'Le montant est requis.'}, status=status.HTTP_400_BAD_REQUEST)
        if solde < montant:
            return Response({'message': 'Fonds insuffisants.'}, status=status.HTTP_400_BAD_REQUEST)
        solde -= montant
        utilisateur.save()
        result = {
                'nom': utilisateur.nom,
                f'nouveau solde': solde,
        }
        return Response(f"{result}", status=status.HTTP_201_CREATED)
