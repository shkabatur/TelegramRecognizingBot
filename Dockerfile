FROM python:3.9

WORKDIR /app
COPY . .
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y ffmpeg
RUN pip install -r requirements.txt
CMD ["python3", "bot.py"]
