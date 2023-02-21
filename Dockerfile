FROM python:3.8-alpine

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

EXPOSE 8773

ENTRYPOINT [ "uvicorn" ]
CMD ["app.main:app", "--port", "8773", "--host", "0.0.0.0", "--reload" ]
