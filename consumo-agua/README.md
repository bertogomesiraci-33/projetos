# 💧 Sistema de Classificação de Consumo de Água

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)
![Ambiente](https://img.shields.io/badge/Meio_Ambiente-Preservação-2ea44f?style=for-the-badge&logo=dependabot&logoColor=white)

## 🎯 Objetivo do Projeto
Este projeto foi desenvolvido como parte de uma campanha de conscientização ambiental da companhia de saneamento. O sistema em Python classifica o perfil de consumo de água dos imóveis e emite alertas educativos automáticos para os moradores, ajudando na economia e prevenção de vazamentos.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3
* **Estrutura:** Operadores Relacionais (`==`, `<`, `<=`) e Lógicos (`and`, `or`)
* **Controle de Versão:** Git e GitHub

## 📝 Regras de Negócio Implementadas
O programa avalia o consumo (em m³) com base no tipo de imóvel:
1. **Comercial:** Tarifa comercial aplicada.
2. **Apartamento (< 10 m³):** Consumo econômico.
3. **Casa ou Apartamento (até 25 m³):** Consumo moderado.
4. **Outros:** Consumo excessivo (alerta de vazamento).

## 🚀 Como Executar o Programa

1. Certifique-se de ter o [Python](https://www.python.org/) instalado em seu computador.
2. Abra o terminal (Prompt de Comando ou PowerShell).
3. Navegue até a pasta do projeto.
4. Execute o seguinte comando:

```bash
python app.py