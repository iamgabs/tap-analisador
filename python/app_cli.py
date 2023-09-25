from read_files import readf_by_extension


if __name__ == "__main__":
    path_got: str = input("informe o path: ")
    readf_by_extension(path_got, ".srt")