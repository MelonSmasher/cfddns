FROM python:3-alpine

WORKDIR /cfddns

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

ENV TTL=1800

CMD [ "./docker-entrypoint.sh" ]