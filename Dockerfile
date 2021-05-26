FROM python:3

# copy script into container
COPY ./probable_tribble/ .

# run script by default
ENTRYPOINT ["python3", "/tribble.py"]