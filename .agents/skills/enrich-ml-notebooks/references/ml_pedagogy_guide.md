# 📖 Guia de Padrões Pedagógicos para Aulas de Machine Learning

Este guia serve de referência para o agente ao interpretar cadernos de códigos de Machine Learning e Reconhecimento de Padrões.

---

## 1. Padrões de Regressão
* **Baselines (Modelos de Referência)**:
  * `average_predictor`: Chute pela média ($\bar{y}$).
  * `random_predictor`: Sorteio uniforme entre $\min(y)$ e $\max(y)$.
  * *Objetivo pedagógico*: Demonstrar que um modelo precisa ser melhor do que um chute ingênuo.
* **Métricas de Erro**:
  * *Erro Médio Simples*: Mostra o cancelamento de erros positivos e negativos.
  * *MAE*: Erro absoluto na unidade real, sem penalizar desproporcionalmente desvios grandes.
  * *MSE*: Erro quadrático, função convexa e suave essencial para derivadas na Descida do Gradiente.
  * *RMSE*: Raiz quadrada do MSE, devolvendo o erro para a escala original de medida.
* **Otimização**:
  * *Descida do Gradiente*: Atualização iterativa $w \leftarrow w + \alpha \cdot \text{gradiente}$. Explicar taxa de aprendizado ($\alpha$) e número de iterações.
  * *Solução Analítica (Equação Normal)*: $w = (X^T X)^{-1} X^T y$ com pseudo-inversa (`np.linalg.pinv`).

---

## 2. Padrões de Classificação
* **Binária vs Multiclasse**:
  * *Binária*: Uso de limiar (*threshold*) em $0.5$ para transformar saídas contínuas em $0$ ou $1$.
  * *Multiclasse*: Necessidade de **One-Hot Encoding** para não criar falsa relação de ordem matemática ($0 < 1 < 2$), matriz de pesos multi-saída e seleção da classe com `np.argmax`.
* **Métrica de Acurácia**:
  * Total de acertos dividido pelo total de amostras.
  * Demonstrar por que a acurácia tem formato de "escada" (degraus) e não pode ser otimizada diretamente por gradiente.

---

## 3. Padrões de Algoritmos Baseados em Distância (k-NN)
* **Distância Euclidiana**: Teorema de Pitágoras multidimensional $\sqrt{\sum (x_i - y_i)^2}$.
* **Armadilha das Escalas**:
  * Se uma coluna varia de 0 a 1000 e outra de 0 a 1, a primeira domina $100\%$ da distância.
  * *Min-Max*: Coloca tudo entre $0$ e $1$.
  * *StandardScaler (Z-Score)*: Centraliza em média $0$ e desvio $1$, ideal para lidar com outliers.
* **Votação por Maioria ($k > 1$)**: Reduz sensibilidade a ruídos em comparação com $k=1$.

---

## 4. Metodologia Científica e Rigor
* **Vazamento de Dados (Data Leakage)**:
  * O pré-processamento (médias, desvios, escalas, imputações) deve ser calculado **estritamente dentro do conjunto de treino**.
  * Aplicar transformadores antes da divisão contamina o teste com informação do futuro.
* **Pipelines**:
  * Encapsula `StandardScaler()` + `Estimator()` para automatizar `fit_transform` no treino e `transform` no teste.
* **Validação Cruzada (K-Fold)**:
  * Garante que todas as amostras passem pelo teste uma vez.
  * Sempre usar `shuffle=True` quando os dados vêm agrupados/ordenados por classe.
* **GridSearchCV & Nested CV**:
  * Parâmetro (pesos internos aprendidos) vs Hiperparâmetro (escolhidos antes do treino, ex: $k$).
  * Validação Cruzada Aninhada (Nested CV): Avaliação imparcial de todo o processo de seleção de modelos.
