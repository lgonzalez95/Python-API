FROM python:latest

MAINTAINER lgonzalez@test.com

RUN mkdir /automation
COPY ./src /automation/src
COPY ./tests /automation/tests
COPY ./setup.py /automation/setup.py
COPY ./envs/dev.env /automation/envs/dev.env
COPY ./envs/qa.env /automation/envs/qa.env
COPY pytest.ini /automation/pytest.ini

WORKDIR /automation
RUN python3 setup.py install

CMD sleep 5 && pytest