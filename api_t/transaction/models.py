from django.db import models

class IsFraud(models.Model):
    nom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    cash_int = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cash_out = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    oldsolde = models.DecimalField(max_digits=10, decimal_places=2)
    newsolde= models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    isfraude = models.IntegerField(default=0)
    def __str__(self):
        return self.nom

class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    solde = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)


    # Ajoutez d'autres champs utilisateur si nécessaire

    def __str__(self):
        return self.nom


class TransactionLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=200)
    status_code = models.IntegerField()
    response = models.TextField()


    def __str__(self):
        return f"transaction {self.id} le {self.timestamp} sur le point de terminaison  {self.method}  {self.path}  status code {self.status_code} response {self.response} "
