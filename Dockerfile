# Dockerfile, Image, Container
FROM python:3.11.0rc2-slim
ADD main.py .
RUN pip install requests pandas sqlalchemy pymysql
CMD ["python", "./main.py"]