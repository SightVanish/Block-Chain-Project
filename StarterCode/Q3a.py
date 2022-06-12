from sys import exit
from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import send_from_P2PKH_transaction

# Private key: cTcg4BkuDxiQqRNCV7iZ3Tu6jUcR9X9ihvwaszh4MDYTcKNs8QWz
# Address: myRcvr2A3CqXTveq65RE235qhfrtFgF5gK
cust1_private_key = CBitcoinSecret(
    'cTcg4BkuDxiQqRNCV7iZ3Tu6jUcR9X9ihvwaszh4MDYTcKNs8QWz')
cust1_public_key = cust1_private_key.pub

# Private key: cQtafo4eP8ZddjmRkCjLYTEkT4pDsfa9Qg5QEEk1rujGR7kdGuGS
# Address: mrBAsXfkzmUegjiFMeaHGYh2bR9XkPJMTS
cust2_private_key = CBitcoinSecret(
    'cQtafo4eP8ZddjmRkCjLYTEkT4pDsfa9Qg5QEEk1rujGR7kdGuGS')
cust2_public_key = cust2_private_key.pub

# Private key: cRxxfEF7VC6TpoR8WoHBejgUoLyJsCkEtzCYL35AtZZRNjZSAtQt
# Address: mjAoZk9VNYzd9EFTyf1SA9pTPcz3it7eWA
cust3_private_key = CBitcoinSecret(
    'cRxxfEF7VC6TpoR8WoHBejgUoLyJsCkEtzCYL35AtZZRNjZSAtQt')
cust3_public_key = cust3_private_key.pub


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 3

# You can assume the role of the bank for the purposes of this problem
# and use my_public_key and my_private_key in lieu of bank_public_key and
# bank_private_key.

Q3a_txout_scriptPubKey = [
    OP_2, my_public_key, cust1_public_key, cust2_public_key, cust3_public_key, OP_4, OP_CHECKMULTISIG
]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00005 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        '92e0432c680bec4ca0a4600c46180a6766031782e6678634d454e7544db45202')
    utxo_index = 4 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(amount_to_send, txid_to_spend, 
        utxo_index, Q3a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
