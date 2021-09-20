FROM python:3.8

RUN apt update && apt install -y postgresql-client

RUN pip install pipenv

WORKDIR /opt/shortcut/

COPY src/requirements/Pipfile src/requirements/Pipfile.lock ./

RUN pipenv install --system --deploy --dev

COPY . /opt/shortcut/


RUN chmod +x "./entrypoint.sh"
ENTRYPOINT ["sh", "./entrypoint.sh"]

EXPOSE 8000
ENV PORT 8000