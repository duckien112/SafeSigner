from eth_account import Account
from hexbytes import HexBytes
from lib import *
import getpass

contractTransactionHash = input("Enter contract_transaction_hash: ")
number = getpass.getpass("Enter number with 9 chars in Visa: ")
password = getpass.getpass("Enter word with 9 chars in Visa: ")
seeds = getpass.getpass("Enter seeds: ")
mnemonic = encryptSeeds('0', number, password, seeds)

contract_transaction_hash = HexBytes(contractTransactionHash)
#account = Account.from_key('')
Account.enable_unaudited_hdwallet_features()
account = Account.from_mnemonic(mnemonic)
signature = account.signHash(contract_transaction_hash)
print(signature.signature.hex())
