import pydicom 
from aspose.imaging import Image 
import os

# Defina o diretório raiz onde estão os arquivos DICOM
dicom_root_dir = r"C:\Users\mathe\Music\arquivos_Tar"
output_root_dir = r"C:\Users\mathe\Music\dicom_comp"

# Função para processar cada arquivo DICOM sem redimensionar
def process_dicom_file(input_file, output_file):
    try:
        # Carrega a imagem a partir do arquivo DICOM
        with Image.load(input_file) as image:
            # Apenas salva a imagem no formato desejado sem redimensionar
            image.save(output_file)
            print(f"O arquivo foi salvo {output_file} com sucesso!")
    except Exception as e:
        print(f"Erro ao processar o arquivo {input_file}: {e}")

# Função para verificar se o arquivo é DICOM
def is_dicom_file(file_path):
    try:
        # Tenta abrir o arquivo usando o pydicom
        pydicom.dcmread(file_path)
        return True
    except Exception:
        return False

# Percorre todas as subpastas e arquivos do diretório raiz
for root, dirs, files in os.walk(dicom_root_dir):
    for file in files:
        input_file = os.path.join(root, file)
        
        # Verifica se o arquivo é um arquivo DICOM
        if file.lower().endswith('.dcm') or is_dicom_file(input_file):
            # Cria o caminho do diretório de saída correspondente
            relative_path = os.path.relpath(root, dicom_root_dir)
            output_dir = os.path.join(output_root_dir, relative_path)
            os.makedirs(output_dir, exist_ok=True)
            
            # Nome do arquivo de saída para o arquivo comprimido
            output_file = os.path.join(output_dir, file)
            
            try:
                process_dicom_file(input_file, output_file)
            except Exception as e:
                print(f"Erro ao processar o arquivo {input_file}: {e}")
