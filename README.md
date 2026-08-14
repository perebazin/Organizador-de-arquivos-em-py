# 📂 Organizador de Arquivos 2.0

Script em Python que organiza automaticamente os arquivos de uma pasta, movendo-os para subpastas de acordo com a categoria (Imagens, Documentos, Vídeos, Áudios, Compactados, Instaladores, Código, Outros), com log de execução e proteção contra sobrescrita de arquivos.

---

## ✨ Funcionalidades

- **Organização automática por categoria**, baseada na extensão do arquivo.
- **Pasta de destino separada da origem**, evitando bagunçar a pasta original.
- **Prevenção de conflitos de nome**: se já existir um arquivo com o mesmo nome no destino, o script adiciona `_1`, `_2`, `_3`... automaticamente, sem sobrescrever nada.
- **Log automático** (`organizador_log.txt`) com data/hora de cada movimentação.
- **Execução via terminal (com `--path`) ou direto pelo botão Run**, usando uma pasta padrão pré-configurada.
- Só move arquivos que estão **diretamente dentro da pasta de origem** (não entra em subpastas).

---

## 🗂️ Categorias e extensões reconhecidas

| Categoria | Extensões |
|---|---|
| Imagens | `.jpg` `.jpeg` `.png` `.gif` `.webp` `.svg` |
| Documentos | `.pdf` `.docx` `.doc` `.txt` `.xlsx` `.pptx` `.csv` |
| Videos | `.mp4` `.mov` `.avi` `.mkv` |
| Audios | `.mp3` `.wav` `.flac` |
| Compactados | `.zip` `.rar` `.7z` `.tar` `.gz` |
| Instaladores | `.exe` `.msi` `.dmg` `.apk` |
| Codigo | `.py` `.js` `.html` `.css` `.json` |
| Outros | Qualquer extensão não listada acima |

> Quer adicionar uma nova categoria ou extensão? Basta editar o dicionário `CATEGORIAS` no início do arquivo.

---

## ⚙️ Configuração

Antes de usar, ajuste as duas variáveis no topo do script:

```python
# Pasta usada quando o script é executado sem o argumento --path
PASTA_ORIGEM_PADRAO = r"C:\Users\PC Gamer\Desktop\Teste"

# Pasta para onde os arquivos organizados serão movidos
PASTA_DESTINO = Path(r"C:\Users\PC Gamer\Desktop\teste 2")
```

- `PASTA_ORIGEM_PADRAO`: pasta de onde os arquivos serão lidos, caso você não informe `--path`.
- `PASTA_DESTINO`: pasta onde as subpastas de categoria (Imagens, Documentos etc.) serão criadas.

O log é salvo automaticamente em:
```
<PASTA_DESTINO>/organizador_log.txt
```

---

## ▶️ Como usar

### Requisitos
- Python 3.7 ou superior (usa apenas bibliotecas padrão: `argparse`, `shutil`, `pathlib`, `datetime` — não precisa instalar nada).

### Opção 1 — Rodar direto (botão Run / IDE)
Sem passar nenhum argumento, o script usa a pasta definida em `PASTA_ORIGEM_PADRAO`:

```bash
python "Organizador de arquivos 2.0.py"
```

### Opção 2 — Rodar pelo terminal informando a pasta
```bash
python "Organizador de arquivos 2.0.py" --path "C:\Users\SeuUsuario\Downloads"
```

### Exemplo de saída no terminal
```
==========================================
      ORGANIZADOR DE ARQUIVOS
==========================================

Origem:
C:\Users\PC Gamer\Desktop\Teste

Destino:
C:\Users\PC Gamer\Desktop\teste 2

📦 foto.jpg -> C:\Users\PC Gamer\Desktop\teste 2\Imagens\foto.jpg
📦 relatorio.pdf -> C:\Users\PC Gamer\Desktop\teste 2\Documentos\relatorio.pdf

==========================================
✅ 2 arquivo(s) organizado(s).
==========================================

📂 Arquivos enviados para:
C:\Users\PC Gamer\Desktop\teste 2

📝 Log:
C:\Users\PC Gamer\Desktop\teste 2\organizador_log.txt
```

---

## 🧠 Como funciona (fluxo interno)

1. Verifica se a pasta de origem (`--path` ou `PASTA_ORIGEM_PADRAO`) existe. Se não existir, exibe erro e encerra.
2. Cria a `PASTA_DESTINO`, caso ainda não exista.
3. Lista apenas os **arquivos** que estão diretamente dentro da pasta de origem (ignora subpastas).
4. Para cada arquivo:
   - Identifica a extensão (`.jpg`, `.pdf` etc.).
   - Descobre a categoria correspondente pelo dicionário `CATEGORIAS` (ou usa `"Outros"` se não encontrar).
   - Cria a subpasta da categoria dentro de `PASTA_DESTINO`, se necessário.
   - Verifica se já existe um arquivo com o mesmo nome no destino; se existir, gera um novo nome com sufixo (`_1`, `_2`...).
   - Move o arquivo com `shutil.move`.
   - Registra a movimentação no console e no arquivo de log.
5. Ao final, exibe um resumo com o total de arquivos organizados.

---

## ⚠️ Observações e limitações

- O script **move** os arquivos (não copia) — a operação não pode ser desfeita automaticamente. Recomendado testar primeiro em uma pasta de exemplo.
- Não organiza arquivos dentro de subpastas da origem, apenas os que estão no primeiro nível.
- Os caminhos padrão (`PASTA_ORIGEM_PADRAO` e `PASTA_DESTINO`) estão fixos para o ambiente Windows do autor original — devem ser ajustados para o seu computador antes de usar.
- Se a pasta de origem estiver vazia, o script apenas informa e encerra sem erro.

---

## 🚀 Possíveis melhorias futuras

- Suporte a `--destino` como argumento de linha de comando (hoje é fixo no código).
- Modo "cópia" em vez de "mover", como opção.
- Interface gráfica (GUI) simples.
- Organização também por data (ano/mês) dentro de cada categoria.
