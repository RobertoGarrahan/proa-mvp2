from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

# Inicializando a aplicação Flask
app = Flask(__name__)

# 1. Carregando o modelo (isso é feito fora das rotas para carregar apenas 1 vez ao iniciar o servidor)
# Como exportamos o Pipeline, o StandardScaler já está embutido aqui!
MODELO_PATH = 'modelo_manutencao_bram.pkl'
modelo = joblib.load(MODELO_PATH)

# 2. Rota para exibir a interface do usuário (Front-end)
@app.route('/')
def home():
    # O Flask vai procurar esse arquivo dentro da pasta 'templates'
    return render_template('index.html')

# 3. Rota da API que recebe os dados via método POST e retorna a predição
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Pegando os dados enviados pelo formulário do front-end (em formato JSON)
        dados = request.get_json()
        
        # Montando um DataFrame com os dados recebidos.
        # IMPORTANTE: O nome das colunas deve ser IDÊNTICO ao que foi usado no treino (X) no Colab
        df_entrada = pd.DataFrame([{
            'Air temperature [K]': float(dados['air_temperature']),
            'Process temperature [K]': float(dados['process_temperature']),
            'Rotational speed [rpm]': float(dados['rotational_speed']),
            'Torque [Nm]': float(dados['torque']),
            'Tool wear [min]': float(dados['tool_wear'])
        }])
        
        # Fazendo a predição usando o modelo carregado
        predicao = modelo.predict(df_entrada)[0]
        
        # Traduzindo o resultado matemático (0 ou 1) para o contexto de negócio da Bram
        if predicao == 1:
            status = "Risco de Falha Detectado! Manutenção Recomendada."
            classe_css = "danger" # Útil para pintar a tela de vermelho no front-end
        else:
            status = "Equipamento Operando Normalmente."
            classe_css = "success" # Útil para pintar a tela de verde no front-end
            
        # Retornando a resposta em formato JSON para o front-end
        return jsonify({
            'predicao': int(predicao),
            'mensagem': status,
            'classe_css': classe_css
        })
        
    except Exception as e:
        # Tratamento de erro básico caso falte algum dado ou seja enviado texto no lugar de número
        return jsonify({'erro': f'Erro ao processar a predição: {str(e)}'}), 400

# Iniciando o servidor local
if __name__ == '__main__':
    # debug=True permite que o servidor reinicie automaticamente se você alterar o código
    app.run(debug=True, host='0.0.0.0', port=5000)