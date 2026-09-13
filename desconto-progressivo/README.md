# 🏷️ Sistema de Desconto Progressivo - Loja Online

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![VS Code](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)

Aplicação desenvolvida em **Python 3** para automatizar o cálculo de descontos progressivos em compras de comércio eletrônico, aplicando boas práticas de sanitização de entradas, operadores relacionais e programação estruturada.

---

## 🎯 Regras de Negócio e Descontos

O sistema avalia o valor total inserido e aplica a alíquota de desconto correspondente:

| Faixa de Valor da Compra (R$) | Alíquota (%) | Condição no Código |
| :--- | :---: | :--- |
| **Menor que R$ 200,00** | **5%** | `valor_compra < 200.00` |
| **De R$ 200,00 até R$ 299,99** | **10%** | `valor_compra >= 200.00 and valor_compra < 300.00` |
| **A partir de R$ 300,00** | **15%** | `else` (`valor_compra >= 300.00`) |

---

## ⚙️ Fluxo e Arquitetura do Programa

O algoritmo está estruturado em três fases distintas e comentadas:

1. **Entrada de Dados e Sanitização:**
   - Leitura do valor via terminal (`input()`).
   - Remoção de espaços acidentais com `.strip()`.
   - Conversão de vírgula decimal para ponto com `.replace(',', '.')`.
   - Conversão do tipo para ponto flutuante (`float`).

2. **Processamento (Lógica e Cálculos):**
   - Determinação do percentual de desconto utilizando estrutura condicional (`if/elif/else`).
   - Cálculo centralizado do valor do desconto e do saldo final a pagar, sem redundâncias.

3. **Saída Formatada:**
   - Exibição de cupom de resumo com alinhamento visual e valores monetários formatados em duas casas decimais (`:.2f`).

---

## 💻 Exemplo de Execução no Terminal

```text
===================================
  RESUMO DO DESCONTO PROGRESSIVO   
===================================
Valor original da compra: R$ 250.00
Desconto aplicado (10%):  R$ 25.00
-----------------------------------
Valor total a pagar:      R$ 225.00
===================================