# syntax=docker/dockerfile:1
FROM python:3.10-slim

WORKDIR /app

RUN pip install flask==3.0.*

RUN pip install emoji==2.8.*

COPY my_thingy.py .

EXPOSE 5000

CMD ["python", "my_thingy.py"]