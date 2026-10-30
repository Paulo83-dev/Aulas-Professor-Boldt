# 🧠 Reconhecimento de Padrões & Machine Learning

Bem-vindo(a) ao repositório de estudos práticos de **Reconhecimento de Padrões e Aprendizado de Máquina (Machine Learning)**, baseado nas aulas ministradas pelo **Prof. Dr. Francisco de Assis Boldt**.

Este repositório foi totalmente estruturado e enriquecido pedagogicamente para transformar códigos brutos de aula em um **guia didático interativo passo a passo**, ideal para quem está começando do zero em programação e inteligência artificial.

---

## 🎯 Filosofia Pedagógica do Curso: *"Do Zero ao Scikit-Learn"*

A abordagem das aulas segue um princípio metodológico fundamental:
1. **Desmistificar a Caixa-Preta**: Quase nunca usamos uma função pronta de biblioteca de primeira. Construímos primeiro a intuição lógica e matemática "na mão" com **NumPy** (cálculo de erros, derivadas/gradiente, distância euclidiana, normalização, validação cruzada).
2. **Entender o "Porquê"**: Descobrir na prática os problemas reais (como escalas desiguais de dados ou vazamento de informação entre treino e teste).
3. **Padrão Profissional com Scikit-Learn**: Somente após entender como as engrenagens funcionam por dentro é que adotamos as ferramentas oficiais da biblioteca `scikit-learn`.

---

## 🗺️ Trilha de Aprendizado (Índice dos Cadernos)

Os notebooks estão organizados em uma sequência evolutiva contínua:

### 📘 Fase 1: Fundamentos de Regressão e Otimização
* **[aula01a_regressão_linear.ipynb](aula01a_regressão_linear.ipynb)**
  * **Problema Real**: Previsão do preço de imóveis na Califórnia (*California Housing Dataset*).
  * **Conceitos**:
    * Divisão em Treino e Teste artesanal (para evitar sobreajuste / decorar a prova).
    * Modelos base (*baselines*): chutar a média ou chutar valores aleatórios.
    * Métricas de erro: por que o erro médio simples anula sinais e como usar **MAE**, **MSE** e **RMSE**.
    * A equação da reta ($y = w \cdot X + b$) e ajuste manual de coeficientes.
    * Implementação da **Descida do Gradiente** do zero em uma classe compatível com o Scikit-Learn.
    * A importância da **Padronização Z-Score** para permitir a convergência do algoritmo.
    * Solução analítica exata via **Equação Normal / Pseudo-Inversa** (`np.linalg.pinv`).
    * Comparação final com o modelo `LinearRegression()` oficial.

---

### 📘 Fase 2: Classificação e Modelos Baseados em Distância
* **[aula02a_classificador_linear_binário.ipynb](aula02a_classificador_linear_binário.ipynb)**
  * **Problema Real**: Diagnóstico de câncer de mama (Maligno = 0 vs Benigno = 1).
  * **Conceitos**:
    * Transição de prever números contínuos para prever decisões binárias.
    * O **truque do limiar (threshold em 0.5)** para transformar uma reta de regressão em classificador.
    * A métrica de **Acurácia** (porcentagem de acertos).
    * Comparação da curva suave do MSE com a curva em escada da acurácia (por que não podemos otimizar acurácia diretamente via gradiente).

* **[aula02b_classificador_linear_multiclasse.ipynb](aula02b_classificador_linear_multiclasse.ipynb)**
  * **Problema Real**: Classificação de 3 tipos de vinhos italianos (*Wine Dataset*).
  * **Conceitos**:
    * Por que não podemos prever classes 0, 1 e 2 em uma única saída (falsa ordem numérica).
    * **One-Hot Encoding** artesanal com NumPy.
    * Matriz de pesos multi-saída ($W$) onde cada coluna pontua uma classe.
    * Regra de decisão por votação máxima via `np.argmax`.

