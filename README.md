# AutoDocsWriter

## Descrição
O AutoDocsWriter é um script Python que automatiza a escrita de documentos. Ele utiliza a biblioteca `pyautogui` para emular ações do teclado e do mouse e preencher documentos de forma rápida e eficiente.

## Funcionalidades
- Automatiza a escrita de documentos.
- Escreve especificações em minúsculas em documentos.
- Permite definir a quantidade de documentos a serem preenchidos.

## Requisitos
- Python 3.x
- Biblioteca `pyautogui`

## Uso
1. Clone este repositório em sua máquina:

   ```bash
   git clone https://github.com/M4thy5/AutoDocsWriter.git
   ```

2. Navegue até o diretório clonado:

   ```bash
   cd AutoDocsWriter
   ```

3. Execute o script:

   ```bash
   python auto_docs_writer.py
   ```

4. Siga as instruções para definir a quantidade de documentos a serem preenchidos e as especificações em minúsculas que deseja incluir nos documentos.

## Exemplo de Uso
```python
# Defina a quantidade de documentos a serem preenchidos
contador_docs = int(input("Qual a quantidade de docs: ").strip())

while True:
    contador = 0
    pergunta_docs = str(input("Escreva a especificação em minúsculo!\nDigite: ").strip().upper()

    # Implemente a função principal (main) que emula as ações do teclado e do mouse.

    while contador != contador_docs:
        # Automatize a escrita nos documentos.
        contador += 1
```

## Notas
- Certifique-se de que o documento em que deseja escrever esteja ativo e em foco antes de executar o script.

## Aviso
Este script foi criado apenas para fins educacionais e de demonstração. A automação de tarefas pode ter aplicações legítimas, mas também pode ser usada de maneira indevida. Certifique-se de usá-lo de acordo com as leis e regulamentos aplicáveis e com a devida permissão, se necessário.

## Autor
[Matheus H](https://github.com/M4thy5)
