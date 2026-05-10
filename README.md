# E-Sales Report

Geração de relatórios mensais em PDF com base em planilhas de vendas para empresas de E-commerce.

## Objetivo

Simular um cenário real de processamento de dados por meio de um workflow completo: **leitura → sanitização → análise → geração de relatórios**, transformando dados brutos em relatórios PDF úteis para tomadas de decisões estratégicas.

## Tecnologias, ferramentas e recursos utilizados

- **Pandas 3.0.2** - manipulação e análise de dados
- **WeasyPrint 68.1** - geração de PDF's com base em HTML/CSS
- **Python 3.14** - linguagem base
- **Docker** - containerização da aplicação
- **Kaggle** - datasets reais para testes

## Funcionalidades

- Leitura de arquivos CSV com validação de caminho
- Sanitização automática: duplicatas, valores nulos, conversão de tipos
- Cálculo de métricas: receita, ticket médio, taxa de entrega, top categorias/marcas/países
- Geração de relatórios PDF com tabelas e resumo financeiro
- Filtro por período (mês/ano)

## Executar o projeto

### Opção 1: Instalação Local com venv

#### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/esales-report.git
cd esales-report
```

#### 2. Criar ambiente virtual e instalar dependências
```bash
python3 -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

#### 3. Executar a aplicação

**Gerar relatório completo (todos os dados):**
```bash
python src/main.py
```

**Gerar relatório de período específico:**
```bash
python src/main.py --month 1 --year 2023
```

**Com CSV customizado:**
```bash
python src/main.py --csv /caminho/para/file.csv --month 6 --year 2023
```

### Opção 2: Com Docker

#### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/esales-report.git
cd esales-report
```

#### 2. Buildar a imagem Docker
```bash
docker build -t esales-report .
```

#### 3. Executar com Docker

**Gerar relatório completo:**
```bash
docker run --rm -v $(pwd)/shared/pdfs:/app/shared/pdfs esales-report
```

**Gerar relatório de período específico:**
```bash
docker run --rm -v $(pwd)/shared/pdfs:/app/shared/pdfs esales-report --month 1 --year 2023
```

**Com CSV customizado:**
```bash
docker run --rm -v $(pwd)/shared:/app/shared esales-report --csv shared/sheets/custom.csv --month 6 --year 2023
```

## Estrutura do projeto

```
esales-report/
├── src/
│   ├── main.py                    # entry point
│   ├── path_handler.py            # validação de caminhos
│   ├── dataframe_service.py       # leitura e sanitização de CSV
│   ├── metrics_service.py         # cálculo de métricas
│   └── report_generator.py        # geração de PDF
├── shared/
│   ├── sheets/
│   │   └── Amazon-sales.csv       # exemplo de dataset
│   └── pdfs/                      # saída dos relatórios gerados
├── .venv/                         # ambiente virtual Python
├── Dockerfile
├── requirements.txt
└── README.md
```

## Métricas Geradas

O relatório PDF inclui:

- **Resumo Executivo:** Total de pedidos, receita total, ticket médio, taxa de entrega
- **Status de Pedidos:** Entregues, cancelados, devolvidos
- **Top 5 Categorias e Marcas:** Por quantidade de pedidos
- **Receita por País:** Top 5 países com maior faturamento
- **Receita por Método de Pagamento:** Distribuição de pagamentos
- **Resumo Financeiro:** Descontos, impostos, custos de frete

## Exemplo de uso

```bash
# Ativar ambiente virtual
source .venv/bin/activate

# Gerar relatório de janeiro de 2023
$ python src/main.py --month 1 --year 2023
✓ 15 registros carregados
✓ Métricas calculadas
✓ PDF gerado: /seu-diretorio/esales-report/shared/pdfs/relatorio_01_2023.pdf
```

## Contribuindo

Este é um projeto puramente para fins de aprendizado. Sinta-se livre para adaptar e utilizar conforme necessário.
