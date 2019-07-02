FROM python:3.6.5

WORKDIR /usr/src/app

COPY Tests ./Tests
COPY Data ./Data
COPY bin ./bin
COPY __init__.py ./
COPY conftest.py ./
COPY definition.py ./
COPY definition.py ./
COPY config ./config
COPY helpers ./helpers
COPY requirements.txt ./

RUN pip install -r requirements.txt

#docker run smiddle_qa /bin/bash -c "python -m pytest Tests/Manager"