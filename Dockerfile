FROM python:3.9-alpine

WORKDIR /app

RUN apk add --no-cache libstdc++ libffi

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "-m", "Adarsh"]
