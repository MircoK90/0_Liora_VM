import os
import requests


os.makedirs('logs', exist_ok=True)
api_address = os.environ.get('API_ADDRESS', 'api')
api_port = 8000

sentences = [                           # from the task
    ('life is beautiful', 'positive'),
    ('that sucks',        'negative'),
]

for version in ['v1', 'v2']:
    for sentence, expected_sentiment in sentences:
        r = requests.get(
            url=f'http://{api_address}:{api_port}/{version}/sentiment',
            params={'username': 'alice', 'password': 'wonderland', 'sentence': sentence}
        )
        score = r.json().get('score', 0)
        actual_sentiment = 'positive' if score > 0 else 'negative'
        test_status = 'SUCCESS' if actual_sentiment == expected_sentiment else 'FAILURE'

        output = f'''
============================
    Content test
============================
request done at "/{version}/sentiment"
| sentence="{sentence}"
expected sentiment = {expected_sentiment}
actual score       = {score} ({actual_sentiment})
==>  {test_status}
'''
        print(output)

        if os.environ.get('LOG') == '1':
            with open('logs/api_test.log', 'a') as f:
                f.write(output)