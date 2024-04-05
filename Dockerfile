FROM python:3.10-alpine

WORKDIR /user-sport-app

COPY . .

COPY app/config/env_cloud.py app/config/env.py

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]