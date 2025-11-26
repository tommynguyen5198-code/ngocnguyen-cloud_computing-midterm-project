FROM python:3.10.19
WORKDIR /app
COPY requirement.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 5000
CMD ["python", "app.py"]

