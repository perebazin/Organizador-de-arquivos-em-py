# 📂 Organizador de Arquivos

Script em Python que organiza automaticamente os arquivos de uma pasta (como `Downloads`) em subpastas por categoria — Imagens, Documentos, Vídeos, Áudios, Compactados, Instaladores e Código.

Chega de pasta de Downloads bagunçada! 🎉

## ✨ Funcionalidades

- Classifica arquivos automaticamente pela extensão
- Cria as subpastas de destino caso não existam
- Evita sobrescrever arquivos com nomes repetidos (`foto.jpg`, `foto_1.jpg`, `foto_2.jpg`...)
- Modo simulação (`--dry-run`) para ver o que seria feito sem mover nada de verdade
- Gera um log (`organizador_log.txt`) com tudo que foi movido, incluindo data e hora

## 📁 Categorias padrão

| Categoria | Extensões |
|---|---|
| Imagens | `.jpg` `.jpeg` `.png` `.gif` `.webp` `.svg` |
| Documentos | `.pdf` `.docx` `.doc` `.txt` `.xlsx` `.pptx` `.csv` |
| Videos | `.mp4` `.mov` `.avi` `.mkv` |
| Audios | `.mp3` `.wav` `.flac` |
| Compactados | `.zip` `.rar` `.7z` `.tar` `.gz` |
| Instaladores | `.exe` `.msi` `.dmg` `.apk` |
| Codigo | `.py` `.js` `.html` `.css` `.json` |

Arquivos com extensões não listadas vão para a pasta `Outros`.

## 🚀 Como usar

### Pré-requisitos

- Python 3.8 ou superior (não usa nenhuma biblioteca externa)

### Instalação

```bash
git clone https://github.com/seu-usuario/organizador-arquivos.git
cd organizador-arquivos
```

### Execução

Organizar a pasta Downloads (padrão):

```bash
python organizador_arquivos.py
```

Organizar uma pasta específica:

```bash
python organizador_arquivos.py --path "/caminho/da/sua/pasta"
```

Simular antes de organizar de verdade (recomendado na primeira vez):

```bash
python organizador_arquivos.py --path ~/Downloads --dry-run
```

## 📝 Exemplo de saída

```
📦 relatorio.pdf movido para Documentos/relatorio.pdf
📦 foto_ferias.jpg movido para Imagens/foto_ferias.jpg
📦 instalador.exe movido para Instaladores/instalador.exe

✅ Concluído! 3 arquivo(s) organizado(s).
📝 Log salvo em: organizador_log.txt
```

## 🛠️ Personalizando categorias

Basta editar o dicionário `CATEGORIAS` no início do arquivo `organizador_arquivos.py` para adicionar, remover ou alterar categorias e extensões:

```python
CATEGORIAS = {
    "Imagens": [".jpg", ".jpeg", ".png"],
    "MinhaCategoria": [".xyz"],
}
```

## 💡 Ideias futuras

- [ ] Suporte a agendamento automático (rodar todo dia em um horário)
- [ ] Modo "assistir pasta" em tempo real (com `watchdog`)
- [ ] Interface gráfica simples
- [ ] Organização por data de criação/modificação

## 📄 Licença

Este projeto está sob a licença MIT — sinta-se livre para usar, modificar e distribuir.
