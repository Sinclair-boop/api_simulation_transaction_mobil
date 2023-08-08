# transactions/views.py
import decimal
import time

import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Utilisateur, IsFraud
from .serializers import UtilisateurSerializer, IsFraudSerializer
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail


class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer

    # permission_classes = (IsAuthenticated,)
    # PUT utilisateur/retrait/{id}/
    def update(self, request, pk):
        utilisateur = self.get_object()

        datauser = {
            f'nom': utilisateur.nom,
            f'telephone': utilisateur.telephone,
            f'oldsolde': utilisateur.solde,
            f'date': utilisateur.date,
        }
        response = requests.get('http://127.0.0.1:8001/pre/model/', params=datauser)
        inst = IsFraud()
        inst.isfraude = response.json()['isfraud']
        inst.nom = response.json()['nom']
        inst.telephone = response.json()['telephone']
        inst.date = response.json()['date']
        inst.oldsolde = response.json()['oldsolde']
        inst.cash_out = request.data["solde"]
        montant = decimal.Decimal(request.data["solde"])
        if response.json()['isfraud'] == 0:
            if montant is None:
                inst.newsolde = response.json()['oldsolde']
                inst.save()
                return Response({'message': 'Le montant est requis.'}, status=status.HTTP_400_BAD_REQUEST)
            if utilisateur.solde < montant:
                inst.newsolde = response.json()['oldsolde']
                inst.save()
                return Response({'message': 'Fonds insuffisants.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                utilisateur.solde -= montant
                inst.newsolde = utilisateur.solde
                inst.save()
                utilisateur.save()
                result = {
                    f'nom': utilisateur.nom,
                    f'nouveau solde': utilisateur.solde,
                }

                return Response(f"{result}", status=status.HTTP_201_CREATED)
        else:
            inst.newsolde = response.json()['oldsolde']
            inst.save()
            # Obtenez l'adresse e-mail du destinataire depuis la demande
            user_email = 'ngapoutfotso@gmail.com'
            # Générez le contenu du message (sujet, contenu HTML, etc.)
            subject = 'Confirmation de processus'
            context = {
                f'id': utilisateur.id,
                f'nom': utilisateur.nom,
                f'solde': utilisateur.solde,
                f'telephone': utilisateur.telephone,
                f'montant': montant,
                f'lien': 'http://192.168.160.154:8000/email/'
            }
            html_message = render_to_string('./emails/email.html', context)
            plain_message = strip_tags(html_message)

            # Envoyez l'e-mail initial à l'utilisateur
            send_mail(subject, plain_message, 'bienvuemarketboutique@gmail.com', [user_email],
                      html_message=html_message)
            result = {
                f'status': "transaction non autorise merci de contacte la direction a l'adress 8080",
            }
            return Response(result, status=status.HTTP_201_CREATED)


class UtilisateurViewSetDepot(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
# PUT utilisateur/depot/{id}/
    def update(self, request, pk):
        utilisateur = self.get_object()

        datauser = {
            f'nom': utilisateur.nom,
            f'telephone': utilisateur.telephone,
            f'oldsolde': utilisateur.solde,
            f'date': utilisateur.date,
        }
        response = requests.get('http://127.0.0.1:8001/pre/model/', params=datauser)
        inst = IsFraud()
        inst.isfraude = response.json()['isfraud']
        inst.nom = response.json()['nom']
        inst.telephone = response.json()['telephone']
        inst.date = response.json()['date']
        inst.oldsolde = response.json()['oldsolde']
        inst.cash_int = request.data["solde"]

        # montant = decimal.Decimal(request.data["solde"])
        montant = decimal.Decimal(request.data["solde"])
        if montant is None:
            inst.newsolde = response.json()['oldsolde']
            inst.save()
            return Response({'message': 'Le montant est requis.'}, status=status.HTTP_400_BAD_REQUEST)
        utilisateur.solde += montant
        inst.newsolde = utilisateur.solde
        inst.save()
        utilisateur.save()
        result = {
                'nom': utilisateur.nom,
                f'nouveau solde': utilisateur.solde,
        }
        return Response(f"{result}", status=status.HTTP_201_CREATED)
