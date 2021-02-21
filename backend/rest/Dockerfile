FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /rest
COPY requirements.txt /rest/
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /rest/