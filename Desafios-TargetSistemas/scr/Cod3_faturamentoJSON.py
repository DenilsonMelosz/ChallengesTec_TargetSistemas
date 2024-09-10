import json
import os

def read_json_file(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    return data

def processando(data):
    numbers = [element.get('valor', 0) for element in data]
    if not numbers:
        raise ValueError("Nenhum dado encontrado para processar.")

    high = max(numbers)
    positive_numbers = [number for number in numbers if number > 0]
    low = min(positive_numbers) if positive_numbers else 0
    total_sum = sum(numbers)
    average = total_sum / len(numbers) if numbers else 0
    greater_average = [number for number in numbers if number > average]

    # Formatar números no estilo pt-BR
    normalize_numbers = lambda x: f"R$ {x:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    formatted_high = normalize_numbers(high)
    formatted_low = normalize_numbers(low)
    formatted_total_sum = normalize_numbers(total_sum)
    formatted_average = normalize_numbers(average)

    return {
        'total': formatted_total_sum,
        'high': formatted_high,
        'low': formatted_low,
        'score_med': len(greater_average)
    }

def main():
    file_path = r'C:\Users\denilson.souza\Desktop\ProcessoSeletivo-TargetSistema\scr\dados.json'
    
    try:
        data = read_json_file(file_path)
        results = processando(data)

        print(f"Total vendido: {results['total']}")
        print(f"O maior valor de faturamento: {results['highest']}")
        print(f"Menor valor de faturamento: {results['low']}")
        print(f"Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {results['score_med']}")
    
    except (FileNotFoundError, ValueError) as e:
        print(f"Erro: {e}")

if __name__ == '__main__':
    main()
