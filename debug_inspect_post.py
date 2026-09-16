import requests
from pathlib import Path

url = 'http://127.0.0.1:5000/api/pipeline-preview'
sample = Path('uploads/9fd08b9d31384493887e6b66d9693bd3_09ae01a2695744a3917751f7158f6599_original.png')
if not sample.exists():
    print('Sample not found:', sample)
else:
    with open(sample, 'rb') as f:
        files = {'image': (sample.name, f, 'image/png')}
        try:
            r = requests.post(url, files=files, timeout=120)
            print('status', r.status_code)
            try:
                print(r.json())
            except Exception:
                print(r.text)
        except Exception as e:
            print('request failed:', e)
