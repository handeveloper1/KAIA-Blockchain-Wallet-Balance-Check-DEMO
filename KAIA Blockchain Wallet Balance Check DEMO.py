from web3 import Web3


RPC_URL = "https://public-en.node.kaia.io"
web3 = Web3(Web3.HTTPProvider(RPC_URL))




ADDRESS = Web3.to_checksum_address("0xea833d7d25797eece3ea1da22b134f82aeeb94eb")


balance_wei = web3.eth.get_balance(ADDRESS)
balance_kaia = web3.from_wei(balance_wei, 'ether')

print(f"Cüzdan Bakiyesi: {balance_kaia} KAIA")
