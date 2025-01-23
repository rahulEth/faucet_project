from django.db import models

class Transaction(models.Model):
    wallet_address = models.CharField(max_length=42)
    transaction_hash = models.CharField(max_length=66)
    status = models.BooleanField(default=True)  # True for success, False for failure
    ip_address = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)
    error_message = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'faucet_app_transaction'
        managed = True