* **[aula02c - classificador de vizinhança.ipynb](aula02c%20-%20classificador%20de%20vizinhança.ipynb)**
  * **Problema Real**: Classificação por proximidade física com o algoritmo **k-NN**.
  * **Conceitos**:
    * Aprendizado baseado em instâncias (*"diga-me com quem andas e te direi quem és"*).
    * Implementação do **1-NN do zero** usando a distância euclidiana (**Teorema de Pitágoras**).
    * **A Armadilha Fatal das Escalas**: Como uma característica que varia de 0 a 1600 neutraliza totalmente uma que varia de 0 a 0.5.
    * As duas grandes formas de escalonamento: **Min-Max (0 a 1)** e **StandardScaler (Z-Score)**.
    * Votação majoritária com múltiplos vizinhos ($k=15$) no `KNeighborsClassifier`.

---

### 📘 Fase 3: Metodologia Científica e Otimização de Modelos
* **[aula03a - validação cruzada.ipynb](aula03a%20-%20validação%20cruzada.ipynb)**
  * **Problema Real**: Como ter certeza de que o modelo generaliza bem e não demos apenas sorte no sorteio dos dados.
  * **Conceitos**:
    * A fragilidade do sorteio único treino/teste: oscilações de acurácia por pura casualidade.
    * **Validação Cruzada K-Fold artesanal**: fatiamento em $K$ pedaços onde cada amostra é testada honestamente uma vez.
    * O perigo mortal do **Vazamento de Dados (Data Leakage)** ao calcular médias antes de separar os dados.
    * Construção de um **`CustomPipeline` do zero** para blindar transformações dentro do treino.
    * Por que o `KFold` exige `shuffle=True` quando os dados estão ordenados por classe.
    * Ferramentas profissionais: `make_pipeline`, `LeaveOneOut` e `RepeatedKFold`.

* **[aula03b - gridsearch.ipynb](aula03b%20-%20gridsearch.ipynb)**
  * **Problema Real**: Como encontrar automaticamente o melhor valor de $k$ e os melhores parâmetros do modelo.
  * **Conceitos**:
    * Parâmetros (pesos que a máquina aprende) vs Hiperparâmetros (configurações que nós calibramos).
    * Conjunto de Validação Interna (Treino, Validação e Teste).
    * O erro sutil: *"Não é a melhor forma. Não mesmo!"*.
    * Busca em grade automatizada com `GridSearchCV`.
    * Integração de `Pipeline` com `GridSearchCV` usando a sintaxe `etapa__parametro`.
    * **Validação Cruzada Aninhada (Nested CV)**: o padrão-ouro da literatura científica para estimar a acurácia real do sistema.

---

## 🛠️ Como Configurar o Ambiente de Execução

### Pré-requisitos
* **Python 3.12+** instalado na máquina.
* As seguintes bibliotecas de Python:
  ```bash
  pip install numpy pandas scikit-learn matplotlib seaborn ipykernel
  ```

### Como Executar os Notebooks no VS Code / Antigravity IDE:
1. Abra a pasta do projeto no editor.
2. Abra qualquer um dos arquivos `.ipynb`.
3. No canto superior direito da janela do caderno, clique em **"Selecione Kernel"** (ou *Select Kernel*).
4. Escolha **"Python Environments..."** e selecione o seu interpretador **Python 3.12**.
5. Clique no botão de play (**▶️**) ao lado de cada célula para executar o código passo a passo.

---

## 💡 Dicas de Estudo para Iniciantes
1. **Leia a teoria antes do código**: Cada bloco tem uma explicação em texto azul/itálico contextualizando a lógica.
2. **Brinque com os números**: Altere taxas de aprendizado, mude a semente aleatória, aumente ou diminua o número de vizinhos ($k$) e veja o comportamento do modelo mudar na prática.
3. **Não decore código**: Foque em compreender o fluxo dos dados: como a matriz entra, que transformação matemática é aplicada e como a resposta final é produzida.

---

## 👨‍🏫 Créditos e Autoria

* **Autor Original das Aulas e Códigos**: **Prof. Dr. Francisco de Assis Boldt**
  * Perfil no GitHub: [@fboldt](https://github.com/fboldt)
  * Repositório Upstream Oficial: [fboldt/aulasml](https://github.com/fboldt/aulasml)
* **Enriquecimento Didático e Curadoria**: **Paulo Fernando** ([@Paulo83-dev](https://github.com/Paulo83-dev))
* **Metodologia de Enriquecimento**: Estruturado com explicações detalhadas, intuição pedagógica e documentação linha a linha desenvolvida com a skill de IA `enrich-ml-notebooks`.
