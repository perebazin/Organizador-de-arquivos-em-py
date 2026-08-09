"""
Organizador de Arquivos
------------------------
Organiza automaticamente os arquivos de uma pasta (ex: Downloads) em
subpastas por categoria (Imagens, Documentos, Vídeos, etc).

Uso:
    python organizador_arquivos.py --path ~/Downloads
    python organizador_arquivos.py --path ~/Downloads --dry-run
"""

import argparse
import shutil
from pathlib import Path
from datetime import datetime

# Mapa de categorias -> extensões de arquivo
CATEGORIAS = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audios": [".mp3", ".wav", ".flac"],
    "Compactados": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Instaladores": [".exe", ".msi", ".dmg", ".apk"],
    "Codigo": [".py", ".js", ".html", ".css", ".json"],
}

LOG_FILE = "organizador_log.txt"


def escrever_log(mensagem: str) -> None:
    """Adiciona uma linha com data/hora ao arquivo de log."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {mensagem}\n")


def encontrar_categoria(extensao: str) -> str:
    """Retorna o nome da categoria correspondente a uma extensão, ou 'Outros'."""
    for categoria, extensoes in CATEGORIAS.items():
        if extensao in extensoes:
            return categoria
    return "Outros"


def caminho_sem_conflito(destino: Path) -> Path:
    """
    Se já existir um arquivo com esse nome no destino, adiciona um
    contador ao final (ex: foto.jpg -> foto_1.jpg) para não sobrescrever.
    """
    if not destino.exists():
        return destino

    contador = 1
    novo_destino = destino
    while novo_destino.exists():
        novo_nome = f"{destino.stem}_{contador}{destino.suffix}"
        novo_destino = destino.with_name(novo_nome)
        contador += 1
    return novo_destino


def organizar(pasta: str, dry_run: bool = False) -> None:
    """
    Percorre todos os arquivos da pasta informada e move cada um
    para a subpasta da categoria correspondente.

    dry_run=True apenas mostra o que seria feito, sem mover nada.
    """
    pasta = Path(pasta).expanduser()

    if not pasta.exists():
        print(f"❌ A pasta '{pasta}' não existe.")
        return

    arquivos = [item for item in pasta.iterdir() if item.is_file()]

    if not arquivos:
        print("✅ Nenhum arquivo solto para organizar.")
        return

    total_movidos = 0

    for arquivo in arquivos:
        extensao = arquivo.suffix.lower()
        categoria = encontrar_categoria(extensao)

        pasta_destino = pasta / categoria
        destino_final = caminho_sem_conflito(pasta_destino / arquivo.name)

        if dry_run:
            print(f"[SIMULAÇÃO] {arquivo.name} -> {categoria}/")
            continue

        pasta_destino.mkdir(exist_ok=True)
        shutil.move(str(arquivo), str(destino_final))

        mensagem = f"{arquivo.name} movido para {categoria}/{destino_final.name}"
        print(f"📦 {mensagem}")
        escrever_log(mensagem)
        total_movidos += 1

    if not dry_run:
        print(f"\n✅ Concluído! {total_movidos} arquivo(s) organizado(s).")
        print(f"📝 Log salvo em: {LOG_FILE}")


def main():
    parser = argparse.ArgumentParser(
        description="Organiza arquivos de uma pasta em subpastas por tipo."
    )
    parser.add_argument(
        "--path",
        type=str,
        default="~/Downloads",
        help="Caminho da pasta a organizar (padrão: ~/Downloads)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Mostra o que seria feito, sem mover nenhum arquivo de verdade",
    )

    args = parser.parse_args()
    organizar(args.path, dry_run=args.dry_run)


if __name__ == "__main__":
    main()