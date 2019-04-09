FROM python:3-alpine
WORKDIR /app
COPY requirements.txt keywords.py input.json /app/
RUN apk add python3-dev gfortran build-base
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3", "keywords.py","input.json","5"]