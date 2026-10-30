# 📊 Controle de Progresso: Enriquecimento Didático de Redes Neurais (ANN)

Este arquivo é a memória de estado persistente do processo de enriquecimento didático dos 42 cadernos de Redes Neurais Artificiais, orientado pela skill `enrich-ml-notebooks`.

---

## 📈 Resumo Geral
* **Total de Cadernos**: 42 (21 anteriores + 21 novos do repositório upstream)
* **Concluídos**: 36 / 42 (85.7%)
* **Status Atual**: Lotes 1 a 10 concluídos com sucesso! Próximo da fila: Lote 11 (Mecanismos de Self-Attention).

---

## 🧭 Tabela de Acompanhamento por Lotes

### 📦 Lote 1: Perceptron & Adaline (Fundamentos dos Modelos Lineares)
| ID | Arquivo | Células Finais | Status | Tópico Pedagógico Principal |
| :---: | :--- | :---: | :---: | :--- |
| 01 | `aula01a_perceptron_learning_algorithm.ipynb` | 19 (10 MD, 9 Code) | ✅ Concluído | Perceptron clássico (Rosenblatt, 1958) e regra de atualização |
| 02 | `aula02a perceptron learning algorithm with bias.ipynb` | 13 (8 MD, 5 Code) | ✅ Concluído | Inclusão do termo de bias para deslocamento da fronteira |
| 03 | `aula02b perceptron vetorial.ipynb` | 11 (7 MD, 4 Code) | ✅ Concluído | Vetorização em NumPy ($w^T x$) sem loops lentos |
| 04 | `aula02c linear regression.ipynb` | 6 (4 MD, 2 Code) | ✅ Concluído | O neurônio como regressor linear contínuo |
| 05 | `aula02d normal equation.ipynb` | 8 (5 MD, 3 Code) | ✅ Concluído | Solução analítica fechada via Equação Normal |
| 06 | `aula02e adaline with normal equation.ipynb` | 8 (5 MD, 3 Code) | ✅ Concluído | Neurônio Adaline (Widrow-Hoff) e ativação linear |
| 07 | `aula02f adaline with SGD.ipynb` | 13 (8 MD, 5 Code) | ✅ Concluído | Adaline com SGD e sensibilidade a outliers |

---

### 📦 Lote 2: Funções de Custo, Multiclasse & O Paradoxo do XOR
| ID | Arquivo | Células Finais | Status | Tópico Pedagógico Principal |
| :---: | :--- | :---: | :---: | :--- |
| 08 | `aula03a_algorithms.ipynb` | 13 (8 MD, 5 Code) | ✅ Concluído | Design Pattern Strategy: desacoplando modelo e otimizador |
| 09 | `aula03b - cost functions.ipynb` | 25 (14 MD, 11 Code) | ✅ Concluído | Funções de Custo: MSE, Sigmoide, Tanh e Hinge Loss |
| 10 | `aula03c_multiclasse.ipynb` | 18 (10 MD, 8 Code) | ✅ Concluído | Matriz de Pesos W e Argmax para 4 classes |
| 11 | `aula03d - XOR.ipynb` | 14 (8 MD, 6 Code) | ✅ Concluído | Portas OR, AND e a crise do XOR (Minsky & Papert, 1969) |

---

### 📦 Lote 3: Não-Linearidades, Tanh & ELM
| ID | Arquivo | Células Finais | Status | Tópico Pedagógico Principal |
| :---: | :--- | :---: | :---: | :--- |
| 12 | `aula04a_cost_functions.ipynb` | 19 (11 MD, 8 Code) | ✅ Concluído | Funções de custo com derivadas para gradiente |
| 13 | `aula04c - XOR classifier.ipynb` | 13 (8 MD, 5 Code) | ✅ Concluído | Derrotando o XOR: 2 neurônios ocultos e espaço latente H |
| 14 | `aula04d - XOR tanh.ipynb` | 12 (7 MD, 5 Code) | ✅ Concluído | Ativação suave Tangente Hiperbólica ($tanh$) e derivadas |
| 15 | `aula04e - ELM.ipynb` | 9 (6 MD, 3 Code) | ✅ Concluído | Extreme Learning Machine: pesos ocultos fixos e Equação Normal |

