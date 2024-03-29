from web3 import Web3

# Make local connection 
GANACHE = 'http://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(GANACHE))
print(f'Connected: {web3.is_connected()}')

#Connect to contract
# https://remix.ethereum.org/ ==>  
# https://github.com/cclabsInc/Python-SmartContact-BlockchainExploitation/blob/main/Part1_Manual_Interactions/Helloworld_Bank_Target.sol
target_adresse = web3.to_checksum_address("")
target_ABI = ''
target = web3.eth.contract(address=target_adresse, abi=target_ABI)