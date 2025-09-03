FROM registry.access.redhat.com/ubi9/python-39

WORKDIR /app
COPY app.py .

CMD ["python", "app.py"]
