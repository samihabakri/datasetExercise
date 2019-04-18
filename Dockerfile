FROM python:3

ADD Test1Data /

RUN pip install pystrich

CMD [ "python", "./Test1Data.py" ]