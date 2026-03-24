# Sheets Report
Geração de relatórios mensais em PDF com base em planilhas de dados CSV.

## Objetivo
Simular um cenário real de processamentos de dados por meio de um workflow de: scrap, análise, processamento, geração --- transformando dados brutos em relatórios úteis para tomadas de decisões.

## Tecnologias, ferramentas e recursos utilizados
- kaggle.com/datasets - plataforma com datasets reais utilizados no processamento
- Pandas - biblioteca de manipulação e análise de dados
- WeasyPrint - gera PDF's com base em arquivos HTML
- Poetry 2.3.2 - gerenciador de dependências em python
- Python 3.14

## Funcionalidades
- Leitura de dados de arquivos CSV;
- Sanitização e tratamento dos dados;
- Calculo de métricas;
- Geração de relatórios PDF's otimizados.

## Exemplo de métricas (em construção...)


## Executar o projeto
### 1. Clone o repositório
```bash
    git clone https://github.com/seu-usuario/sheets-report.git
    cd sheets-report
```

### 2. Instalar o poetry e dependências do projeto
```bash
    curl -sSL https://install.python-poetry.org | python3 -
    poetry --version   # deve mostrar 2.3.2 ou superior

    poetry install # instala pandas e wasyprint
```

## Estrutura do projeto (em construção...)


Este é um projeto puramente para fins de aprendizado, sinta-se livre para contribuir!