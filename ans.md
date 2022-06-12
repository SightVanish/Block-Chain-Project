transactions.py

```
Q1_txid = 'a18b0f27bd4a17987b8625c549f8c31104f5b8af08900f3cb00779510d5b71a2'

Q2a_txid = '747c7fcf77624c9339f7ed1c2522a845b4e39b7459f46da5801733d48805e5c6'

Q2b_txid = 'd21c1351f0de74a5ae5e6fc8325d41f156f0562a1f16b250ebaafd42215f683a'

Q3a_txid = '374daea0e7366eb6ab289a9868ef0e0d788b61407a630e9e302e5e54bea0633f'

Q3b_txid = '1f4cf74b91158cee90d44136058e054a4e6661edc6980cfdb953d6f98bea9797'
```



Q1.py

```python
from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)


def P2PKH_scriptPubKey(address):
    ######################################################################
    # TODO: Complete the standard scriptPubKey implementation for a
    # PayToPublicKeyHash transaction
    return [
        OP_DUP, OP_HASH160, address, OP_EQUALVERIFY, OP_CHECKSIG
    ]
    ######################################################################


def P2PKH_scriptSig(txin, txout, txin_scriptPubKey, private_key, public_key):
    signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             private_key)
    ######################################################################
    # TODO: Complete this script to unlock the BTC that was sent to you
    # in the PayToPublicKeyHash transaction.
    return [
        signature, public_key 
    ]
    ######################################################################

def send_from_P2PKH_transaction(amount_to_send,
                                txid_to_spend,
                                utxo_index,
                                txout_scriptPubKey,
                                sender_private_key,
                                network):

    sender_public_key = sender_private_key.pub
    sender_address = P2PKHBitcoinAddress.from_pubkey(sender_public_key)

    txout = create_txout(amount_to_send, txout_scriptPubKey)

    txin_scriptPubKey = P2PKH_scriptPubKey(sender_address)
    txin = create_txin(txid_to_spend, utxo_index)
    txin_scriptSig = P2PKH_scriptSig(txin, txout, txin_scriptPubKey,
        sender_private_key, sender_public_key)

    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,
                                       txin_scriptSig)

    return broadcast_transaction(new_tx, network)


if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00005 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        '92e0432c680bec4ca0a4600c46180a6766031782e6678634d454e7544db45202')
    utxo_index = 0 # index of the output you are spending, indices start at 0
    ######################################################################

    txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)
    response = send_from_P2PKH_transaction(
        amount_to_send,
        txid_to_spend,
        utxo_index,
        txout_scriptPubKey,
        my_private_key,
        network_type,
    )
    print(response.status_code, response.reason)
    print(response.text)
```



Q2a.py

```python
from sys import exit
from bitcoin.core.script import *

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import send_from_P2PKH_transaction


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 2
Q2a_txout_scriptPubKey = [
        OP_2DUP, OP_ADD, 1, OP_EQUALVERIFY, OP_SUB, 1, OP_EQUAL
    ]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00005 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        '92e0432c680bec4ca0a4600c46180a6766031782e6678634d454e7544db45202')
    utxo_index = 3 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        Q2a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)

```



Q2b.py

```python
from sys import exit
from bitcoin.core.script import *

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import P2PKH_scriptPubKey
from Q2a import Q2a_txout_scriptPubKey


######################################################################
# TODO: set these parameters correctly
amount_to_send = 0.00001 # amount of BTC in the output you're sending minus fee
txid_to_spend = (
        '747c7fcf77624c9339f7ed1c2522a845b4e39b7459f46da5801733d48805e5c6')
utxo_index = 0 # index of the output you are spending, indices start at 0
######################################################################

txin_scriptPubKey = Q2a_txout_scriptPubKey
######################################################################
# TODO: implement the scriptSig for redeeming the transaction created
# in  Exercise 2a.
txin_scriptSig = [
        1, 0
]
######################################################################
txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)

response = send_from_custom_transaction(
    amount_to_send, txid_to_spend, utxo_index,
    txin_scriptPubKey, txin_scriptSig, txout_scriptPubKey, network_type)
print(response.status_code, response.reason)
print(response.text)

```



Q3a.py

```python
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

```



Q3b.py

```python
from sys import exit
from bitcoin.core.script import *

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import P2PKH_scriptPubKey
from Q3a import (Q3a_txout_scriptPubKey, cust1_private_key, cust2_private_key,
                  cust3_private_key)


def multisig_scriptSig(txin, txout, txin_scriptPubKey):
    bank_sig = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             my_private_key)
    cust1_sig = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             cust1_private_key)
    cust2_sig = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             cust2_private_key)
    cust3_sig = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             cust3_private_key)
    ######################################################################
    # TODO: Complete this script to unlock the BTC that was locked in the
    # multisig transaction created in Exercise 3a.
    return [
        OP_0, bank_sig, cust1_sig
    ]
    ######################################################################


def send_from_multisig_transaction(amount_to_send, txid_to_spend, utxo_index,
                                   txin_scriptPubKey, txout_scriptPubKey, network):
    txout = create_txout(amount_to_send, txout_scriptPubKey)

    txin = create_txin(txid_to_spend, utxo_index)
    txin_scriptSig = multisig_scriptSig(txin, txout, txin_scriptPubKey)

    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,
                                       txin_scriptSig)

    return broadcast_transaction(new_tx, network)

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00001 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        '48e91771442b4af2409c1c0a242b8726a67634d912ddddad57238db12ef920f4')
    utxo_index = 0 # index of the output you are spending, indices start at 0
    ######################################################################

    txin_scriptPubKey = Q3a_txout_scriptPubKey
    txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)

    response = send_from_multisig_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        txin_scriptPubKey, txout_scriptPubKey, network_type)
    print(response.status_code, response.reason)
    print(response.text)

```

