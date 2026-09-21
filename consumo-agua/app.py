def main():
    print("="*50)
    print("  SISTEMA DE CLASSIFICAÇÃO DE CONSUMO DE ÁGUA  ")
    print("="*50)
    
    tipo_imovel = input("Digite o tipo de imóvel (comercial, casa, apartamento): ").strip().lower()
    
    try:
        consumo = float(input("Digite o consumo mensal de água (em m³): ").replace(",", "."))
    except ValueError:
        print("Valor inválido. Por favor, digite um número para o consumo.")
        return

    print("\n--- RESULTADO DA AVALIAÇÃO ---")
    
    # 1. Uso do operador relacional de igualdade (==)
    if tipo_imovel == "comercial":
        print("Tarifa comercial aplicada – consulte o plano corporativo.")
        
    # 2. Uso do operador lógico 'and' e relacional menor (<)
    elif (tipo_imovel == "apartamento") and (consumo < 10):
        print("Consumo econômico – excelente controle de água!")
        
    # 3. Uso dos operadores lógicos 'or' e 'and', e relacional menor ou igual (<=)
    elif (tipo_imovel == "apartamento" or tipo_imovel == "casa") and (consumo <= 25):
        print("Consumo moderado – dentro do padrão residencial.")
        
    # 4. Qualquer outra condição cai no else
    else:
        print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")
        
    print("="*50)

if __name__ == "__main__":
    main()
