#explorando o gerenciamento de arquivos e diretórios

# Podemos criar, renomear, e excluir arquivos e diretórios usando os módulos
# "os" e "shutil"

import os 
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# os.mkdir(ROOT_PATH / "New-Directory")

#file = open(ROOT_PATH / "new-file.txt", "w")
#file.close()

#os.rename(ROOT_PATH / "new-file.txt", ROOT_PATH / "new-name-file.txt")

#os.remove(ROOT_PATH / "new-name-file.txt")

shutil.move(ROOT_PATH / "new-file.txt", ROOT_PATH / "New-Directory" / "new-file.txt")
