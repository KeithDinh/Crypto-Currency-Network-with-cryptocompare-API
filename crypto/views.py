from django.shortcuts import render
import requests
import json
# Create your views here.
def home(request):

	# WARNING: You may need the API key attached at the end of the request URL

	# ******************************************************** CRYPTO PRICE ******************************************************** #
	# request the data from server: 
	price_request = requests.get\
	("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD,EUR")
	
	# convert the data into json 
	price = json.loads(price_request.content)
	# copy to file for better interpretation: open("PriceTemplate.txt",'w').write(json.dumps(price,indent=2))


	# ******************************************************** CRYPTO NEWS ******************************************************** #
	# request the data from server: 
	api_request = requests.get\
	("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	
	# convert the data into json 
	api = json.loads(api_request.content)
	# copy to file for better interpretation: open("NewsTemplate.txt",'w').write(json.dumps(api,indent=2))

	
	return render(request, 'home.html', {'api' : api, 'price': price})

def prices(request):
	cryptolist = {'Bitcoin':'XBT', 'Ether':'ETH','Litecoin':'LTC','Ripple':'XRP','BitcoinCash':'BCH','US Dollar':'USD','Euro':'EUR'}

	if request.method == "POST":
		quote = request.POST['quote']

		# ******************************************************** CRYPTO PRICE ******************************************************** #
		# request the data from server : 
		crypto_request = requests.get\
		("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote.upper() + "&tsyms=USD")
		
		# convert the data into json 
		crypto = json.loads(crypto_request.content)
		return render(request, 'prices.html', {'quote' : quote, 'crypto' : crypto, "cryptolist" : cryptolist })

	else:
		return render(request, 'prices.html', { "cryptolist" : cryptolist })


