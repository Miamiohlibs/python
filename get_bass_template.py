import base64

def get_bass():
	bass = base64.b64encode(b'key:secret')
	return bass.decode("utf-8")
