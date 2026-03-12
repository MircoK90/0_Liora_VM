# mini bs, coping files of in tests/....
FROM python:3.10-slim

# working folders for teh containers like /app/test_authentication.py ...
WORKDIR /app

RUN pip install requests

COPY tests/ /app/

# fallback "startingpoint" when startzing seperatly
CMD ["python", "authentication.py"]