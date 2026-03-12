import os
import requests

os.makedirs('logs', exist_ok=True)
api_address = os.environ.get('API_ADDRESS', 'api')
api_port = 8000

tests = [
    ('bob', 'builder', 'v1', 200),
    ('bob',   'builder', 'v2', 403),
    ('alice', 'wonderland', 'v1', 200),
    ('alice', 'wonderland', 'v2', 200)
]

for username, password, expected in tests:
    r = requests.get(
        url=f'http://{api_address}:{api_port}/permissions',
        params={'username': username, 'password': password}
    )
    status_code = r.status_code
    test_status = 'SUCCESS' if status_code == expected else 'FAILURE'

    output = f'''
============================
    Authentication test
============================
request done at "/permissions"
| username="{username}"
| password="{password}"
expected result = {expected}
actual result   = {status_code}
==>  {test_status}
'''
    print(output)

    if os.environ.get('LOG') == '1':
        with open('logs/api_test.log', 'a') as f:
            f.write(output)