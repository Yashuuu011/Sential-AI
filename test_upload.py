import urllib.request
import urllib.parse
import uuid

url = "https://sential-ai-production.up.railway.app/scan/upload"
boundary = uuid.uuid4().hex

body = (
    f"--{boundary}\r\n"
    f"Content-Disposition: form-data; name=\"file\"; filename=\"dummy.txt\"\r\n"
    f"Content-Type: text/plain\r\n\r\n"
    f"dummy malware test\r\n"
    f"--{boundary}--\r\n"
).encode('utf-8')

req = urllib.request.Request(url, data=body, headers={'Content-Type': f'multipart/form-data; boundary={boundary}'})

try:
    with urllib.request.urlopen(req) as response:
        print(f"Status Code: {response.status}")
        print(f"Response Body: {response.read().decode('utf-8')}")
except urllib.error.HTTPError as e:
    print(f"Error Code: {e.code}")
    print(f"Error Body: {e.read().decode('utf-8')}")
except Exception as e:
    print(f"Error: {e}")
