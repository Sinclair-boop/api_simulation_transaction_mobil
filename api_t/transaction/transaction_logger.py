from .models import TransactionLog

class TransactionLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # Enregistrement du log de transaction dans la base de données
        transaction_log = TransactionLog(
            method=request.method,
            path=request.path,
            status_code=response.status_code,
            response=response.content.decode()
            # Autres champs pertinents pour votre cas
        )
        transaction_log.save()
        return response
