FROM python:3.9

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y --no-install-recommends \
    sumo \
    sumo-tools \
    sumo-doc 

RUN pip install eclipse-sumo==1.22.0
RUN pip install --upgrade traci sumolib
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "script.py"]