FROM python:3.11-slim

# install requirements
COPY requirements.txt /TheFool
workdir /TheFool
run python3 pip install -r requirements.txt

# copy project
COPY . /TheFool
workdir /TheFool
CMD py main.py