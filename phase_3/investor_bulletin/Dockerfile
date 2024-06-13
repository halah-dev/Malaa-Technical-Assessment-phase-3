FROM python:3.11.4

# WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

WORKDIR phase_3/investor_bulletin

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH phase_3/investor_bulletin

EXPOSE 8000

CMD ["fastapi", "run", "api/main.py", "--port", "8000"]
