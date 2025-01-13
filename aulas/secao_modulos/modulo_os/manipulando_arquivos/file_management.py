"""
os e shutil - Mover, copiar e apagar arquivos

Mover/Renomear -> shutil.move
Mover/Renomear -> os.rename

Copiar -> shutil.copy, shutil.copytree
Apagar -> os.unlink
Apagar diretório recursivamente -> shutil.rmtree
"""
import  os
import  shutil

caminho = "C:\\Users\\gholiveira\\Documents\\GitHub\\CursoPython\\aulas\\secao_modulos\\modulo_os\\manipulando_arquivos"

# criando o arquivo
with open(os.path.join(caminho, 'arquivo.txt'), 'w', encoding='utf8') as arquivo:
    arquivo.write('Bom dia pessoal')

# renomeando o arquivo
shutil.move(os.path.join(caminho, 'arquivo.txt'), os.path.join(caminho, 'renomeado.txt'))
