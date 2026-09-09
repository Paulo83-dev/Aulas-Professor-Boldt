# 🎓 Aulas do Professor Fernando Boldt: Machine Learning & Redes Neurais

[![Python 3.12](https://img.shields.io/badge/Python-3.12%2B-blue.svg?logo=python)](https://www.python.org/)
[![Jupyter Notebooks](https://img.shields.io/badge/Jupyter-Notebooks-orange.svg?logo=jupyter)](https://jupyter.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E.svg?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C.svg?logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Status](https://img.shields.io/badge/Status-100%25%20Concluído%20(27%2F27)-brightgreen.svg)]()
[![GitHub Repo](https://img.shields.io/badge/GitHub-Paulo83--dev%2FAulas--Professor--Boldt-blue)](https://github.com/Paulo83-dev/Aulas-Professor-Boldt)

Repositório central de estudos avançados em **Inteligência Artificial, Machine Learning Clássico e Redes Neurais Profundas (Deep Learning)**, baseado nas disciplinas do **Professor Dr. Fernando Boldt**.

Todos os 27 cadernos práticos do acervo original foram **enriquecidos pedagogicamente**, preservando 100% da lógica e do código original do professor, mas adicionando contextualização histórica, intuição geométrica, deduções matemáticas, explicações pré-bloco e **comentários didáticos linha a linha** orientados para iniciantes e pós-graduandos.

---

## 🌟 Diferenciais deste Acervo Enriquecido

* 📖 **Didática Passo a Passo**: Nenhum bloco de código é executado sem que sua razão conceitual seja apresentada antes.
* ✍️ **100% Comentado Linha a Linha**: Cada variável, função, operador e transformação matricial do NumPy/PyTorch é explicada de forma clara.
* 💡 **Alertas Conceituais**: Uso de caixas de destaque (`NOTE`, `TIP`, `IMPORTANT`) para fixar conceitos fundamentais e armadilhas comuns da modelagem.
* 🔬 **Da Teoria ao Framework**: Implementações manuais do zero em NumPy (soluções fechadas, SGD e Backpropagation) seguidas pela transição profissional para o **PyTorch** e integração com **Scikit-Learn**.
* 🤖 **Skill de IA Integrada**: Inclui a skill `.agents/skills/enrich-ml-notebooks/` para processar e manter a mesma consistência pedagógica em cadernos futuros.

---

## 🗂️ Estrutura do Repositório

```text
📁 Aulas-Professor-Boldt/
│
├── 📁 .agents/                             # Skill de Inteligência Artificial para enriquecimento contínuo
│   └── skills/enrich-ml-notebooks/
│       ├── SKILL.md                        # Diretrizes pedagógicas completas
│       ├── scripts/enricher_helper.py      # Automação de leitura e injeção sem perda de metadados
│       └── references/ml_pedagogy_guide.md # Guia de design pedagógico
│
├── 📁 01_machine_learning/                 # Módulo 01: Machine Learning & Reconhecimento de Padrões (6 cadernos)
│   ├── README.md                           # Visão geral e fundamentação teórica de ML
│   └── aula01a a aula03b                   # Regressão Linear, k-NN, Classificadores e Otimização
│
├── 📁 02_redes_neurais/                    # Módulo 02: Redes Neurais Artificiais & Deep Learning (21 cadernos)
│   ├── README.md                           # Guia do curso e Ementa Oficial de 15 semanas (PPGComp)
│   ├── TRACKING_PROGRESS.md                # Memória de estado de auditoria e células dos 21 cadernos
│   └── aula01a a aula06a                   # Do Perceptron (1958) e Crise do XOR até MLP e PyTorch
│
├── .gitignore                              # Proteção contra checkpoints e caches
└── README.md                               # Este portal de navegação
```

---

## 🧭 Trilha de Aprendizado Completa (27 Cadernos)

### 📘 Módulo 1: Machine Learning & Reconhecimento de Padrões (6 Cadernos)
> **Foco**: Fundamentos da aprendizagem supervisionada, regressão, classificação linear e não-linear, validação cruzada e ajuste de hiperparâmetros.

| Aula | Caderno | Tópicos Centrais |
| :---: | :--- | :--- |
| **01a** | [aula01a_regressão_linear.ipynb](01_machine_learning/aula01a_regressão_linear.ipynb) | Regressão Linear Simples, Gradiente Descendente Manual, MSE e Padronização Z-Score. |
| **02a** | [aula02a_classificador_linear_binário.ipynb](01_machine_learning/aula02a_classificador_linear_binário.ipynb) | Classificação linear binária, hiperplano de separação e métricas de acurácia. |
| **02b** | [aula02b_classificador_linear_multiclasse.ipynb](01_machine_learning/aula02b_classificador_linear_multiclasse.ipynb) | Estratégia multiclasse (One-vs-Rest), matrizes de peso e tomada de decisão. |
| **02c** | [aula02c - classificador de vizinhança.ipynb](01_machine_learning/aula02c%20-%20classificador%20de%20vizinhança.ipynb) | Classificador de K Vizinhos Mais Próximos ($k$-NN), distância Euclidiana e o impacto do $k$. |
| **03a** | [aula03a - validação cruzada.ipynb](01_machine_learning/aula03a%20-%20validação%20cruzada.ipynb) | Validação Cruzada ($k$-Fold), partição estratificada e mitigação de vazamento de dados. |
| **03b** | [aula03b - gridsearch.ipynb](01_machine_learning/aula03b%20-%20gridsearch.ipynb) | Busca sistemática em grade (GridSearchCV) para ajuste ótimo de hiperparâmetros. |

---

### 🧠 Módulo 2: Redes Neurais Artificiais (ANN) & Deep Learning (21 Cadernos)
> **Foco**: A evolução histórica e técnica das redes neurais — dos modelos biológicos lineares à diferenciação automática moderna com PyTorch.

#### 📦 Lote 1: Fundamentos Lineares (Perceptron & Adaline)
| Aula | Caderno | Tópicos Centrais |
| :---: | :--- | :--- |
| **01a** | [aula01a_perceptron_learning_algorithm.ipynb](02_redes_neurais/aula01a_perceptron_learning_algorithm.ipynb) | O Perceptron clássico (Rosenblatt, 1958), regra de atualização de pesos e convergência. |
| **02a** | [aula02a perceptron learning algorithm with bias.ipynb](02_redes_neurais/aula02a%20perceptron%20learning%20algorithm%20with%20bias.ipynb) | Inclusão do termo independente de *bias* ($b$) para deslocamento do hiperplano da origem. |
| **02b** | [aula02b perceptron vetorial.ipynb](02_redes_neurais/aula02b%20perceptron%20vetorial.ipynb) | Vetorização matricial em NumPy ($w^T x$), eliminando loops lentos em Python. |
| **02c** | [aula02c linear regression.ipynb](02_redes_neurais/aula02c%20linear%20regression.ipynb) | O neurônio artificial adaptado para tarefas contínuas de regressão linear. |
| **02d** | [aula02d normal equation.ipynb](02_redes_neurais/aula02d%20normal%20equation.ipynb) | Solução analítica fechada via Equação Normal: $w = (X^T X)^{-1} X^T y$. |
| **02e** | [aula02e adaline with normal equation.ipynb](02_redes_neurais/aula02e%20adaline%20with%20normal%20equation.ipynb) | O neurônio Adaline (Widrow-Hoff) e a separação entre ativação linear e quantizador. |
| **02f** | [aula02f adaline with SGD.ipynb](02_redes_neurais/aula02f%20adaline%20with%20SGD.ipynb) | Treinamento do Adaline com Gradiente Descendente Estocástico (SGD) e sensibilidade a outliers. |

#### 📦 Lote 2: Otimização, Multiclasse & O Paradoxo do XOR
| Aula | Caderno | Tópicos Centrais |
| :---: | :--- | :--- |
| **03a** | [aula03a_algorithms.ipynb](02_redes_neurais/aula03a_algorithms.ipynb) | Design Pattern *Strategy*: desacoplamento arquitetural entre a rede e o algoritmo de otimização. |
| **03b** | [aula03b - cost functions.ipynb](02_redes_neurais/aula03b%20-%20cost%20functions.ipynb) | Análise comparada de superfícies de perda: MSE, Sigmoide, Tangente Hiperbólica e Hinge Loss. |
| **03c** | [aula03c_multiclasse.ipynb](02_redes_neurais/aula03c_multiclasse.ipynb) | Matriz de pesos $W$ multidimensional e decodificação multiclasse via `argmax`. |
| **03d** | [aula03d - XOR.ipynb](02_redes_neurais/aula03d%20-%20XOR.ipynb) | Portas lógicas OR, AND e a crise histórica da separabilidade linear do XOR (Minsky & Papert, 1969). |

#### 📦 Lote 3: Não-Linearidades Suaves & Extreme Learning Machine (ELM)
| Aula | Caderno | Tópicos Centrais |
| :---: | :--- | :--- |
| **04a** | [aula04a_cost_functions.ipynb](02_redes_neurais/aula04a_cost_functions.ipynb) | Derivação matemática formal das funções de custo para cálculo de gradientes. |
| **04c** | [aula04c - XOR classifier.ipynb](02_redes_neurais/aula04c%20-%20XOR%20classifier.ipynb) | Superando o XOR: 2 neurônios ocultos e a projeção no espaço latente $H$. |
| **04d** | [aula04d - XOR tanh.ipynb](02_redes_neurais/aula04d%20-%20XOR%20tanh.ipynb) | Ativação suave Tangente Hiperbólica ($\tanh$) e sua derivada analítica $1 - \tanh^2(z)$. |
| **04e** | [aula04e - ELM.ipynb](02_redes_neurais/aula04e%20-%20ELM.ipynb) | Extreme Learning Machine: projeção aleatória fixa na camada oculta e solução direta por Equação Normal. |

#### 📦 Lote 4: Multilayer Perceptron (MLP) do Zero em NumPy
| Aula | Caderno | Tópicos Centrais |
| :---: | :--- | :--- |
| **05a** | [aula05a_Last_Layer.ipynb](02_redes_neurais/aula05a_Last_Layer.ipynb) | Backpropagation na última camada: gradiente de saída e regra de atualização dos pesos finais. |
| **05b** | [aula05b - Single Hidden Layer.ipynb](02_redes_neurais/aula05b%20-%20Single%20Hidden%20Layer.ipynb) | Retropropagação do erro através de uma camada oculta intermediária ($H \rightarrow X$). |
| **05c** | [aula05c - Multi Layer.ipynb](02_redes_neurais/aula05c%20-%20Multi%20Layer.ipynb) | Implementação genérica de MLP profundo para $N$ camadas arbitrárias (forward e backward matriciais). |
| **05d** | [aula05d - Multi Classe.ipynb](02_redes_neurais/aula05d%20-%20Multi%20Classe.ipynb) | Generalização do MLP para classificação multiclasse com múltiplas saídas ativas. |
| **05e** | [aula05e - MLP Iris.ipynb](02_redes_neurais/aula05e%20-%20MLP%20Iris.ipynb) | Caso prático completo com o dataset Iris: convergência do custo e visualização das fronteiras não-lineares. |

#### 📦 Lote 5: Deep Learning Moderno com PyTorch
| Aula | Caderno | Tópicos Centrais |
| :---: | :--- | :--- |
| **06a** | [aula06a_pytorch.ipynb](02_redes_neurais/aula06a_pytorch.ipynb) | Transição definitiva para o PyTorch: Autograd, `nn.Sequential`, `nn.Linear`, `nn.ReLU`, `optim.Adam`, compatibilidade com Scikit-Learn e cálculo detalhado de parâmetros livres. |

---

## ⚙️ Como Executar Localmente

### 1. Clonar o Repositório
```bash
git clone https://github.com/Paulo83-dev/Aulas-Professor-Boldt.git
cd Aulas-Professor-Boldt
```

### 2. Criar e Ativar Ambiente Virtual
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux / MacOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependências
```bash
pip install numpy pandas scikit-learn matplotlib seaborn jupyter ipykernel torch
```

### 4. Abrir no Jupyter Lab ou VS Code
```bash
jupyter lab
# ou abra a pasta diretamente no VS Code com a extensão Jupyter instalada
code .
```

---

## 📚 Bibliografia Recomendada

1. **Goodfellow, I., Bengio, Y., & Courville, A.** (2016). *Deep Learning*. MIT Press.
2. **Hastie, T., Tibshirani, R., & Friedman, J.** (2009). *The Elements of Statistical Learning: Data Mining, Inference, and Prediction*. Springer.
3. **Aggarwal, C. C.** (2018). *Neural Networks and Deep Learning: A Textbook*. Springer.
4. **Weidman, S.** (2019). *Deep Learning from Scratch: Building with Python from First Principles*. O'Reilly.

---

## 👨‍🏫 Créditos e Autoria
* **Aulas e Códigos Originais**: Prof. Dr. Fernando Boldt ([GitHub](https://github.com/fboldt)).
* **Enriquecimento Didático e Curadoria**: Paulo Fernando ([@Paulo83-dev](https://github.com/Paulo83-dev)).
* **Metodologia de Enriquecimento**: Desenvolvida com auxílio da skill de IA `enrich-ml-notebooks`.
