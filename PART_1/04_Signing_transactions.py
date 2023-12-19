from web3 import Web3

# Make a connection
GANACHE = 'http://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(GANACHE))
print(f'Connected: {web3.is_connected()}')

#accounts for transactions
first_account = "0x9665b12B2A6634E856766f5b675a87891ed08EA9"
first_account_priv = "0xf5bc48486dff252df456a2e2a897f6ae5440d0bf9453493410864062274d7770"
second_account = "0x52cAcd9BE516376c335d5453a9eB381D735e6168"


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

print(Web3.to_hex(transaction_hash))
print(web3.eth.get_transaction(transaction_hash))