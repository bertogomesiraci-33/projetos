"""Calculadora de consumo inteligente de energia
Entrada de dados"""
aparelho = input("Digite o nome do seu Aparelho: ")
potencia = float(input("Digite a potência do seu aparelho em watts (W): ").replace(',', '.'))
horas_dia = float(input("Digite o tempo médio de uso diário em horas (h): ").strip().replace(" ", "").replace(',', '.'))#6h30 min = 6.5
dias_no_mes = 30

#Valor fixo da tarifa de energia em reais por KWh
valor_kwh = 2.15

"""Processamento dos dados da calculadora 
Calculo do consumo mensal em KWh
Calculo do valor em R$"""

consumo_mensal = (potencia * horas_dia * dias_no_mes)/ 1000
custo_estimado = consumo_mensal * valor_kwh

"""Saída dos dados no Terminal
Consumo mensal"""
print("\n---Resultado do consumo mensal---")
print(f"\nAparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} KWh/mês")
print("\n---Resultado do custo estimado---")
print(f"Custo estimado: R$ {custo_estimado:.2f} mês")

# Estrutura de decisão para alerta de consumo
if consumo_mensal > 50:
    print("\n[ALERTA] Este aparelho possui um consumo elevado de energia!")
    print("Dica: Considere reduzir o tempo de uso diário.")
else:
    print("\n[INFO] Este aparelho possui um consumo dentro do padrão econômico.")


                  