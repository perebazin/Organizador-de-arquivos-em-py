

import argparse
import shutil
from pathlib import Path
from datetime import datetime


# ============================================================
# PASTA DE ORIGEM PADRÃO
# ============================================================
# Usada quando você roda pelo botão Run (sem passar --path).
# Troque pelo caminho que você quer organizar por padrão.

PASTA_ORIGEM_PADRAO = r"C:\Users\PC Gamer\Desktop\Teste"


# ============================================================
# CATEGORIAS
# ============================================================

CATEGORIAS = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audios": [".mp3", ".wav", ".flac"],
    "Compactados": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Instaladores": [".exe", ".msi", ".dmg", ".apk"],
    "Codigo": [".py", ".js", ".html", ".css", ".json"],
}


# ============================================================
# PASTA DE DESTINO
# ============================================================

PASTA_DESTINO = Path(r"C:\Users\PC Gamer\Desktop\teste 2")


# ============================================================
# LOG
# ============================================================

LOG_FILE = PASTA_DESTINO / "organizador_log.txt"


def escrever_log(mensagem: str) -> None:
    """Adiciona uma linha com data e hora ao arquivo de log."""

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {mensagem}\n")


# ============================================================
# ENCONTRAR CATEGORIA
# ============================================================

def encontrar_categoria(extensao: str) -> str:
    """Retorna a categoria correspondente à extensão."""

    for categoria, extensoes in CATEGORIAS.items():
        if extensao in extensoes:
            return categoria

    return "Outros"


# ============================================================
# EVITAR ARQUIVOS COM MESMO NOME
# ============================================================

def caminho_sem_conflito(destino: Path) -> Path:
    """
    Se já existir um arquivo com o mesmo nome,
    adiciona _1, _2, _3 etc.
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


# ============================================================
# ORGANIZAR ARQUIVOS
# ============================================================

def organizar(pasta: str) -> None:

    # Pasta onde estão os arquivos
    pasta = Path(pasta).expanduser()

    # Verifica se a pasta de origem existe
    if not pasta.exists():

        print(f"❌ A pasta de origem não existe:")
        print(pasta)

        return

    # Cria a pasta de destino caso ela não exista
    PASTA_DESTINO.mkdir(parents=True, exist_ok=True)

    # Pega somente os arquivos diretamente dentro da pasta
    arquivos = [
        item
        for item in pasta.iterdir()
        if item.is_file()
    ]

    if not arquivos:

        print("✅ Nenhum arquivo encontrado na pasta de origem.")

        return

    total_movidos = 0

    print()
    print("==========================================")
    print("      ORGANIZADOR DE ARQUIVOS")
    print("==========================================")
    print()
    print(f"Origem:")
    print(pasta)
    print()
    print(f"Destino:")
    print(PASTA_DESTINO)
    print()

    for arquivo in arquivos:

        # Descobre a extensão
        extensao = arquivo.suffix.lower()

        # Descobre a categoria
        categoria = encontrar_categoria(extensao)

        # Cria a pasta da categoria
        pasta_categoria = PASTA_DESTINO / categoria

        pasta_categoria.mkdir(
            parents=True,
            exist_ok=True
        )

        # Define o destino final
        destino_final = caminho_sem_conflito(
            pasta_categoria / arquivo.name
        )

        try:

            # Move o arquivo
            shutil.move(
                str(arquivo),
                str(destino_final)
            )

            mensagem = (
                f"{arquivo.name} -> "
                f"{destino_final}"
            )

            print(f"📦 {mensagem}")

            escrever_log(mensagem)

            total_movidos += 1

        except Exception as erro:

            print(
                f"❌ Erro ao mover {arquivo.name}: {erro}"
            )

    print()
    print("==========================================")
    print(f"✅ {total_movidos} arquivo(s) organizado(s).")
    print("==========================================")
    print()
    print(f"📂 Arquivos enviados para:")
    print(PASTA_DESTINO)
    print()
    print(f"📝 Log:")
    print(LOG_FILE)


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

def main():

    parser = argparse.ArgumentParser(
        description="Organiza arquivos automaticamente por categoria."
    )

    parser.add_argument(
        "--path",
        type=str,
        default=PASTA_ORIGEM_PADRAO,   # usado se você NÃO passar --path
        help="Pasta onde estão os arquivos que serão organizados."
    )

    args = parser.parse_args()

    organizar(args.path)


# ============================================================
# INICIAR PROGRAMA
# ============================================================

if __name__ == "__main__":
    main()