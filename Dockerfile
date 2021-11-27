FROM python:3.9.7
COPY ./src ./src
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
CMD [ "uvicorn", "--host", "0.0.0.0", "--port", "80", "--workers", "10", "src.main:app" ]