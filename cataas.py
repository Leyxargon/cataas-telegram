import requests

def get_cat() -> str:
	"""
	Requests a json document that has an URL containing a cat picture.
	@return			the url containing the picture of the cat.
	"""
	contents = requests.get('https://cataas.com/cat?json=true').json()
	url = contents['url']
	return 'https://cataas.com/' + url

def get_labeled_cat(str) -> str:
	"""
	Requests a json document that has an URL containing a cat picture
	with label passed by parameter to this function.
	@param	str		a part of URL used to pass to the API the string that will be on the cat picture
	@return			the url containing the picture of the cat.
	"""
	contents = requests.get('https://cataas.com/cat/says/'+ str +'?json=true').json()
	url = contents['url']
	return 'https://cataas.com/' + url

def get_gif() -> str:
	"""
	Requests a json document that has an URL containing a feline GIF.
	@return			the url containing the feline GIF.
	"""
	contents = requests.get('https://cataas.com/cat/gif?json=true').json()
	url = contents['url']
	return 'https://cataas.com/' + url
