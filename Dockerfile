FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
RUN python -c "import os; open('osk.db', 'a').close() if not os.path.exists('osk.db')"
EXPOSE 5000
CMD ["python", "app.py"]