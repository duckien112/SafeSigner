from eth_account import Account
from hexbytes import HexBytes
from lib import *

contractTransactionHash = input("Enter contract_transaction_hash: ")
number = input("Enter number with 9 chars in Visa: ")
password = input("Enter word with 9 chars in Visa: ")
seeds = input("Enter seeds: ")
mnemonic = encryptSeeds('0', number, password, seeds)

contract_transaction_hash = HexBytes(contractTransactionHash)
#account = Account.from_key('')
Account.enable_unaudited_hdwallet_features()
account = Account.from_mnemonic(mnemonic)
signature = account.signHash(contract_transaction_hash)
print(signature.signature.hex())