FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["top", "-b"]

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY .. /code/

RUN python manage.py migrate


