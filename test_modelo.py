import joblib
import pandas as pd
from sklearn.metrics import accuracy_score

def test_modelo_desempenho():
    # 1. Carrega o modelo exportado
    modelo = joblib.load('modelo_manutencao_bram.pkl')

    # 2. Cria um "Golden Dataset" com dados onde já sabemos a resposta correta
    # Usaremos exatamente os dados que testamos no Front-end
    dados_conhecidos = pd.DataFrame([
        # Cenário Normal (Gabarito: 0)
        {'Air temperature [K]': 298.1, 'Process temperature [K]': 308.6, 'Rotational speed [rpm]': 1551, 'Torque [Nm]': 42.8, 'Tool wear [min]': 15},
        # Cenário de Falha (Gabarito: 1)
        {'Air temperature [K]': 302.5, 'Process temperature [K]': 312.0, 'Rotational speed [rpm]': 1300, 'Torque [Nm]': 68.5, 'Tool wear [min]': 230}
    ])
    
    # O gabarito esperado para as duas linhas acima
    gabarito_esperado = [0, 1]

    # 3. Faz a predição usando o modelo
    predicoes = modelo.predict(dados_conhecidos)

    # 4. Calcula a métrica (Acurácia)
    acuracia = accuracy_score(gabarito_esperado, predicoes)

    # 5. O Teste (Assert): Verifica se a acurácia é de pelo menos 80% (0.80)
    limite_minimo_aceitavel = 0.80
    
    assert acuracia >= limite_minimo_aceitavel, f"Falha no teste de desempenho. Acurácia atual: {acuracia}"