# E-Sales Report
Geração de relatórios mensais em PDF com base em planilhas padronizadas de vendas para empresas de vendas no varejo e atacado.

## Objetivo
Simular um cenário real de processamento de dados por meio de um workflow completo: **leitura → sanitização → análise → geração de relatórios**, transformando dados brutos em relatórios PDF úteis para tomadas de decisões estratégicas.

## Tecnologias, ferramentas e recursos utilizados
- **Pandas 3.0.2** - manipulação e análise de dados
- **WeasyPrint 68.1** - geração de PDF's com base em HTML/CSS
- **Docker** - containerização da aplicação

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

# linux:
source .venv/bin/activate  

# windows: 
.venv\Scripts\activate

pip install -r requirements.txt
```

#### 3. Executar a aplicação

****
```bash
# Gera relatório completo (todos os dados):
python src/main.py

# ou gere o relatório de um período específico
python src/main.py --month 1 --year 2023

# com planilha customizada
python src/main.py --csv /caminho/para/file.csv --month 6 --year 2023
```

### Opção 2: Com Docker

#### 1. Clone o repositório
```bash
git clone https://github.com/juanfkr/esales-report.git
cd esales-report
```

#### 2. Buildar e executar com docker
```bash
# build
docker build -t esales-report .

# Gera relatório completo
docker run --rm -v $(pwd)/shared/pdfs:/app/shared/pdfs esales-report

# gera para um período específico
docker run --rm -v $(pwd)/shared/pdfs:/app/shared/pdfs esales-report --month 1 --year 2023

# com planilha customizada
docker run --rm -v $(pwd)/shared:/app/shared esales-report --csv shared/sheets/custom.csv --month 6 --year 2023
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
Este é um projeto para fins de aprendizado. Sinta-se livre para adaptar e utilizar conforme necessário.
