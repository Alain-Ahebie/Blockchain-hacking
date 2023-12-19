from web3 import Web3

INFURA = 'https://mainnet.infura.io/v3/12765045634040aba2c2ae29a97be8d4'

#Connect to Blockchain
web3 = Web3(Web3.HTTPProvider(INFURA))
print(f'Connected: {web3.is_connected()}')
      
#Connect to contract
target_adresse = web3.to_checksum_address("")
target_ABI = ''
target = web3.eth.contract(address=target_adresse, abi=target_ABI)