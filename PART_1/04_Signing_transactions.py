from web3 import Web3

# Make a connection
GANACHE = 'http://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(GANACHE))
print(f'Connected: {web3.is_connected()}')

#accounts for transactions
first_account = "0xfF26933Ee7F623BF74810D211263f22964f53586"
first_account_priv = "0x2164941972dd17afc794781aec4547a37bd37e6f55dfd3b74c11e2c000b84347"
second_account = "0x58AD4f8F3C8c4AbC84b69fCaf7683CD0f07b7E4b"


#build a transaction
transaction = {
     'nonce' : web3.eth.get_transaction_count(first_account),
     'to': second_account,
     'value' : web3.to_wei(1, 'ether'),
     'gas' : 3000000,
     'gasPrice' : web3.to_wei('20', 'gwei')
     
}
#sign and send transaction (transaction + private key)
signed_transacion = web3.eth.account.sign_transaction(transaction, first_account_priv)
transaction_hash = web3.eth.send_raw_transaction(signed_transacion.rawTransaction)

print("HASH",Web3.to_hex(transaction_hash))
print(web3.eth.get_transaction(transaction_hash))