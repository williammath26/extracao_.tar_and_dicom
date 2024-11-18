# DICOM Image Processor

Este projeto processa arquivos DICOM, validando e salvando-os em um formato compactado. Utiliza o Aspose.Imaging para manipular as imagens e a biblioteca `pydicom` para verificar a validade dos arquivos DICOM. O objetivo é navegar em um diretório contendo arquivos DICOM e salvar as imagens processadas em um diretório de saída.

## Funcionalidades

- Validação de arquivos DICOM.
- Processamento iterativo de arquivos DICOM.
- Salvamento dos arquivos processados em um diretório de saída.

## Bibliotecas Utilizadas

- `pydicom`: Para leitura e validação de arquivos DICOM.
- `Aspose.Imaging`: Para carregar e salvar imagens em diversos formatos.

## Estrutura do Código

1. **Verificação de arquivo DICOM**: A função `is_dicom_file()` tenta carregar o arquivo com a biblioteca `pydicom` e verifica sua validade.

2. **Processamento de arquivos DICOM**: A função `process_dicom_file()` utiliza o Aspose.Imaging para carregar a imagem a partir do arquivo DICOM e salvá-la no diretório de saída.

3. **Iteração pelos arquivos DICOM**: O script percorre o diretório raiz (`dicom_root_dir`), verifica os arquivos com extensão `.dcm` ou aqueles que podem ser lidos como DICOM, e processa cada um deles.

## Requisitos

- Python 3.12
- Biblioteca `pydicom`
- Biblioteca `Aspose.Imaging`

Instale os requisitos com o comando:

```bash
pip install pydicom
pip install aspose-imaging-python-net
