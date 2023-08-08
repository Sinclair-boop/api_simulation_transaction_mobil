from django.contrib import admin

from transaction.models import Utilisateur, TransactionLog, IsFraud

admin.site.register(Utilisateur)
admin.site.register(TransactionLog)
admin.site.register(IsFraud)