---

### 📦 Lote 4: Multilayer Perceptron (MLP) do Zero
| ID | Arquivo | Células Finais | Status | Tópico Pedagógico Principal |
| :---: | :--- | :---: | :---: | :--- |
| 16 | `aula05a_Last_Layer.ipynb` | 9 (6 MD, 3 Code) | ✅ Concluído | Backpropagation na última camada (gradiente de saída e update) |
| 17 | `aula05b - Single Hidden Layer.ipynb` | 10 (6 MD, 4 Code) | ✅ Concluído | Retropropagação do erro através de 1 camada oculta ($H \rightarrow X$) |
| 18 | `aula05c - Multi Layer.ipynb` | 19 (9 MD, 10 Code) | ✅ Concluído | MLP Arbitrário de N camadas: forward e backward genérico |
| 19 | `aula05d - Multi Classe.ipynb` | 12 (7 MD, 5 Code) | ✅ Concluído | Classificação multiclasse com camadas densas |
| 20 | `aula05e - MLP Iris.ipynb` | 11 (7 MD, 4 Code) | ✅ Concluído | Aplicação ponta a ponta do MLP no dataset Iris |

---

### 📦 Lote 5: Deep Learning Moderno com PyTorch
| ID | Arquivo | Células Finais | Status | Tópico Pedagógico Principal |
| :---: | :--- | :---: | :---: | :--- |
| 21 | `aula06a_pytorch.ipynb` | 17 (8 MD, 9 Code) | ✅ Concluído | Grafos Dinâmicos, Autograd no PyTorch, ReLU, Adam e Parâmetros |

---

### 📦 Lote 6: Keras & Classificação de Texto Inicial
| ID | Arquivo | Células Finais | Status | Tópico Pedagógico Principal |
| :---: | :--- | :---: | :---: | :--- |
| 22 | `aula06b_keras.ipynb` | 12 (7 MD, 5 Code) | ✅ Concluído | Padrão Scikit-Learn no Keras: SLP, SHLP e MLP Modular |
| 23 | `aula06c_reuters.ipynb` | 56 (28 MD, 28 Code) | ✅ Concluído | NLP e Reuters: BoW, Overfitting, Gargalo e Keras vs PyTorch |

---

### 📦 Lote 7: Visão Computacional: MNIST em Keras e PyTorch
| ID | Arquivo | Células Finais | Status | Tópico Pedagógico Principal |
| :---: | :--- | :---: | :---: | :--- |
| 24 | `aula07a_mnist_flat_keras.ipynb` | 38 (20 MD, 18 Code) | ✅ Concluído | MLP Flat no Keras, a armadilha do StandardScaler e Pipelines |
| 25 | `aula07b_mnist_conv_keras.ipynb` | 19 (12 MD, 7 Code) | ✅ Concluído | CNNs no Keras, transformador Shape2Keras e 99%+ de acurácia |
| 26 | `aula07c_mnist_flat_torch.ipynb` | 16 (9 MD, 7 Code) | ✅ Concluído | MLP Flat no PyTorch com nn.Module, DataLoaders e Pipeline |
| 27 | `aula07d_mnist_conv_torch.ipynb` | 14 (8 MD, 6 Code) | ✅ Concluído | CNNs no PyTorch com nn.Conv2d, Channels-First e Shape2Torch |

---

### 📦 Lote 8: Visão Computacional com Imagens Reais & Séries Temporais
| ID | Arquivo | Células Finais | Status | Tópico Pedagógico Principal |
| :---: | :--- | :---: | :---: | :--- |
| 28 | `aula08a_dogs_vs_cats.ipynb` | 62 (32 MD, 30 Code) | ✅ Concluído | Imagens Reais (Dogs vs Cats), Augmentation e Transfer Learning com VGG16 (97%+) |
| 29 | `aula09a_forecasting.ipynb` | 60 (34 MD, 26 Code) | ✅ Concluído | Séries Temporais (Jena Climate), Janelas Deslizantes, Baseline, RNN, LSTM e BiLSTM |

