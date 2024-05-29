FROM python:3.12.3

RUN mkdir /beta

WORKDIR /beta

COPY poetry.lock pyproject.toml ./
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-dev

COPY conf /beta/conf
COPY src /beta/src
RUN cd /beta

CMD gunicorn -c conf/gunicorn.conf.py 'src.beta.main.web_api:create_app()'