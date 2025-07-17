FROM python:3.12-alpine

WORKDIR /app

COPY . .

RUN pip install --proxy http://172.28.111.10:3128 --trusted-host pypi.python.org --no-cache-dir -r req.txt

EXPOSE 8000

CMD [ "uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000" ]⏎