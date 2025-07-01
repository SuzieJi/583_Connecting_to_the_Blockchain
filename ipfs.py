import requests
import json

CHAINSTACK_IPFS_URL      = 'https://bsc-testnet.core.chainstack.com/'
CHAINSTACK_IPFS_USERNAME = 'brave-dubinsky'
CHAINSTACK_IPFS_PASSWORD = 'strive-boney-popper-action-ankle-karma'

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	json_str = json.dumps(data)
	files = {'file': ('data.json', json_str)}
	resp = requests.post(
			f"{CHAINSTACK_IPFS_URL}/add",
			files=files,
			auth=(CHAINSTACK_IPFS_USERNAME, CHAINSTACK_IPFS_PASSWORD)
	)
	resp.raise_for_status()
	result = resp.json()
	cid = result.get('Hash') or result.get('Cid') or result.get('cid')
	if not cid:
			raise RuntimeError(f"Failed to pin data, unexpected response: {result}")
	##
	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
	params = {'arg': cid}
	resp = requests.post(
			f"{CHAINSTACK_IPFS_URL}/cat",
			params=params,
			auth=(CHAINSTACK_IPFS_USERNAME, CHAINSTACK_IPFS_PASSWORD)
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


