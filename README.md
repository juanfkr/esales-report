# E-Sales Report

Geração de relatórios mensais em PDF com base em planilhas de vendas para empresas de E-commerce.

## Objetivo

Simular um cenário real de processamento de dados por meio de um workflow completo: **leitura → sanitização → análise → geração de relatórios**, transformando dados brutos em relatórios PDF úteis para tomadas de decisões estratégicas.

## Tecnologias, ferramentas e recursos utilizados

- **Pandas** - manipulação e análise de dados
- **WeasyPrint** - geração de PDF's com base em HTML/CSS
- **Poetry 2.3.2** - gerenciador de dependências Python
- **Python 3.14** - linguagem base
- **Kaggle** - datasets reais para testes

## Funcionalidades

- Leitura de arquivos CSV com validação de caminho
- Sanitização automática: duplicatas, valores nulos, conversão de tipos
- Cálculo de métricas: receita, ticket médio, taxa de entrega, top categorias/marcas/países
- Geração de relatórios PDF com tabelas, gráficos e resumo financeiro
- Filtro por período (mês/ano)

## Executar o projeto

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/esales-report.git
cd esales-report
```

### 2. Instalar Poetry e dependências
```bash
curl -sSL https://install.python-poetry.org | python3 -
poetry --version   # verificar versão 2.3.2+
poetry install     # instala pandas e weasyprint
```

### 3. Executar a aplicação

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
├── poetry.lock
├── pyproject.toml
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
# Gerar relatório de janeiro de 2023
$ python src/main.py --month 1 --year 2023
✓ 15 registros carregados
✓ Métricas calculadas
✓ PDF gerado: /seu-diretorio/esales-report/shared/pdfs/relatorio_01_2023.pdf
```

## Contribuindo

Este é um projeto puramente para fins de aprendizado. Sinta-se livre para adaptar e utilizar conforme necessário.
