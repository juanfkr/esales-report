FROM python:3.14-slim

# Definir diretório de trabalho
WORKDIR /app

# Instalar dependências do sistema necessárias para WeasyPrint
RUN apt-get update && apt-get install -y \
    libpango-1.0-0 \
    libpango1.0-dev \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    libcairo2 \
    && rm -rf /var/lib/apt/lists/*

# Instalar Poetry
RUN pip install --no-cache-dir poetry==2.3.2

# Copiar arquivos de dependências
COPY pyproject.toml poetry.lock ./

# Instalar dependências do projeto
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Copiar código fonte
COPY src/ ./src/
COPY shared/ ./shared/

# Criar diretório para saída de PDFs se não existir
RUN mkdir -p shared/pdfs

# Comando padrão
ENTRYPOINT ["python", "src/main.py"]
CMD []