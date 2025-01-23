from web3 import Web3
from django.conf import settings
import os

def send_eth(to_address):
    w3 = Web3(Web3.HTTPProvider(settings.ETHEREUM_NODE_URL))
    account = w3.eth.account.from_key(settings.PRIVATE_KEY)
    nonce = w3.eth.get_transaction_count(account.address)
    
    transaction = {
        'nonce': nonce,
        'to': to_address,
        'value': w3.to_wei(0.0001, 'ether'),
        'gas': 21000,
        'gasPrice': w3.eth.gas_price,
        'chainId': 11155111  # Sepolia chain ID
    }
    
    signed_txn = w3.eth.account.sign_transaction(transaction, settings.PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)    
    return w3.to_hex(tx_hash)
