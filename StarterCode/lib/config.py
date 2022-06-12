from bitcoin import SelectParams
from bitcoin.base58 import decode
from bitcoin.core import x
from bitcoin.wallet import CBitcoinAddress, CBitcoinSecret, P2PKHBitcoinAddress


SelectParams('testnet')

faucet_address = CBitcoinAddress('mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB')

# For questions 1-3, we are using 'btc-test3' network. For question 4, you will
# set this to be either 'btc-test3' or 'bcy-test'
network_type = 'btc-test3'


######################################################################
# This section is for Questions 1-3
# TODO: Fill this in with your private key.
#
# Create a private key and address pair in Base58 with keygen.py
# Send coins at https://testnet-faucet.mempool.co/

# Private key: cQ6QPnfjrkEBLExjzFnDvmM8eSdVKqaxckKxdyWKQSVhTuR1V9KQ
# Address: mrPGjWmHoXHE9MrNQk7Cmtzyft2sM7bX9V
my_private_key = CBitcoinSecret(
    'cQ6QPnfjrkEBLExjzFnDvmM8eSdVKqaxckKxdyWKQSVhTuR1V9KQ')

my_public_key = my_private_key.pub
my_address = P2PKHBitcoinAddress.from_pubkey(my_public_key)
######################################################################

# ######################################################################
# # NOTE: This section is for Question 4
# # TODO: Fill this in with address secret key for BTC testnet3
# #
# # Create address in Base58 with keygen.py
# # Send coins at https://testnet-faucet.mempool.co/

# # Only to be imported by alice.py
# # Alice should have coins!!

# # Private key: cTE83sHns9b8VZfv8mApwc4qznMWtHrVKR9aGe1qjZQXj6pmb9Wm
# # Address: muVuLFEY3HVjcKS3bEveovCLeiNgFd7ZNQ
# alice_secret_key_BTC = CBitcoinSecret(
#     'cTE83sHns9b8VZfv8mApwc4qznMWtHrVKR9aGe1qjZQXj6pmb9Wm')

# # Only to be imported by bob.py
# # Private key: cULsZz4nSdovEtXBjd22ikGULtk2PzvkKKacaQvGAuMN64EmnKPw
# # Address: mySMXgEfVdwb85Q32wtgGBbbPxRYXbaiuQ
# bob_secret_key_BTC = CBitcoinSecret(
#     'cULsZz4nSdovEtXBjd22ikGULtk2PzvkKKacaQvGAuMN64EmnKPw')

# # Can be imported by alice.py or bob.py
# alice_public_key_BTC = alice_secret_key_BTC.pub
# alice_address_BTC = P2PKHBitcoinAddress.from_pubkey(alice_public_key_BTC)

# bob_public_key_BTC = bob_secret_key_BTC.pub
# bob_address_BTC = P2PKHBitcoinAddress.from_pubkey(bob_public_key_BTC)
# ######################################################################


# ######################################################################
# # NOTE: This section is for Question 4
# # TODO: Fill this in with address secret key for BCY testnet
# #
# # Create address in hex with
# # curl -X POST https://api.blockcypher.com/v1/bcy/test/addrs?token=YOURTOKEN
# # This request will return a private key, public key and address. Make sure to save these.
# #
# # Send coins with
# # curl -d '{"address": "BCY_ADDRESS", "amount": 1000000}' https://api.blockcypher.com/v1/bcy/test/faucet?token=YOURTOKEN
# # This request will return a transaction reference. Make sure to save this.

# # Only to be imported by alice.py
# alice_secret_key_BCY = CBitcoinSecret.from_secret_bytes(
#     x('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'))

# # Only to be imported by bob.py
# # Bob should have coins!!
# bob_secret_key_BCY = CBitcoinSecret.from_secret_bytes(
#     x('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'))

# # Can be imported by alice.py or bob.py
# alice_public_key_BCY = alice_secret_key_BCY.pub
# alice_address_BCY = P2PKHBitcoinAddress.from_pubkey(alice_public_key_BCY)

# bob_public_key_BCY = bob_secret_key_BCY.pub
# bob_address_BCY = P2PKHBitcoinAddress.from_pubkey(bob_public_key_BCY)
# ######################################################################
