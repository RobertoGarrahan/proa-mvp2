# 🚢 P.R.O.A - Plataforma de Risco e Operação de Ativos

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.8.0-F7931E?style=for-the-badge&logo=scikit-learn)
![Flask](https://img.shields.io/badge/Flask-3.1.3-black?style=for-the-badge&logo=flask)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.0-7952B3?style=for-the-badge&logo=bootstrap)

## 📌 Contexto do Projeto
Este projeto é o Produto Mínimo Viável (MVP) desenvolvido para a disciplina de **Engenharia de Software para Sistemas Inteligentes**. 

Ele simula um sistema de suporte à decisão aplicado à realidade do **Mercado Offshore**, focado na **Manutenção Preditiva** de ativos navais (como propulsores e motores). O objetivo é prever falhas mecânicas com base em dados de telemetria de sensores, reduzindo o *downtime* (tempo de inatividade) da frota e aumentando a segurança operacional.

## ⚙️ Funcionalidades
- **Cérebro de IA:** Treinamento, validação e otimização de algoritmos clássicos de Machine Learning (KNN, Naive Bayes, SVM e Árvore de Decisão).
- **Prevenção de Data Leakage:** Uso intensivo de `Pipelines` do Scikit-Learn para garantir a correta padronização dos dados (`StandardScaler`).
- **API Rest (Back-end):** Aplicação servida via **Flask** que embarca o modelo preditivo otimizado (`.pkl`) na memória e expõe uma rota `/predict`.
- **Interface Web (Front-end):** Dashboard responsivo construído com **HTML, JS e Bootstrap 5**, permitindo a entrada de dados dos sensores e o retorno em tempo real do status do equipamento.
- **Testes Automatizados:** Cobertura de testes de desempenho com **PyTest** para garantir a confiabilidade da IA.

## 📂 Estrutura do Repositório
```text
/
├── MVP2.ipynb                           # Notebook de Data Science (Treino e Otimização da IA)
├── modelo_manutencao_bram.pkl           # Modelo serializado otimizado (Pipeline + Árvore)
├── app.py                               # Back-end em Python/Flask
├── test_modelo.py                       # Testes automatizados de métricas do modelo
└── templates/
    └── index.html                       # Front-end do sistema (Dashboard PROA)
````

## 🚀 Como Executar o Projeto Localmente
### 1. Pré-requisitos

Certifique-se de ter o Python 3.x instalado. Clone este repositório e navegue até a pasta do projeto.

### 2. Instalação das Dependências

Abra o terminal na raiz do projeto e instale as bibliotecas necessárias:
```Bash
pip install flask scikit-learn pandas joblib pytest
```

### 3. Rodando os Testes Automatizados (PyTest)

Para verificar se o modelo atende aos requisitos mínimos de desempenho (acurácia > 80%):
```Bash
pytest test_modelo.py
```

### 4. Iniciando a Aplicação Full Stack

Para iniciar o servidor Flask que conecta o modelo à interface:
```Bash
python app.py
```

O terminal exibirá o endereço local (geralmente http://127.0.0.1:5000). Acesse este link em seu navegador para utilizar o painel de diagnóstico.
🔒 Segurança e Boas Práticas (LGPD)

No contexto offshore, a telemetria pode, por vezes, estar atrelada a identificadores de tripulantes ou à localização de embarcações de alto valor. Seguindo as boas práticas de Desenvolvimento de Software Seguro e LGPD, simula-se a aplicação de anonimização e hashing de dados sensíveis na camada de pré-processamento, garantindo que o modelo aprenda exclusivamente os padrões mecânicos de falha, mitigando riscos de exposição de dados. Além disso, o back-end processa os inputs sanitizados para evitar injeções oriundas do front-end.

Autor: Roberto Garrahan

Pós-Graduação PUC - Engenharia de Software
