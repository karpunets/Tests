FROM python:3

WORKDIR /usr/src/app

COPY Tests ./
COPY Data ./
COPY bin ./
COPY __init__.py ./
COPY conftest.py ./
COPY definition.py ./
COPY definition.py ./
COPY requirements.txt ./

RUN pip install -r requirements.txt

CMD [ "python", "./my_script.py" ]