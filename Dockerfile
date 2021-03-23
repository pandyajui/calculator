FROM python:3

ADD calcTest.py /

CMD ["python", "./calcTest.py"]