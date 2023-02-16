# Python TST Reports

## Descrição

- Esse projeto é uma automação para rapagem e tratamento de dados dos cadernos semanais do Tribunal Superior do Trabalho. Sua implementação consiste em:

1. Baixar os cadernos do TST da última semana
2. Extrair os números de processo de cada caderno
3. Gerar planilhas de saída com todos os números de processos separados por dia da semana
  - Ex. TST 13/10/2022.xlsx
4. Caso um processo apareça repetido em mais de um dia, gerar relatório de duplicatas com os respectivos processos e suas datas.

- Fonte dos dados: https://dejt.jt.jus.br/dejt/f/n/diariocon