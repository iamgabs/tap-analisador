import os
import re
import json

from path_not_found_exception import PathNotFoundException

# imutabilidade e função pura
def __create_json(filename: str, words_info: list) -> None:
    """
    Esta função possui o conceito de imutabilidade pois não modifiquei
    os argumentos diretamente e de função pura, uma vez que ela só depende 
    dos argumentos passados
    """
    # Atualiza o nome do arquivo para ser um arquivo JSON
    new_json_file= filename.replace('.srt', '.json')

    # Cria o diretório 'resultados' se não existir
    # Obs: caso o diretórtio exista, não é um problema 
    os.makedirs('resultados', exist_ok=True)

    filepath = os.path.join('resultados', new_json_file)

    # Escrevendo as informações no arquivo JSON
    with open(filepath, 'w', encoding='utf-8') as json_file:
        json.dump(words_info, json_file, indent=4)


# imutablilidade e função pura
def __count_words(file_content: str) -> dict:
    """
    Esta função possui o conceito de imutabilidade pois não modifiquei
    os argumentos diretamente e de função pura, uma vez que ela só depende 
    dos argumentos passados
    """
    # Aplicar regex para contabilizar apenas palavras
    words = re.findall(r"\b[a-zA-Z\']+\b", file_content.lower())
    words = [x for x in words if len(x) > 1]
    word_count = {}
    # OBS: eu verifico se a palavra já existe no dicionário
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


# currying, alta ordem, composição de funções e recursão
def readf_by_extension(path: str = '.', extension: str = 'txt') -> callable:
    """
    Nesta função utilizo o conceito de função de alta ordem 
    pois ela retorna outra função como resultado e de currying pois cada função 
    recebe apenas um argumento de acordo com  uma função superior que possui mais
    E composição de funções onde utilizo de uma função para compr outra
    """

    def read_files(extension: str) -> dict:
        """
        Nesta função utilizo o conceito de recursão para cada arquivo
        ela deve repetir o processo de leitura e criação 
        """
        output = {}

        # Verifico se o path é realmente um path válido
        if not os.path.isdir(path):
            raise PathNotFoundException('The path couldn\'t be identified')

        def readf(file: str) -> None:
            # Conceito de nonlocal - explicar ao pessoal
            nonlocal output

            # É necessário verificar se o arquivo termina com a extensão especificada
            # no caso, arquivos .srt
            if file.endswith(extension):
                current_str_file = os.path.join(path, file)
                
                # operaçãod e leitura no arquivo
                with open(current_str_file, 'r') as curr:
                    words = __count_words(curr.read())

                # list comprehension se assemelha com o lambda 
                list_words = [{"palavra": word, "frequencia": count} for word, count in words.items()]
                sorting = sorted(list_words, key=lambda item: item["frequencia"], reverse=True) # conceito de currying "implícito"
                
                output[file] = sorting

                # Escrever arquivo JSON
                __create_json(file, output[file])

        for files in os.listdir(path):
            readf(files)

        return output

    return read_files(extension)



