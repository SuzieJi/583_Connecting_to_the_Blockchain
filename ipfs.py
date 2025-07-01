import requests
import json

INFURA_PROJECT_ID     = '5201817cd3f79482142b'
INFURA_PROJECT_SECRET = 'cc2b8b2b904156c58e4b85516b493fc0ffbe980adb2b9755d48dcdcb2ecc4324'
INFURA_URL            = 'https://ipfs.infura.io:5001/api/v0'

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	json_str = json.dumps(data)
	files = {'file': ('data.json', json_str)}
	resp = requests.post(
			f"{INFURA_URL}/add",
			files=files,
			auth=(INFURA_PROJECT_ID, INFURA_PROJECT_SECRET)
	)
	resp.raise_for_status()
	result = resp.json()
	cid = result.get('Hash')
	if not cid:
			raise RuntimeError(f"Failed to pin data: {result}")
	##
	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
	params = {'arg': cid}
	resp = requests.post(
			f"{INFURA_URL}/cat",
			params=params,
			auth=(INFURA_PROJECT_ID, INFURA_PROJECT_SECRET)
	)
	resp.raise_for_status()
	raw = resp.text
	if content_type == "json":
			data = json.loads(raw)
	else:
			raise ValueError(f"Unsupported content_type: {content_type}")
	##
	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data


