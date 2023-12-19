from web3 import Web3

INFURA = 'https://mainnet.infura.io/v3/12765045634040aba2c2ae29a97be8d4'

#Connect to Blockchain
web3 = Web3(Web3.HTTPProvider(INFURA))
print(f'Connected: {web3.is_connected()}')
      
#Connect to contract
target_adresse = web3.to_checksum_address("0x514910771AF9Ca656af840dff83E8264EcF986CA")

print(web3.from_wei(web3.eth.get_balance(target_adresse),'ether'))

# 1.find if the target adress is a crontract or a wallet
# 2. its machine code in assembly ==> disassemble into assembly 
# 3. and go futher down into decompilation into regular source code(it's white Code)
print(web3.to_hex(web3.eth.get_code(target_adresse)))
