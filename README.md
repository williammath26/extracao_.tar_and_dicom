# Processamento de Arquivos DICOM Extraídos de Arquivos .tar

Este projeto tem como objetivo extrair arquivos DICOM contidos em arquivos compactados no formato .tar, processá-los e salvá-los em um diretório de destino. O processamento é realizado utilizando a biblioteca Aspose.Imaging para salvar as imagens em outro formato de imagem (sem redimensionamento). Além disso, é utilizado o pydicom para verificar a validade dos arquivos DICOM antes de serem processados.

## Funcionalidades

- Extração de Arquivos .tar: Extração automática de arquivos compactados em formato .tar de um diretório de entrada.
- Processamento de Arquivos DICOM: Verificação e processamento de arquivos DICOM utilizando Aspose.Imaging.
- Barra de Progresso: Acompanhe o progresso tanto na extração dos arquivos .tar quanto no processamento dos arquivos DICOM.
- Log de Erros: Erros durante a extração ou processamento são registrados em um arquivo de log (error_log.txt), permitindo análise posterior.

## Pré-requisitos

- Python 3.12
- Bibliotecas necessárias:
   - **tarfile** (biblioteca padrão do Python)
   - **pydicom** (para verificar e manipular arquivos DICOM)
   - **aspose-imaging** (para salvar os arquivos DICOM processados)
   - **tqdm** (para a barra de progresso)
 Você pode instalar as bibliotecas necessárias usando o pip:
  pip install pydicom aspose-imaging tqdm


## Como Usar

1. Diretório de Arquivos .tar: O diretório onde os arquivos .tar comprimidos estão localizados.

2. Diretório de Extração: O diretório onde os arquivos DICOM extraídos dos .tar serão salvos.

3. Diretório de Saída: O diretório onde os arquivos DICOM processados serão salvos.
4. Modifique os caminhos das variáveis no script de acordo com seus diretórios locais
```
tar_root_dir = r"C:\Users\mathe\Music\arquivos_Tar"  # Onde estão os arquivos .tar
dicom_root_dir = r"C:\Users\mathe\Music\arquivos_Tar_extracao"  # Onde os arquivos .tar serão extraídos
output_root_dir = r"C:\Users\mathe\Music\dicom_comp"  # Onde os DICOMs processados serão salvos"
```

## Passo 2: Execução
Execute o script Python diretamente:
python nome_do_script.py

O script irá:
Extrair os arquivos .tar.
Processar os arquivos DICOM extraídos.
Salvar os arquivos processados no diretório de saída

##Logs de Erros
Se ocorrerem erros durante a extração ou processamento, eles serão registrados no arquivo error_log.txt. 
Isso permite que você verifique quais arquivos causaram problemas sem interromper o processo de outros arquivos.
## Exemplo de Execução
$ python processar_dicom.py
Extraindo arquivos .tar: 100%|██████████| 10/10 [00:05<00:00,  1.80arquivo/s]
Processando arquivos DICOM: 100%|██████████| 150/150 [00:30<00:00,  5.00arquivo/s]

