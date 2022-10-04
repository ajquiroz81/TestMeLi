# Dockerfile, Image, Container
FROM python:3.11.0rc2-slim
ADD main.py .
RUN pip freeze > requirements.txt .
RUN pip install -r requirements.txt
CMD [ "python", "./main.py"]
EXPOSE 3306:3306
