"""
Programa de desconto progressivo
Aplicar descontos progressivos de acordo com o valor total da compra

Regras de descontos
- Valor total da compra for menor do que R$ 200,00 
o cliente recebe um desconto 5%
- Valor total da compra for maior ou igual a R$ 200,00 e menor que R$ 300,00,
o cliente recebe um desconto de 10%
- Valor total da compra for maior ou igual a R$ 300,00
o cliente recebe um desconto de 15% 
"""

#======================================================
# 1. ENTRADA DE DADOS E SANITIZAÇÃO
#======================================================
#strip() remove espaços vazios acidentais e replace(',', '.')permite o uso da vírgula decimal.
#Solicita o valor total da compra ao usuário:
valor_compra = float(input("usuário, digite o valor total da compra (R$): ").strip().replace(',', '.'))

#======================================================
# 2. PROCESSAMENTO E LÓGICA RELACIONAL E CÁLCULOS
#======================================================
# AVALIA A FAIXA DE COMPRA PARA APLICAÇÃO DO DESCONTO
if valor_compra < 200.00:
    percentual_desconto = 0.05
elif valor_compra >= 200.00 and valor_compra < 300.00:
    percentual_desconto = 0.10
else:
    percentual_desconto = 0.15
    
#Realiza os cálculos de acordo com o percentual obtido
desconto = valor_compra * percentual_desconto
valor_final = valor_compra - desconto

#=====================================================
# 3. SAÍDA DOS DADOS - RESUMO VALORES FINAIS
#=====================================================
print("\n" + "=" *35)
print("\n---Resumo do desconto progressivo ---")
print("=" * 35)
print(f"Valor original da compra: R$ {valor_compra:.2f}")
print(f"Desconto aplicado ({int(percentual_desconto *100)}%): R$ {desconto:.2f}")
print(f"Valor total da compra: R$ {valor_final:.2f}")
print("=" * 35)





    


