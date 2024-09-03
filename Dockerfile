FROM python:3.11

WORKDIR /usr/app
COPY . .

RUN pip install -r ./requirements.txt

EXPOSE 8000
CMD [ "streamlit", "run", "app.py", "--server.port", "8000"]

