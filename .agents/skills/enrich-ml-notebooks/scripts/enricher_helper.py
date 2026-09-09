"""
Script auxiliar para manipulação segura e enriquecimento de notebooks Jupyter (.ipynb).
Permite inspecionar, injetar células markdown explicativas e validar arquivos JSON.
"""

import json
import sys
import shutil
from pathlib import Path

def backup_notebook(filepath: str) -> str:
    """Cria uma cópia de segurança do notebook antes de qualquer edição."""
    path = Path(filepath)
    backup_path = path.with_suffix('.ipynb.bak')
    shutil.copy2(path, backup_path)
    print(f"[Backup] Cópia criada em: {backup_path}")
    return str(backup_path)

def inspect_notebook(filepath: str):
    """Inspeciona as células existentes do notebook."""
    with open(filepath, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    cells = nb.get('cells', [])
    print(f"=== Inspeção de {filepath} ===")
    print(f"Total de células: {len(cells)}")
    for i, c in enumerate(cells):
        ctype = c.get('cell_type')
        src = "".join(c.get('source', [])).strip().split('\n')[0] if c.get('source') else '<vazio>'
        print(f"  [{i:02d}] {ctype.upper()}: {src[:80]}")

def verify_notebook(filepath: str) -> bool:
    """Verifica se o arquivo é um JSON válido e exibe contagem de células."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        cells = nb.get('cells', [])
        md_count = sum(1 for c in cells if c.get('cell_type') == 'markdown')
        code_count = sum(1 for c in cells if c.get('cell_type') == 'code')
        print(f"[OK] {filepath}: Válido! Total: {len(cells)} (Markdown: {md_count}, Código: {code_count})")
        return True
    except Exception as e:
        print(f"[ERRO] {filepath} é inválido: {e}")
        return False

if __name__ == '__main__':
    if len(sys.argv) > 1:
        inspect_notebook(sys.argv[1])
    else:
        print("Uso: python enricher_helper.py <caminho_do_notebook.ipynb>")
