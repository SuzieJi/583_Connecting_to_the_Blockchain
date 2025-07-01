import requests
import json

PINATA_JWT = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiIxZDEyYzZlZS03NzVkLTQwYTItYjYxZC00YjA2NDE3NzA3YmQiLCJlbWFpbCI6Inl5MjAyM0BzZWFzLnVwZW5uLmVkdSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJwaW5fcG9saWN5Ijp7InJlZ2lvbnMiOlt7ImRlc2lyZWRSZXBsaWNhdGlvbkNvdW50IjoxLCJpZCI6IkZSQTEifSx7ImRlc2lyZWRSZXBsaWNhdGlvbkNvdW50IjoxLCJpZCI6Ik5ZQzEifV0sInZlcnNpb24iOjF9LCJtZmFfZW5hYmxlZCI6ZmFsc2UsInN0YXR1cyI6IkFDVElWRSJ9LCJhdXRoZW50aWNhdGlvblR5cGUiOiJzY29wZWRLZXkiLCJzY29wZWRLZXlLZXkiOiI1MjAxODE3Y2QzZjc5NDgyMTQyYiIsInNjb3BlZEtleVNlY3JldCI6ImNjMmI4YjJiOTA0MTU2YzU4ZTRiODU1MTZiNDkzZmMwZmZiZTk4MGFkYjJiOTc1NWQ0OGRjZGNiMmVjYzQzMjQiLCJleHAiOjE3ODI0NDcyMTl9.eNHoJ0_gEwQwtBexBBaZuCs91YTVHyLIWbLwP65lsLY"
PINATA_PIN_JSON_URL = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
PINATA_GATEWAY = "https://gateway.pinata.cloud/ipfs"

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	headers = {
			"Content-Type": "application/json",
			"Authorization": f"Bearer {PINATA_JWT}"
	}
	payload = {"pinataContent": data}

	response = requests.post(PINATA_PIN_JSON_URL, headers=headers, json=payload)
	response.raise_for_status()
	result = response.json()
	cid = result.get("IpfsHash")
	if not cid:
			raise Exception(f"Failed to retrieve CID: {result}")
	##
	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
	params = {'arg': cid}
		url = f"{PINATA_GATEWAY}/{cid}"
		response = requests.get(url)
		response.raise_for_status()

		if content_type.lower() == "json":
				return response.json()
		else:
				return response.content
	##
	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data