---

### 📦 Lote 9: Processamento de Linguagem Natural (NLP) Clássico & Vetorização
| ID | Arquivo | Células Finais | Status | Tópico Pedagógico Principal |
| :---: | :--- | :---: | :---: | :--- |
| 30 | `aula10a_NLP.ipynb` | 22 (13 MD, 9 Code) | ✅ Concluído | Fundamentos de NLP: Padronização, Tokenização, OOV e TextVectorization |
| 31 | `aula10b_binary_unigram.ipynb` | 23 (13 MD, 10 Code) | ✅ Concluído | Análise de Sentimentos no IMDB: Vetorização Binária com Unigramas (1-gram) |
| 32 | `aula10b_binary_2gram.ipynb` | 23 (13 MD, 10 Code) | ✅ Concluído | Análise de Sentimentos no IMDB: Vetorização Binária com Bigramas (2-gram) |
| 33 | `aula10b_binary_3gram.ipynb` | 23 (13 MD, 10 Code) | ✅ Concluído | Análise de Sentimentos no IMDB: Vetorização Binária com Trigramas (3-gram) |
| 34 | `aula10b_tfidf.ipynb` | 23 (13 MD, 10 Code) | ✅ Concluído | Análise de Sentimentos no IMDB: Ponderação Estatística TF-IDF |

---

### 📦 Lote 10: NLP Sequencial: Recorrência & Embeddings Densos
| ID | Arquivo | Células Finais | Status | Tópico Pedagógico Principal |
| :---: | :--- | :---: | :---: | :--- |
| 35 | `aula10f - lstm.ipynb` | 23 (13 MD, 10 Code) | ✅ Concluído | Sequências Ordenadas no IMDB: Embedding Treinável, mask_zero e BiLSTM |
| 36 | `aula10g - glove.ipynb` | 29 (16 MD, 13 Code) | ✅ Concluído | Transfer Learning em NLP: Embeddings GloVe (Stanford) Congelados & BiLSTM |

---

### 📦 Lote 11: A Era da Atenção (Mecanismos de Self-Attention)
| ID | Arquivo | Células Atuais | Status | Tópico Pedagógico Principal |
| :---: | :--- | :---: | :---: | :--- |
| 37 | `aula11a_Simplified_self_attention.ipynb` | Bruto: 31 (18 MD, 13 Code) | ⏳ Próximo | Mecanismo básico de auto-atenção (Self-Attention) simplificado |
| 38 | `aula11b_self_attention_mechanism_with_trainable_weights.ipynb` | Bruto: 21 (7 MD, 14 Code) | ⏳ Na fila | Self-Attention com pesos treináveis ($Q, K, V$) |
| 39 | `aula11c_Causal_attention.ipynb` | Bruto: 23 (8 MD, 15 Code) | ⏳ Na fila | Atenção Causal mascarada (estilo GPT / autoregressivo) |
| 40 | `aula11d_Multi_head_attention.ipynb` | Bruto: 13 (4 MD, 9 Code) | ⏳ Na fila | Atenção com Múltiplas Cabeças (*Multi-Head Attention*) |

---

### 📦 Lote 12: Transformers & Deep Learning Moderno (Hugging Face)
| ID | Arquivo | Células Atuais | Status | Tópico Pedagógico Principal |
| :---: | :--- | :---: | :---: | :--- |
| 41 | `aula12a_transformer.ipynb` | Bruto: 18 (8 MD, 10 Code) | ⏳ Na fila | Arquitetura Transformer completa (*Attention Is All You Need*) |
| 42 | `aula12c_huggingface.ipynb` | Bruto: 9 (1 MD, 8 Code) | ⏳ Na fila | Ecossistema Hugging Face (`transformers`, pipelines e modelos) |
