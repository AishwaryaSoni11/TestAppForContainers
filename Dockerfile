FROM python:3.10.5

WORKDIR /app

COPY requirements.txt .
COPY main.py .
COPY st_desktop.py .
COPY st_mobile.py .
COPY sx_desktop.py .
COPY sx_mobile.py .
COPY currency_exchange.py .
COPY proxy.txt . 
COPY users.json .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD [ "python", "main.py" ]
