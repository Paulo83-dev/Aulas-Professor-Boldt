---
name: enrich-ml-notebooks
description: >-
  Transform raw machine learning and data science code notebooks (.ipynb) into comprehensive,
  beginner-friendly, step-by-step didactic lessons. Use when the user asks to explain,
  annotate, teach, or enrich Python/Jupyter notebooks for studying, or when processing
  future lectures from Professor Boldt or similar Machine Learning courses.
---

# 🎓 Skill: Enriquecimento Didático de Notebooks de Machine Learning

Esta skill instrui o agente de IA a analisar cadernos Jupyter brutos (`.ipynb`) e transformá-los em **guias de estudo passo a passo para iniciantes**, preservando integralmente o código e a intenção do professor, mas adicionando contextualização teórica e comentários minuciosos.

---

## 🎯 Objetivo Pedagógico
Garantir que um estudante leigo consiga abrir o caderno e entender:
1. **O Problema Real**: O que estamos tentando resolver no mundo real.
2. **A Intenção Pedagógica**: Por que o professor escreveu o código desse jeito específico (ex: por que fazer uma versão ingênua ou artesanal antes de usar a biblioteca pronta).
3. **A Matemática Intuitiva**: Sem jargões impenetráveis; usar analogias e formas visuais (ex: parábolas, distâncias no plano, vales).
4. **O Código Linha por Linha**: O que cada função do Python, NumPy, Pandas, Matplotlib e Scikit-Learn faz.

---

## 🔄 Fluxo de Trabalho (Passo a Passo para o Agente)

### Passo 1: Inspeção Estrutural do Caderno
Antes de alterar qualquer coisa, o agente deve rodar um script Python rápido para inspecionar todas as células do arquivo `.ipynb`:
* Contar quantas células existem.
* Identificar quais são código e quais são markdown.
* Mapear a sequência de tópicos abordados pelo professor.

### Passo 2: Mapeamento da Intenção Didática
Descubra a evolução pedagógica da aula:
* **Construção "Do Zero" vs Biblioteca**: O professor fez uma implementação manual (com loops ou NumPy puro) antes de chamar a função do `scikit-learn`? Destaque isso explicitamente!
* **A Armadilha / Pegadinha**: Existe algum erro comum sendo demonstrado de propósito? (Ex: gradiente que explode sem escala, vazamento de dados ao normalizar antes do split, KFold sem shuffle).
* **Métricas**: Qual métrica foi escolhida (MSE, MAE, RMSE, Acurácia) e por quê?

### Passo 3: Criação da Estrutura Didática Padrão
Para cada notebook, o agente deve gerar:

1. **Cabeçalho Principal (Markdown no Topo)**:
   * Título amigável com emoji (ex: `📘 Aula 0X: ...`).
   * **Objetivo da Aula**: Contexto do problema real.
   * **A Intenção Pedagógica**: O caminho do aprendizado.
   * **Glossário Rápido**: Termos novos apresentados na aula.
   * **Trilha / Mapa da Aula**: Tópicos numerados.

2. **Células de Markdown Antes de Cada Bloco de Código**:
   * Título da seção (ex: `## 3. Divisão em Treino e Teste`).
   * Explicação simples de *"O que estamos fazendo agora?"*.
   * *"Por que fazer assim?"* (a motivação do professor).
   * Alertas com GitHub Alerts:
     * `> [!NOTE]`: Explicação conceitual de apoio.
     * `> [!TIP]`: Dica prática ou atalho.
     * `> [!IMPORTANT]`: Regra de ouro da ciência de dados (ex: não vazar dados).
     * `> [!WARNING]`: Pegadinhas ou limitações de algoritmos.

3. **Comentários no Código (Linha por Linha)**:
   * Cada linha relevante deve ter comentário em Português do Brasil.
   * Explicar parâmetros chave (ex: `test_size=0.2`, `random_state=42`, `n_neighbors=15`).
   * Preservar 100% dos nomes de variáveis e funções originais do professor.

4. **Resumo Final (Markdown no Fim do Caderno)**:
   * `🎓 Resumo da Aula & O que você aprendeu`: Lista consolidando os pontos chave.
   * `👉 Próximo Passo`: Ponte conectando o conteúdo com a próxima aula.

---

## ⚠️ Regras Críticas de Execução Técnica

1. **Manipulação Segura do Arquivo `.ipynb`**:
   * Arquivos `.ipynb` são JSON. Sempre utilize scripts Python com `json.load()` e `json.dump(..., ensure_ascii=False, indent=1)` para editar o caderno.
   * **Nunca** corrompa metadados de células de código existentes (`outputs`, `execution_count`).
2. **Prevenção contra Sobrescrita do Editor (Buffer de Memória)**:
   * Se o usuário estiver com o notebook aberto na tela do VS Code / Antigravity IDE, o editor manterá o arquivo na memória (exibindo uma bolinha `•` na aba).
   * **Instrução obrigatória ao usuário**: Sempre peça para o usuário **fechar a aba do notebook (`X`) sem salvar** antes de reabri-lo, garantindo que o editor carregue a versão fresca do disco.
3. **Verificação de Integridade**:
   * Sempre rode um script de validação sintática garantindo que o JSON resultante seja válido e que a contagem de células reflita as novas adições.
