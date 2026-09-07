# ⚡ Calculadora de Consumo Elétrico Inteligente

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)
![Git](https://img.shields.io/badge/Git-Versionado-orange?logo=git)
![GitHub](https://img.shields.io/badge/GitHub-Publicado-lightgrey?logo=github)

Projeto desenvolvido para cálculo e análise do consumo de energia elétrica de eletrodomésticos, permitindo estimar o impacto financeiro mensal na conta de luz e emitir alertas de eficiência energética com base em estruturas condicionais.

---

## 📌 Funcionalidades

- **Sanitização de Dados:** Tratamento de entradas do usuário com `.strip()` para remoção de espaços extras e `.replace(',', '.')` para suporte a números com vírgula ou ponto.
- **Cálculo de Consumo:** Conversão da potência do aparelho (Watts) e horas diárias de uso em consumo diário e mensal em quilowatts-hora ($kWh$).
- **Custo Estimado:** Cálculo financeiro mensal em Reais ($R\$$) a partir do valor da tarifa da distribuidora.
- **Estrutura de Decisão (`if/else`):** Análise automática que emite um alerta caso o consumo mensal do aparelho ultrapasse o limite estipulado (50 kWh/mês).

---

## 🧮 Fórmulas Matemáticas Utilizadas

1. **Consumo Diário:**
   $$\text{Consumo Diário (kWh)} = \frac{\text{Potência (W)} \times \text{Horas/Dia}}{1000}$$

2. **Consumo Mensal:**
   $$\text{Consumo Mensal (kWh)} = \text{Consumo Diário (kWh)} \times \text{Dias de Uso no Mês}$$

3. **Custo Estimado:**
   $$\text{Custo Mensal (R\$)} = \text{Consumo Mensal (kWh)} \times \text{Tarifa (R\$/kWh)}$$

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
- Ter o **Python 3** instalado em sua máquina.
- Ter o **Git** instalado.

### Passo a Passo
1. Clone o repositório em sua máquina:
   ```bash
   git clone [https://github.com/bertogomesiraci-33/projetos.git](https://github.com/bertogomesiraci-33/projetos.git)