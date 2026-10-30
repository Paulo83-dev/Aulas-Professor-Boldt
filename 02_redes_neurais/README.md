# Programa Completo: Disciplina de Redes Neurais Artificiais (ANN)
## 15 Semanas | 45 Horas | Mestrado/Doutorado em Computação
**Professor**: Prof. Dr. Francisco de Assis Boldt | **Material Prático Enriquecido Didaticamente**

---

## 🚀 Cadernos Práticos Enriquecidos (Laboratório Passo a Passo)

Todos os cadernos práticos do curso foram enriquecidos segundo as diretrizes pedagógicas da skill `enrich-ml-notebooks`. Cada caderno preserva integralmente a lógica e o código do professor, com a adição de:
- Cabeçalhos conceituais, objetivos e intuição teórica;
- Explicação do "porquê" antes de cada bloco de código;
- Código 100% comentado linha a linha;
- Callouts conceituais (`> [!NOTE]`, `> [!TIP]`, `> [!IMPORTANT]`);
- Resumos de consolidação ao final de cada aula.

### 📦 Lote 1: Fundamentos Lineares (Perceptron & Adaline)
1. [Aula 01a: Perceptron Learning Algorithm](file:///c:/Users/paulo/OneDrive/%C3%81rea%20de%20Trabalho/Cursos%20e%20Educa%C3%A7%C3%A3o/AULAS%20DO%20BOLDT/02_redes_neurais/aula01a_perceptron_learning_algorithm.ipynb) — Rosenblatt (1958), hiperplano separador e regra clássica.
2. [Aula 02a: Perceptron com Bias](file:///c:/Users/paulo/OneDrive/%C3%81rea%20de%20Trabalho/Cursos%20e%20Educa%C3%A7%C3%A3o/AULAS%20DO%20BOLDT/02_redes_neurais/aula02a%20perceptron%20learning%20algorithm%20with%20bias.ipynb) — Inclusão do termo independente de deslocamento.
3. [Aula 02b: Perceptron Vetorial](file:///c:/Users/paulo/OneDrive/%C3%81rea%20de%20Trabalho/Cursos%20e%20Educa%C3%A7%C3%A3o/AULAS%20DO%20BOLDT/02_redes_neurais/aula02b%20perceptron%20vetorial.ipynb) — Vetorização em NumPy ($w^T x$) de alta performance.
4. [Aula 02c: Regressão Linear com Neurônio](file:///c:/Users/paulo/OneDrive/%C3%81rea%20de%20Trabalho/Cursos%20e%20Educa%C3%A7%C3%A3o/AULAS%20DO%20BOLDT/02_redes_neurais/aula02c%20linear%20regression.ipynb) — O neurônio como preditor de variáveis contínuas.
5. [Aula 02d: Equação Normal](file:///c:/Users/paulo/OneDrive/%C3%81rea%20de%20Trabalho/Cursos%20e%20Educa%C3%A7%C3%A3o/AULAS%20DO%20BOLDT/02_redes_neurais/aula02d%20normal%20equation.ipynb) — Solução analítica matricial exata via Mínimos Quadrados.
6. [Aula 02e: Adaline com Equação Normal](file:///c:/Users/paulo/OneDrive/%C3%81rea%20de%20Trabalho/Cursos%20e%20Educa%C3%A7%C3%A3o/AULAS%20DO%20BOLDT/02_redes_neurais/aula02e%20adaline%20with%20normal%20equation.ipynb) — Neurônio Adaline (Widrow-Hoff) e ativação puramente linear.
7. [Aula 02f: Adaline com SGD](file:///c:/Users/paulo/OneDrive/%C3%81rea%20de%20Trabalho/Cursos%20e%20Educa%C3%A7%C3%A3o/AULAS%20DO%20BOLDT/02_redes_neurais/aula02f%20adaline%20with%20SGD.ipynb) — Gradiente descendente estocástico e análise de sensibilidade a outliers.

### 📦 Lote 2: Otimização, Multiclasse & O Paradoxo do XOR
8. [Aula 03a: Padrão Strategy para Otimizadores](file:///c:/Users/paulo/OneDrive/%C3%81rea%20de%20Trabalho/Cursos%20e%20Educa%C3%A7%C3%A3o/AULAS%20DO%20BOLDT/02_redes_neurais/aula03a_algorithms.ipynb) — Desacoplamento arquitetural entre modelo preditivo e algoritmo de otimização.
9. [Aula 03b: Funções de Custo Comparadas](file:///c:/Users/paulo/OneDrive/%C3%81rea%20de%20Trabalho/Cursos%20e%20Educa%C3%A7%C3%A3o/AULAS%20DO%20BOLDT/02_redes_neurais/aula03b%20-%20cost%20functions.ipynb) — Análise aprofundada de MSE, Sigmoide, Tanh e Hinge Loss.
10. [Aula 03c: Classificação Multiclasse](file:///c:/Users/paulo/OneDrive/%C3%81rea%20de%20Trabalho/Cursos%20e%20Educa%C3%A7%C3%A3o/AULAS%20DO%20BOLDT/02_redes_neurais/aula03c_multiclasse.ipynb) — Matrizes de pesos bidimensionais ($W$) e decodificação Argmax.
11. [Aula 03d: A Crise Histórica do XOR](file:///c:/Users/paulo/OneDrive/%C3%81rea%20de%20Trabalho/Cursos%20e%20Educa%C3%A7%C3%A3o/AULAS%20DO%20BOLDT/02_redes_neurais/aula03d%20-%20XOR.ipynb) — Portas OR, AND e a prova de não-separabilidade de Minsky & Papert (1969).

### 📦 Lote 3: Não-Linearidades Suaves & ELM
12. [Aula 04a: Funções de Custo Diferenciáveis](file:///c:/Users/paulo/OneDrive/%C3%81rea%20de%20Trabalho/Cursos%20e%20Educa%C3%A7%C3%A3o/AULAS%20DO%20BOLDT/02_redes_neurais/aula04a_cost_functions.ipynb) — Derivação matemática explícita dos gradientes.
13. [Aula 04c: Superando o XOR com Camada Oculta](file:///c:/Users/paulo/OneDrive/%C3%81rea%20de%20Trabalho/Cursos%20e%20Educa%C3%A7%C3%A3o/AULAS%20DO%20BOLDT/02_redes_neurais/aula04c%20-%20XOR%20classifier.ipynb) — Projeção no espaço latente $H$ com 2 neurônios ocultos.
14. [Aula 04d: Ativação Tangente Hiperbólica ($tanh$)](file:///c:/Users/paulo/OneDrive/%C3%81rea%20de%20Trabalho/Cursos%20e%20Educa%C3%A7%C3%A3o/AULAS%20DO%20BOLDT/02_redes_neurais/aula04d%20-%20XOR%20tanh.ipynb) — Dinâmica suave e centrada em zero com derivada $1 - \tanh^2(z)$.
15. [Aula 04e: Extreme Learning Machine (ELM)](file:///c:/Users/paulo/OneDrive/%C3%81rea%20de%20Trabalho/Cursos%20e%20Educa%C3%A7%C3%A3o/AULAS%20DO%20BOLDT/02_redes_neurais/aula04e%20-%20ELM.ipynb) — Pesos ocultos aleatórios fixos e treino ultrarrápido via Equação Normal.

### 📦 Lote 4: Multilayer Perceptron (MLP) do Zero em NumPy
16. [Aula 05a: Backpropagation na Última Camada](file:///c:/Users/paulo/OneDrive/%C3%81rea%20de%20Trabalho/Cursos%20e%20Educa%C3%A7%C3%A3o/AULAS%20DO%20BOLDT/02_redes_neurais/aula05a_Last_Layer.ipynb) — Gradiente do erro e atualização da camada de saída.
17. [Aula 05b: MLP com Camada Oculta Única](file:///c:/Users/paulo/OneDrive/%C3%81rea%20de%20Trabalho/Cursos%20e%20Educa%C3%A7%C3%A3o/AULAS%20DO%20BOLDT/02_redes_neurais/aula05b%20-%20Single%20Hidden%20Layer.ipynb) — Retropropagação do erro através da camada oculta ($H \rightarrow X$).
18. [Aula 05c: MLP Arbitrário de N Camadas](file:///c:/Users/paulo/OneDrive/%C3%81rea%20de%20Trabalho/Cursos%20e%20Educa%C3%A7%C3%A3o/AULAS%20DO%20BOLDT/02_redes_neurais/aula05c%20-%20Multi%20Layer.ipynb) — Forward e backward genéricos para qualquer topologia profunda.
19. [Aula 05d: MLP Multiclasse com Camadas Densas](file:///c:/Users/paulo/OneDrive/%C3%81rea%20de%20Trabalho/Cursos%20e%20Educa%C3%A7%C3%A3o/AULAS%20DO%20BOLDT/02_redes_neurais/aula05d%20-%20Multi%20Classe.ipynb) — Classificação com múltiplos neurônios de saída.
20. [Aula 05e: MLP Aplicado ao Dataset Iris](file:///c:/Users/paulo/OneDrive/%C3%81rea%20de%20Trabalho/Cursos%20e%20Educa%C3%A7%C3%A3o/AULAS%20DO%20BOLDT/02_redes_neurais/aula05e%20-%20MLP%20Iris.ipynb) — Aplicação prática completa com fronteiras de decisão e convergência.

### 📦 Lote 5: Deep Learning Moderno com PyTorch
21. [Aula 06a: PyTorch, Autograd e Módulos Neurais](file:///c:/Users/paulo/OneDrive/%C3%81rea%20de%20Trabalho/Cursos%20e%20Educa%C3%A7%C3%A3o/AULAS%20DO%20BOLDT/02_redes_neurais/aula06a_pytorch.ipynb) — Diferenciação automática, Adam, ReLU, classificação de dígitos manuscritos e contagem analítica de parâmetros.

---

> [!NOTE]
> Abaixo segue a ementa curricular e o programa teórico oficial de 15 semanas da disciplina.

---

## **SEMANA 1 — Perceptron e Aprendizado Supervisionado**

### Estrutura da Aula (3 horas)
- **0:00–0:45**: Neurônio de McCulloch & Pitts, Perceptron de Rosenblatt
- **0:45–0:55**: *Intervalo 1*
- **0:55–1:45**: Regra de atualização via gradiente, ativação e convergência
- **1:45–1:55**: *Intervalo 2*
- **1:55–2:50**: Linearidade, separabilidade e laboratório
- **2:50–3:00**: Fechamento

### Conteúdo Detalhado

#### Bloco 1: História e Formulação (45 min)
- **Contextualização histórica**
  - 1943: McCulloch & Pitts – neurônio binário lógico
  - 1958: Rosenblatt – Perceptron Mark I

- **Modelo matemático**
  - y = f(wᵀx + b)
  - Função de ativação sinal: y = sign(wᵀx)
  - Interpretação geométrica como hiperplano separador

- **Interpretação geométrica**
  - Comparação com regressão linear
  - Exemplo visual em 2D
  - Noção de hipótese linear separável

#### Bloco 2: Regra de Atualização (50 min)
- **Função de perda e atualização**
  - w ← w + η(y - ŷ)x
  - Interpretação como descida de gradiente estocástica

- **Propriedades e Convergência**
  - Teorema de convergência de Rosenblatt
  - Falhas em dados não separáveis

- **Ativação, bias e derivação moderna**
  - Inclusão de bias como entrada constante
  - Transição para perceptrons com funções suaves

#### Bloco 3: Laboratório (55 min)
- **Comparação conceitual**: Perceptron vs. SVM linear
- **Limitações**: XOR e motivação para MLPs
- **Laboratório prático**: Implementação do zero em NumPy

**Leituras**: Aggarwal (2018) Cap. 1, Weidman (2019) Cap. 1

---

## **SEMANA 2 — MLP, Ativações e Backpropagation**

### Estrutura da Aula (3 horas)
- **0:00–0:45**: Redes multicamadas e funções compostas
- **0:45–0:55**: *Intervalo 1*
- **0:55–1:40**: Funções de ativação e suas derivadas
- **1:40–1:50**: *Intervalo 2*
- **1:50–2:50**: Backpropagation completo e laboratório
- **2:50–3:00**: Fechamento

### Conteúdo Detalhado

#### Bloco 1: Arquitetura MLP (45 min)
- **Limitações do perceptron**: problema XOR
- **Definição de MLP**: y = fₗ(... f₂(f₁(x)))
- **Teorema da universalidade**: aproximação de funções contínuas
- **Interpretando MLP**: engenharia de representação hierárquica

#### Bloco 2: Funções de Ativação (45 min)
- **Sigmoid**: σ(z) = 1/(1 + e⁻ᶻ)
  - Derivada: σ'(z) = σ(z)(1 - σ(z))
  - Problemas: saturação, vanishing gradient

- **Tanh**: tanh(z), derivada: 1 - tanh²(z)
- **ReLU**: max(0, z), derivada: {0 se z≤0, 1 se z>0}
- **Softmax**: exp(zᵢ) / Σⱼ exp(zⱼ)

#### Bloco 3: Backpropagation (60 min)
- **Forward pass**: propagação camada a camada
- **Derivada via regra da cadeia**: computational graphs
- **Backpropagation passo a passo**: dedução matemática completa
- **Implementação manual**: NumPy, teste em XOR e multiclasse

**Leituras**: Goodfellow Cap. 6-8, Aggarwal Cap. 3

---

## **SEMANA 3 — Generalização e Regularização**

### Estrutura da Aula (3 horas)
- **0:00–0:50**: Overfitting e bias-variance tradeoff
- **0:50–1:00**: *Intervalo 1*
- **1:00–1:45**: Técnicas de regularização (L1, L2, dropout, early stopping)
- **1:45–1:55**: *Intervalo 2*
- **1:55–2:50**: Inicialização, batch normalization e laboratório IMDB
- **2:50–3:00**: Fechamento

### Conteúdo Detalhado

#### Bloco 1: Overfitting (50 min)
- **Demonstração visual**: curvas de training vs. validation
- **Decomposição Bias-Variance**: Error = Bias² + Variance + Noise
- **Causas**: dados ruidosos, features espúrias, capacidade excessiva

#### Bloco 2: Regularização (45 min)
- **L2 Regularization**: L = L_original + λΣᵢwᵢ²
- **L1 Regularization**: L = L_original + λΣᵢ|wᵢ| (promove sparsity)
- **Dropout**: desativação aleatória com probabilidade p
- **Early Stopping**: patience, restore_best_weights

#### Bloco 3: Inicialização e Laboratório (55 min)
- **Xavier/Glorot**: Var(w) = 2/(n_in + n_out)
- **He initialization**: Var(w) = 2/n_in (para ReLU)
- **Batch Normalization**: x̂ = (x - μ)/√(σ² + ε)
- **Laboratório IMDB**: comparação de técnicas de regularização

**Leituras**: Chollet Cap. 4-5, Aggarwal Cap. 4

---

## **SEMANA 4 — CNNs: Fundamentos e Arquiteturas Clássicas**

### Estrutura da Aula (3 horas)
- **0:00–0:45**: Operações de convolução, padding, pooling, stride
- **0:45–0:55**: *Intervalo 1*
- **0:55–1:45**: LeNet-5, AlexNet e evolução histórica
- **1:45–1:55**: *Intervalo 2*
- **1:55–2:50**: Representação hierárquica e laboratório LeNet/MNIST
- **2:50–3:00**: Fechamento

### Conteúdo Detalhado

#### Bloco 1: Operações Fundamentais (45 min)
- **Motivação**: invariância translacional, redução de parâmetros
- **Convolução 2D**: S(i,j) = (K * I)(i,j) = Σₘ Σₙ K(m,n)I(i-m, j-n)
- **Stride e padding**: preservação de dimensões
- **Pooling**: max pooling, average pooling

#### Bloco 2: Arquiteturas Clássicas (50 min)
- **LeNet-5 (1998)**: conv → pool → conv → pool → denso
- **AlexNet (2012)**: ReLU, dropout, GPU, data augmentation
- **Análise crítica**: avanços em hardware e datasets

#### Bloco 3: Laboratório (55 min)
- **Hierarquia de features**: bordas → texturas → formas → classes
- **Implementação LeNet**: Keras/PyTorch
- **Visualização**: filtros aprendidos, feature maps

**Leituras**: Chollet Cap. 8, Weidman Cap. 5

---

## **SEMANA 5 — CNNs Modernas: VGG, Inception, ResNet**

### Estrutura da Aula (3 horas)
- **0:00–0:45**: VGG — simplicidade e profundidade
- **0:45–0:55**: *Intervalo 1*
- **0:55–1:45**: InceptionNet — eficiência via paralelismo
- **1:45–1:55**: *Intervalo 2*
- **1:55–2:50**: ResNet — aprendizado residual e laboratório
- **2:50–3:00**: Fechamento

### Conteúdo Detalhado

#### Tópico 1: VGG — Simplicidade e Profundidade
- **Princípios**: filtros 3×3 sequenciais
- **Estrutura VGG16/19**: blocos convolucionais repetitivos
- **Contribuições**: modularidade, transfer learning
- **Limitações**: 138M parâmetros, custo computacional

#### Tópico 2: Inception (GoogLeNet) — Paralelismo
- **Módulo Inception**: operações 1×1, 3×3, 5×5, pooling paralelas
- **Convoluções 1×1**: bottleneck, redução de dimensionalidade
- **Estrutura GoogLeNet**: 22 camadas, ~7M parâmetros
- **Global Average Pooling**: substituição de FC layers

#### Tópico 3: ResNet — Aprendizado Residual
- **Degradation problem**: redes profundas têm erro maior
- **Blocos residuais**: H(x) = F(x) + x
- **Skip connections**: gradientes fluem diretamente
- **Estrutura ResNet-50**: (3, 4, 6, 3) blocos por estágio
- **Laboratório**: comparação VGG vs Inception vs ResNet em CIFAR-10

#### Tópico 4: Técnicas Avançadas
- **Batch Normalization** em CNNs
- **Transfer Learning**: feature extraction vs fine-tuning
- **Data Augmentation**: rotação, flip, crop, mixup

#### Tópico 5: Comparação Quantitativa

| Modelo | Camadas | Parâmetros | Top-5 Error | FLOPs |
|--------|---------|------------|-------------|--------|
| VGG16 | 16 | 138M | 7.3% | 15.5G |
| Inception v3 | 48 | 24M | 5.6% | 5.7G |
| ResNet-50 | 50 | 25M | 5.3% | 4.1G |

**Leituras**: Papers originais VGG, Inception, ResNet

---

## **SEMANA 6 — Redes Recorrentes e Processamento de Sequências**

### Estrutura da Aula (3 horas)
- **0:00–0:45**: Dados sequenciais e arquitetura RNN
- **0:45–0:55**: *Intervalo 1*
- **0:55–1:45**: Vanishing gradient, LSTM, GRU
- **1:45–1:55**: *Intervalo 2*
- **1:55–2:50**: Laboratório prático (séries temporais/texto)
- **2:50–3:00**: Fechamento

### Conteúdo Detalhado

#### Bloco 1: Introdução a RNNs (45 min)
- **Dados sequenciais**: texto, áudio, séries temporais
- **Arquitetura recorrente**: 
  - hₜ = f(W_hh·hₜ₋₁ + W_xh·xₜ + b_h)
  - yₜ = W_hy·hₜ + b_y
- **Diagrama unfolded**: timesteps

#### Bloco 2: LSTM e GRU (50 min)
- **Backpropagation Through Time (BPTT)**
- **Vanishing/Exploding gradients**

- **LSTM**: Long Short-Term Memory
  - Gates: input, forget, output
  - Cell state: memória persistente
  - Fórmulas principais das gates

- **GRU**: simplificação do LSTM
- **Bidirecionais e empilhadas**

#### Bloco 3: Laboratório (55 min)
- **Dataset**: previsão de série temporal ou geração de texto
- **Implementação**: RNN → LSTM → GRU
- **Comparação**: performance e convergência
- **Regularização**: dropout em LSTM

**Leituras**: Chollet Cap. 10, Aggarwal Cap. 7

---

## **SEMANA 7 — Seq2Seq e Tradução Automática**

### Estrutura da Aula (3 horas)
- **0:00–0:45**: Arquitetura Encoder-Decoder
- **0:45–0:55**: *Intervalo 1*
- **0:55–1:45**: Teacher Forcing e técnicas de treinamento
- **1:45–1:55**: *Intervalo 2*
- **1:55–2:50**: Mecanismos de Atenção (Bahdanau/Luong) e laboratório
- **2:50–3:00**: Fechamento

### Conteúdo Detalhado

#### Bloco 1: Encoder-Decoder (45 min)
- **Motivação**: tradução, sumarização, chatbots
- **Encoder**: c = q(h₁, h₂, ..., hₜ)
- **Decoder**: p(y₁, y₂, ..., yₜ | c)
- **Tokens especiais**: `<BOS>`, `<EOS>`

#### Bloco 2: Teacher Forcing (50 min)
- **Exposure bias**: ground truth vs. predições próprias
- **Teacher forcing**: usar target real durante treinamento
- **Scheduled sampling**: mistura probabilística
- **Professor forcing**: discriminador regulariza diferenças

#### Bloco 3: Atenção e Laboratório (55 min)
- **Problema do bottleneck**: context vector fixo
- **Atenção Bahdanau (additive)**:
  - e_ij = a(s_i-1, h_j) = vᵀ·tanh(W₁h_j + W₂s_i-1)
  
- **Atenção Luong (multiplicative)**:
  - Dot-product, General, Concat

- **Laboratório**: Seq2Seq com atenção para tradução EN→PT
- **Visualização**: matrizes de atenção (alignment)

**Leituras**: Papers Bahdanau, Luong

---

## **SEMANA 8 — Mecanismos de Atenção Avançados**

### Estrutura da Aula (3 horas)
- **0:00–0:45**: Self-Attention: Query, Key, Value
- **0:45–0:55**: *Intervalo 1*
- **0:55–1:45**: Scaled Dot-Product Attention
- **1:45–1:55**: *Intervalo 2*
- **1:55–2:50**: Multi-Head Attention e laboratório
- **2:50–3:00**: Fechamento

### Conteúdo Detalhado

#### Bloco 1: Fundamentos de Self-Attention (45 min)
- **Diferença de atenção tradicional**: sequência atende a si mesma
- **Analogias**:
  - Sistema de busca (YouTube/Google)
  - Dicionário (HashMap)
  
- **No contexto NLP**:
  - Query (Q): "O que eu quero saber?"
  - Key (K): "Que informação cada palavra oferece?"
  - Value (V): "Qual é o conteúdo real?"

- **Formulação**: qᵢ = xᵢW^Q, kᵢ = xᵢW^K, vᵢ = xᵢW^V

#### Bloco 2: Scaled Dot-Product (50 min)
- **Cálculo de scores**: scores = QKᵀ
- **Problema de escala**: variância ≈ d_k
- **Solução — Scaled Dot-Product**:
  - Attention(Q, K, V) = softmax(QKᵀ/√d_k)·V

- **Masking**: padding mask, causal mask (look-ahead)
- **Implementação**: NumPy/PyTorch do zero

#### Bloco 3: Multi-Head Attention (55 min)
- **Motivação**: múltiplas "noções de relevância"
- **Processo**:
  1. Projetar em h conjuntos de Q, K, V
  2. Aplicar attention em cada head
  3. Concatenar outputs
  4. Projeção final W^O

- **Implementação completa**: classe PyTorch
- **Laboratório**: visualização de attention patterns
- **Análise**: diferentes heads capturam relações diversas

**Leituras**: "Attention Is All You Need" (Vaswani et al., 2017)

---

## **SEMANA 9 — Transformer: Arquitetura Completa**

### Estrutura da Aula (3 horas)
- **0:00–0:50**: Arquitetura Transformer e Positional Encoding
- **0:50–1:00**: *Intervalo 1*
- **1:00–1:45**: Feed-Forward, Residual Connections, Layer Normalization
- **1:45–1:55**: *Intervalo 2*
- **1:55–2:50**: Treinamento, Masking e laboratório
- **2:50–3:00**: Fechamento

### Conteúdo Detalhado

#### Bloco 1: Arquitetura e Positional Encoding (50 min)
- **Paper "Attention Is All You Need" (2017)**: 173k+ citações
- **Estrutura dual**: Encoder (6 camadas) + Decoder (6 camadas)
- **Positional Encoding sinusoidal**:
  - PE_(pos,2i) = sin(pos/10000^(2i/d_model))
  - PE_(pos,2i+1) = cos(pos/10000^(2i/d_model))

#### Bloco 2: Feed-Forward e Normalization (45 min)
- **Position-wise FFN**:
  - FFN(x) = max(0, xW₁ + b₁)W₂ + b₂

- **Residual Connections**: Output = Sublayer(x) + x
- **Layer Normalization**: 
  - LayerNorm(x) = γ·(x - μ)/√(σ² + ε) + β

- **Padrão "Add & Norm"**: x = LayerNorm(x + Sublayer(x))

#### Bloco 3: Treinamento e Laboratório (55 min)
- **Masking**: padding, look-ahead, cross-attention
- **Teacher forcing** no decoder
- **Label smoothing**, **learning rate schedule** (warmup + decay)

- **Laboratório**: Mini-Transformer para tradução
  - Implementação completa em PyTorch
  - Training loop
  - Visualização de attention weights
  - Comparação com Seq2Seq LSTM

**Leituras**: Paper "Attention Is All You Need" completo

---

## **SEMANA 10 — Large Language Models (LLMs)**

### Estrutura da Aula (3 horas)
- **0:00–0:50**: Evolução dos LLMs: BERT, GPT, T5
- **0:50–1:00**: *Intervalo 1*
- **1:00–1:45**: Scaling Laws e Emergent Abilities
- **1:45–1:55**: *Intervalo 2*
- **1:55–2:50**: Prompt Engineering e laboratório
- **2:50–3:00**: Fechamento

### Conteúdo Detalhado

#### Bloco 1: BERT, GPT, T5 (50 min)
**BERT (Encoder-only)**:
- Masked Language Modeling (MLM)
- Next Sentence Prediction (NSP)
- Aplicações: classificação, NER, QA

**GPT (Decoder-only)**:
- Causal Language Modeling
- Evolução: GPT-1 (117M) → GPT-4 (~1.7T)
- Zero-shot e few-shot learning

**T5 (Encoder-Decoder)**:
- Text-to-text framework unificado
- Span corruption pré-treinamento

#### Bloco 2: Scaling Laws e Emergent Abilities (45 min)
- **Scaling Laws**: performance previsível
  - L(N) = (N_c/N)^α

- **Emergent Abilities**: habilidades imprevisíveis
  - Few-shot learning
  - Aritmética
  - Chain-of-thought reasoning
  - Code generation

- **Debate científico**: mirage vs. real emergence

#### Bloco 3: Prompt Engineering (55 min)
- **Zero-Shot Learning**: instrução sem exemplos
- **Few-Shot Learning**: 1-shot, 3-shot, 5-shot
- **In-Context Learning**: aprender do contexto

- **Componentes de prompt**:
  - System message
  - Context
  - Instruction
  - Examples
  - Input
  - Output indicator

- **Laboratório**: experimentação com API
  - Sentiment analysis
  - Translation
  - Chain-of-thought reasoning
  - System messages

**Leituras**: Papers GPT-3, BERT, "Emergent Abilities of LLMs"

---

## **SEMANA 11 — Autoencoders e VAEs**

### Estrutura da Aula (3 horas)
- **0:00–0:45**: Autoencoders clássicos e latent space
- **0:45–0:55**: *Intervalo 1*
- **0:55–1:45**: VAEs: ELBO, Reparameterization Trick, KL Divergence
- **1:45–1:55**: *Intervalo 2*
- **1:55–2:50**: Laboratório: implementando VAE
- **2:50–3:00**: Fechamento

### Conteúdo Detalhado

#### Bloco 1: Autoencoders Clássicos (45 min)
- **Definição**: rede neural para compressão + reconstrução
- **Componentes**: Encoder f_φ: x → z, Decoder g_θ: z → x̂
- **Bottleneck**: latent space comprimido
- **Loss**: L = (1/N)Σᵢ||xᵢ - x̂ᵢ||²
- **Latent space**: visualização, propriedades, limitações

#### Bloco 2: VAEs — Teoria (50 min)
- **Paradigma probabilístico**: z ~ q_φ(z|x) = N(μ(x), σ²(x))
- **ELBO derivation**:
  - log p_θ(x) ≥ 𝔼_q[log p_θ(x|z)] - D_KL(q_φ(z|x) || p(z))

- **Loss VAE**:
  - ℒ = Reconstruction Loss - KL Divergence

- **Reparameterization Trick**:
  - ε ~ N(0, I), z = μ_φ(x) + σ_φ(x)⊙ε

#### Bloco 3: Laboratório (55 min)
- **Implementação completa em PyTorch**
- **Dataset**: MNIST
- **Experimentos**:
  - Treinamento e visualização de loss
  - Exploração do latent space 2D
  - Geração de novos dígitos
  - Interpolação no latent space
  - β-VAE: variar peso do KL

**Leituras**: "Auto-Encoding Variational Bayes" (Kingma & Welling, 2013)

---

## **SEMANA 12 — Generative Adversarial Networks (GANs)**

### Estrutura da Aula (3 horas)
- **0:00–0:50**: Fundamentos de GANs: Minimax Game, Nash Equilibrium
- **0:50–1:00**: *Intervalo 1*
- **1:00–1:45**: DCGAN e técnicas de estabilização
- **1:45–1:55**: *Intervalo 2*
- **1:55–2:50**: Mode Collapse e laboratório
- **2:50–3:00**: Fechamento

### Conteúdo Detalhado

#### Bloco 1: Fundamentos (50 min)
- **Arquitetura dual**: Generator vs. Discriminator
- **Minimax Game**:
  - min_G max_D V(D,G) = 𝔼_x[log D(x)] + 𝔼_z[log(1 - D(G(z)))]

- **Nash Equilibrium**: D(x) = 0.5 quando p_g = p_data
- **Non-saturating loss**: max_G log D(G(z))

#### Bloco 2: DCGAN (45 min)
- **Inovações arquiteturais** (Radford et al., 2015):
  1. Strided convolutions (sem pooling)
  2. Batch Normalization (exceto input/output)
  3. Remove FC layers
  4. ReLU (Generator) + LeakyReLU (Discriminator) + Tanh (output)

- **Best practices**:
  - Learning rate: 0.0002
  - Adam com β₁ = 0.5
  - Batch size: 128
  - Weight init: Normal(0, 0.02)

- **Monitoramento**: losses, amostras, IS, FID

#### Bloco 3: Mode Collapse e Laboratório (55 min)
- **Mode Collapse**: Generator produz poucos tipos de outputs
- **Tipos**: total, parcial, rotating
- **Detecção**: visualizar batch, Inception Score
- **Soluções**: minibatch discrimination, Unrolled GAN, WGAN

- **Outros desafios**: vanishing gradients, non-convergence
- **Laboratório**: implementação DCGAN completa
  - Training loop alternado
  - Visualização de evolução
  - Experimentos com hiperparâmetros
  - Interpolação no latent space

**Leituras**: Papers GAN (Goodfellow, 2014), DCGAN (Radford, 2015)

---

## **SEMANA 13 — Diffusion Models e Estado da Arte**

### Estrutura da Aula (3 horas)
- **0:00–0:50**: Forward/Reverse Diffusion e Score Matching
- **0:50–1:00**: *Intervalo 1*
- **1:00–1:45**: DDPM: Training Objective e Implementação
- **1:45–1:55**: *Intervalo 2*
- **1:55–2:50**: Latent Diffusion Models (Stable Diffusion) e laboratório
- **2:50–3:00**: Fechamento

### Conteúdo Detalhado

#### Bloco 1: Fundamentos de Diffusion (50 min)
- **Inspiração**: termodinâmica não-equilibrada
- **Forward process**: adição gradual de ruído
  - q(xₜ | xₜ₋₁) = N(xₜ; √(1-βₜ)xₜ₋₁, βₜI)

- **Reparametrização direta**:
  - xₜ = √(ᾱₜ)x₀ + √(1-ᾱₜ)ε

- **Reverse process**: p_θ(xₜ₋₁|xₜ)
- **Score matching**: conexão teórica

#### Bloco 2: DDPM (45 min)
- **Loss simplificada**:
  - L_simple = 𝔼[||ε - ε_θ(xₜ, t)||²]

- **Algoritmo de treinamento**: sample timestep aleatório, prever ruído
- **Sampling algorithm**: denoising iterativo de x_T a x₀
- **Arquitetura U-Net**: time embedding, self-attention, ResNet blocks

#### Bloco 3: Latent Diffusion e Stable Diffusion (55 min)
- **Problema**: pixel space é caro
- **Solução**: diffusion no latent space de VAE

- **Componentes Stable Diffusion**:
  1. VAE (Encoder/Decoder)
  2. U-Net (denoising no latent space)
  3. CLIP Text Encoder
  4. Cross-attention conditioning

- **Classifier-Free Guidance**:
  - ε̃ = ε_uncond + s·(ε_cond - ε_uncond)

- **Laboratório**: experimentação com Stable Diffusion
  - Variar guidance scale
  - Negative prompts
  - Número de steps
  - Interpolação entre prompts

**Leituras**: Papers DDPM (Ho, 2020), Stable Diffusion (Rombach, 2022)

---

## **SEMANA 14 — Interpretabilidade, Robustez e Ética**

### Estrutura da Aula (3 horas)
- **0:00–0:50**: Interpretabilidade e XAI (SHAP, LIME, Grad-CAM)
- **0:50–1:00**: *Intervalo 1*
- **1:00–1:45**: Robustez Adversarial: Ataques e Defesas
- **1:45–1:55**: *Intervalo 2*
- **1:55–2:50**: Ética em IA: Viés, Fairness, Privacidade
- **2:50–3:00**: Fechamento

### Conteúdo Detalhado

#### Bloco 1: Interpretabilidade (50 min)
- **Problema da "caixa preta"**
- **Saliency Maps**: S = |∂y_c/∂x|
- **Grad-CAM**: heatmaps em CNNs
- **LIME**: explicação local via modelo linear
- **SHAP**: Shapley values da teoria dos jogos

#### Bloco 2: Robustez Adversarial (45 min)
- **Exemplos adversariais**: x_adv = x + δ
- **FGSM**: x_adv = x + ε·sign(∇_x J)
- **PGD**: FGSM iterativo com projeção
- **C&W**: otimização sofisticada
- **Ataques físicos**: adversarial patches
- **Defesas**:
  - Adversarial training (mais efetiva)
  - Defensive distillation
  - Input transformations
  - Certified defenses

#### Bloco 3: Ética em IA (55 min)
- **Viés algorítmico**:
  - Fontes: dataset, label, model, deployment bias
  - Casos reais: COMPAS, Amazon recruiting, facial recognition

- **Definições de Fairness**:
  - Demographic parity: P(Ŷ=1|A=0) = P(Ŷ=1|A=1)
  - Equal opportunity
  - Equalized odds

- **Privacidade**: differential privacy, federated learning
- **Uso responsável**: deepfakes, environmental impact, automação
- **AI Safety**: alignment, specification gaming

- **Laboratório**: detectando e mitigando viés

**Leituras**: Papers sobre Fairness, Adversarial Examples, AI Ethics

---

## **SEMANA 15 — Apresentações e Perspectivas Futuras**

### Estrutura da Aula (3 horas)
- **0:00–1:00**: Apresentações de Projetos Finais (Parte 1)
- **1:00–1:10**: *Intervalo 1*
- **1:10–2:00**: Apresentações de Projetos Finais (Parte 2)
- **2:00–2:10**: *Intervalo 2*
- **2:10–2:50**: Fronteiras da Pesquisa e Perspectivas Futuras
- **2:50–3:00**: Encerramento

### Conteúdo Detalhado

#### Blocos 1-2: Apresentações de Projetos (110 min total)
- **Formato**: 10 min apresentação + 2-3 min Q&A
- **8-10 projetos** no total

**Categorias de Projetos**:
- Reprodução de paper recente
- Aplicação original
- Estudo comparativo
- Extensão teórica

**Critérios de Avaliação**:
- Implementação técnica (30%)
- Profundidade teórica (25%)
- Qualidade experimental (25%)
- Apresentação (20%)

#### Bloco 3: Fronteiras da Pesquisa (40 min)

**Tópicos Emergentes**:
1. **Modelos Multimodais**: CLIP, GPT-4V, Embodied AI
2. **Efficient AI**: quantization, pruning, distillation
3. **Neuro-Symbolic AI**: integração com raciocínio simbólico
4. **Graph Neural Networks**: dados não-Euclidianos
5. **Continual Learning**: evitar catastrophic forgetting
6. **Foundation Models**: modelos multi-propósito massivos

**Desafios Abertos**:
- Reasoning complexo multi-step
- Sample efficiency
- Interpretabilidade profunda
- Robustez out-of-distribution
- AGI e alignment

**Carreira e Oportunidades**:
- Pesquisa acadêmica vs. indústria
- ML Engineer, MLOps, Data Scientist
- Habilidades valorizadas
- Recursos para continuar aprendendo

#### Encerramento (10 min)
- Reflexão sobre a jornada (Semanas 1-15)
- Princípios para levar adiante
- Feedback da disciplina
- Agradecimentos e despedida

---

## **RESUMO DO PROGRAMA**

### Estrutura Modular
```
Semanas 1-3:  Fundamentos (Perceptron → MLP → Regularização)
Semanas 4-5:  Visão Computacional (CNNs Clássicas e Modernas)
Semanas 6-7:  Sequências (RNNs, LSTMs, Seq2Seq)
Semanas 8-10: Revolução Transformer (Atenção → Transformers → LLMs) ⭐
Semanas 11-13: Modelos Generativos (VAE → GAN → Diffusion) ⭐
Semana 14:    Responsabilidade (Interpretabilidade, Robustez, Ética)
Semana 15:    Integração (Projetos e Perspectivas Futuras)
```

### Avaliação
- **Projeto Final**: 40%
- **Listas de Exercícios**: 30% (3 listas)
- **Paper Review**: 15%
- **Participação**: 15%

### Bibliografia Principal
1. Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press.
2. Chollet, F. (2021). *Deep Learning with Python* (2nd ed.). Manning.
3. Aggarwal, C. C. (2018). *Neural Networks and Deep Learning*. Springer.
4. Weidman, S. (2019). *Deep Learning from Scratch*. O'Reilly.

### Papers Fundamentais
- Vaswani et al. (2017): "Attention Is All You Need"
- Goodfellow et al. (2014): "Generative Adversarial Networks"
- Kingma & Welling (2013): "Auto-Encoding Variational Bayes"
- Ho et al. (2020): "Denoising Diffusion Probabilistic Models"
- Devlin et al. (2018): "BERT"
- Brown et al. (2020): "GPT-3"
- Rombach et al. (2022): "Stable Diffusion"

### Pré-requisitos
- Álgebra Linear
- Cálculo Diferencial
- Probabilidade e Estatística
- Python (intermediário)
- Machine Learning (básico)

---

**Elaborado para**: Programa de Pós-Graduação em Computação (Mestrado/Doutorado)  
**Versão**: 2025.2  
**Última atualização**: Outubro 2025

---

## 👨‍🏫 Créditos e Autoria

* **Autor Original das Aulas e Códigos**: **Prof. Dr. Francisco de Assis Boldt**
  * Perfil no GitHub: [@fboldt](https://github.com/fboldt)
  * Repositório Upstream Oficial: [fboldt/aulasann](https://github.com/fboldt/aulasann)
* **Enriquecimento Didático e Curadoria**: **Paulo Fernando** ([@Paulo83-dev](https://github.com/Paulo83-dev))
* **Metodologia de Enriquecimento**: Desenvolvida com auxílio da skill de IA `enrich-ml-notebooks`.
