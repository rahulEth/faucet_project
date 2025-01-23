from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from datetime import timedelta
from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator
from .serializers import WalletAddressSerializer, TransactionStatsSerializer
from .models import Transaction
from .utils import send_eth

class FaucetFundView(APIView):
    @method_decorator(ratelimit(key='ip', rate='1/m', method=['POST']))
    def post(self, request):
        print('----------:--------')    
        serializer = WalletAddressSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        wallet_address = serializer.validated_data['wallet_address']
        ip_address = request.META.get('REMOTE_ADDR')
        
        # Check if wallet has received funds in the last minute
        recent_transaction = Transaction.objects.filter(
            wallet_address=wallet_address,
            created_at__gte=timezone.now() - timedelta(minutes=1)
        ).first()
        if recent_transaction:
            return Response(
                {"error": "Please wait 1 minute before requesting again"},
                status=status.HTTP_429_TOO_MANY_REQUESTS
            )
            
        try:
            tx_hash = send_eth(wallet_address)
            Transaction.objects.create(
                wallet_address=wallet_address,
                transaction_hash=tx_hash,
                ip_address=ip_address,
                status=True
            )
            return Response({"transaction_id": tx_hash})
        except Exception as e:
            Transaction.objects.create(
                wallet_address=wallet_address,
                transaction_hash="",
                ip_address=ip_address,
                status=False,
                error_message=str(e)
            )
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class FaucetStatsView(APIView):
    def get(self, request):
        last_24h = timezone.now() - timedelta(hours=24)
        successful = Transaction.objects.filter(
            created_at__gte=last_24h,
            status=True
        ).count()
        failed = Transaction.objects.filter(
            created_at__gte=last_24h,
            status=False
        ).count()
        
        serializer = TransactionStatsSerializer(data={
            'successful_transactions': successful,
            'failed_transactions': failed
        })
        serializer.is_valid()
        return Response(serializer.data)
