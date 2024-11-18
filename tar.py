import tarfile
import pydicom
from aspose.imaging import Image
import os
from tqdm import tqdm  # Biblioteca para barra de progresso

# Diretórios de entrada e saída
tar_root_dir = r"C:\Users\mathe\Music\arquivos_Tar"  # Onde estão os arquivos .tar
dicom_root_dir = r"C:\Users\mathe\OneDrive\Desktop\tar_descompactado"  # Onde os arquivos .tar serão extraídos
output_root_dir = r"C:\Users\mathe\Music\dicom_comp"  # Onde os DICOMs processados serão salvos
error_log_path = "error_log.txt"  # Caminho do arquivo de log para erros

# Função para extrair arquivos .tar
def extract_tar_files(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    tar_files = [f for f in os.listdir(input_dir) if f.endswith('.tar')]

    # Barra de progresso para extração
    for filename in tqdm(tar_files, desc="Extraindo arquivos .tar", unit="arquivo"):
        tar_file_path = os.path.join(input_dir, filename)
        extract_dir = os.path.join(output_dir, os.path.splitext(filename)[0])  # Subpasta para cada tar
        os.makedirs(extract_dir, exist_ok=True)
        try:
            with tarfile.open(tar_file_path, 'r') as tar:
                tar.extractall(path=extract_dir)
        except Exception as e:
            print(f"\nErro ao extrair {tar_file_path}: {e}")
            with open(error_log_path, "a") as log_file:
                log_file.write(f"Erro ao extrair {tar_file_path}: {e}\n")

# Função para verificar se o arquivo é DICOM
def is_dicom_file(file_path):
    try:
        pydicom.dcmread(file_path)
        return True
    except Exception:
        return False

# Função para processar arquivos DICOM
def process_dicom_file(input_file, output_file):
    try:
        with Image.load(input_file) as image:
            image.save(output_file)
    except Exception as e:
        print(f"\nErro ao processar o arquivo {input_file}: {e}")
        with open(error_log_path, "a") as log_file:
            log_file.write(f"Erro ao processar {input_file}: {e}\n")

# Processo principal
if __name__ == "__main__":
    # Passo 1: Extrair arquivos .tar
    extract_tar_files(tar_root_dir, dicom_root_dir)

    # Passo 2: Processar arquivos DICOM extraídos
    total_files = sum(len(files) for _, _, files in os.walk(dicom_root_dir))
    processed_count = 0

    # Barra de progresso para processamento de DICOMs
    with tqdm(total=total_files, desc="Processando arquivos DICOM", unit="arquivo") as pbar:
        for root, dirs, files in os.walk(dicom_root_dir):
            for file in files:
                input_file = os.path.join(root, file)
                
                # Verifica se o arquivo é um DICOM
                if file.lower().endswith('.dcm') or is_dicom_file(input_file):
                    # Cria a estrutura de saída correspondente
                    relative_path = os.path.relpath(root, dicom_root_dir)
                    output_dir = os.path.join(output_root_dir, relative_path)
                    os.makedirs(output_dir, exist_ok=True)
                    
                    # Define o caminho do arquivo de saída
                    output_file = os.path.join(output_dir, file)
                    
                    # Processa o arquivo DICOM
                    try:
                        process_dicom_file(input_file, output_file)
                    except Exception as e:
                        print(f"\nErro ao processar o arquivo {input_file}: {e}")
                        with open(error_log_path, "a") as log_file:
                            log_file.write(f"Erro ao processar {input_file}: {e}\n")
                
                # Atualiza a barra de progresso
                pbar.update(1)

