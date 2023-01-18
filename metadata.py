from google.auth import compute_engine
import requests

credentials = compute_engine.Credentials()

url = f'http://metadata.google.internal/computeMetadata/v1/instance/attributes/{attribute}'
headers = {'Metadata-Flavor': 'Google'}
r = requests.get(url, headers=headers, 
                 proxies={'http': 'http://proxy.example.com:8080', 'https': 'http://proxy.example.com:8080'},
                 timeout=5, 
                 verify=True,
                 auth=credentials.create_scoped('https://www.googleapis.com/auth/compute'))
metadata = r.json()
print(json.dumps(metadata, default=str, indent=4))
