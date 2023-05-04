import re
import unicodedata

def remove_non_ascii_chars(file_path):
    # Vérifie si le fichier est un fichier texte, SQL ou Excel
    if file_path.endswith(('.txt', '.sql')):
        with open(file_path, 'r', encoding='iso-8859-1') as f:
            data = f.read()
        # Remplace les caractères non-ASCII par leur équivalent ASCII
        new_data = ''.join(c if ord(c) < 128 else unicodedata.normalize('NFKD', c).encode('ascii', 'ignore').decode('utf-8') for c in data)
        # Enregistre le fichier avec un nouveau nom
        new_file_path = os.path.splitext(file_path)[0] + '_ascii' + os.path.splitext(file_path)[1]
        with open(new_file_path, 'w', encoding='utf-8') as f:
            f.write(new_data)

        # Affiche la modification faite dans la console
        if data != new_data:
            print(f"Le fichier {file_path} a été modifié :")
            for line_old, line_new in zip(data.splitlines(), new_data.splitlines()):
                if line_old != line_new:
                    print(f"- {line_old} => {line_new}")
    else:
        print('Format de fichier non pris en charge')


directory_path = 'Path file'

for filename in os.listdir(directory_path):
    if filename.endswith('.txt') or filename.endswith('.sql'):
        file_path = os.path.join(directory_path, filename)
        remove_non_ascii_chars(file_path)
