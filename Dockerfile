FROM python:3.14-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpango-1.0-0 \
    libpango1.0-dev \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    libcairo2 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN python -m pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY shared/ ./shared/

RUN mkdir -p shared/pdfs

ENTRYPOINT ["python", "src/main.py"]
CMD []