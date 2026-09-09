# 🎓 Cursos e Educação: Aulas do Professor Boldt

Repositório central de estudos em **Inteligência Artificial, Reconhecimento de Padrões e Redes Neurais**, baseado nos cursos do **Professor Fernando Boldt**.

---

## 🗂️ Organização dos Módulos

O repositório está estruturado em duas trilhas complementares de conhecimento:

```text
📁 AULAS DO BOLDT/
│
├── 📁 .agents/                             # Skill de IA para enriquecimento pedagógico contínuo
│   └── skills/enrich-ml-notebooks/
│
├── 📁 01_machine_learning/                 # Módulo 1: Machine Learning & Reconhecimento de Padrões
│   ├── README.md                           # Guia detalhado do curso de ML
│   ├── aula01a_regressão_linear.ipynb      # Regressão Linear, Gradiente e Z-Score
│   ├── aula02a_classificador_linear_binário.ipynb
│   ├── aula02b_classificador_linear_multiclasse.ipynb
│   ├── aula02c - classificador de vizinhança.ipynb
│   ├── aula03a - validação cruzada.ipynb
│   └── aula03b - gridsearch.ipynb
│
└── 📁 02_redes_neurais/                    # Módulo 2: Redes Neurais Artificiais (ANN)
    ├── README.md                           # Guia original de Redes Neurais
    ├── aula01a_perceptron_learning_algorithm.ipynb
    ├── aula02a... até aula02f              # Adaline, Equação Normal e SGD
    ├── aula03a... até aula03d              # Funções de Custo e o problema do XOR
    ├── aula04a... até aula04e              # Classificadores XOR, Tanh e ELM
    ├── aula05a... até aula05e              # Camadas ocultas e Multilayer Perceptron (MLP)
    └── aula06a_pytorch.ipynb               # Introdução ao PyTorch
```

---

## 🧭 Roteiro Recomendado de Estudos

1. **[Módulo 1: 01_machine_learning](file:///c:/Users/paulo/OneDrive/%C3%81rea%20de%20Trabalho/Cursos%20e%20Educa%C3%A7%C3%A3o/AULAS%20DO%20BOLDT/01_machine_learning/README.md)** (6/6 Cadernos — 100% Concluído):
   * Aprenda os fundamentos essenciais: separação treino/teste, funções de custo analíticas e iterativas, padronização Z-Score, classificadores lineares binários e multiclasse, k-NN, validação cruzada k-Fold e busca sistemática com GridSearch.
   * Todos os 6 cadernos estão **completamente comentados linha a linha e enriquecidos didaticamente**.

2. **[Módulo 2: 02_redes_neurais](file:///c:/Users/paulo/OneDrive/%C3%81rea%20de%20Trabalho/Cursos%20e%20Educa%C3%A7%C3%A3o/AULAS%20DO%20BOLDT/02_redes_neurais/README.md)** (21/21 Cadernos — 100% Concluído):
   * Entenda a evolução histórica desde o **Perceptron clássico** (Rosenblatt, 1958) e inclusão de bias.
   * Transição para neurônios lineares contínuos (**Adaline**), solução fechada via **Equação Normal** e descida do gradiente estocástica (**SGD**).
   * O problema histórico da separação não-linear do **XOR** (Minsky & Papert, 1969).
   * Projeção em espaços latentes ($H$), ativações suaves ($\tanh$) e Extreme Learning Machine (**ELM**).
   * Construção manual do **Multilayer Perceptron (MLP)** com Backpropagation analítico do zero em NumPy.
   * Entrada no **Deep Learning moderno com PyTorch** (Autograd, `nn.Sequential`, `optim.Adam`, ReLU e contagem de parâmetros).

---

## 🛠️ Ambiente e Ferramentas

* **Linguagem**: Python 3.12+
* **Bibliotecas Essenciais**:
  ```bash
  pip install numpy pandas scikit-learn matplotlib seaborn ipykernel torch
  ```
* **Assistente de Estudos**: O repositório conta com a skill [enrich-ml-notebooks](.agents/skills/enrich-ml-notebooks/SKILL.md), permitindo enriquecer qualquer aula sob demanda.
