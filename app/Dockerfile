FROM python:3.9.13

WORKDIR /opt/app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip \
    && pip install -r requirements.txt --no-cache-dir

COPY . .


ENTRYPOINT ["python3"]
CMD ["main.py"]