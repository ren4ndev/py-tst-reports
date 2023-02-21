# Python TST Reports

## Descrição

- Esse projeto é uma automação para rapagem e tratamento de dados dos cadernos semanais do Tribunal Superior do Trabalho. Sua implementação consiste em:

- [x] Baixar os cadernos do TST da última semana
- [x] Extrair os números de processo de cada caderno
- [x] Gerar planilhas de saída com todos os números de processos separados por dia da semana
  - Ex. TST 13/10/2022.xlsx
- [x] Caso um processo apareça repetido em mais de um dia, gerar relatório de duplicatas com os respectivos processos e suas datas.

- Fonte dos dados: https://dejt.jt.jus.br/dejt/f/n/diariocon

## Bibliotecas utilizadas

- Selenium
- Web Driver Manager
- PyMuPdf
- Pandas

## Setup

Para configurar o projeto na sua máquina e compilar o executável para Windows, siga os seguintes passos (PowerShell):

- Crie o ambiente virtual com o comando:
`python -m venv .venv`

- Ative o ambiente virtual com o comando:
`.venv\Scripts\\Activate.ps1`

- Instale as dependências:
`python -m pip install -r requirements.txt`

- Compile para um executável com o comando:
`pyinstaller main.py --onefile --noconsole`
