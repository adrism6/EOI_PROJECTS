import os, zipfile, statistics, datetime, time


def get_files(backup_path: str) -> list:
    files_list: list = []
    for t in os.walk(backup_path):
        dirpath, _, files = t
        for _file in files:
            name, ext = os.path.splitext(_file)
            if ext in extensions:
                full_path = os.path.join(dirpath, _file)
                files_list.append(full_path)
    return files_list


def create_backup(backup_path: str, zip_path: str) -> int:
    t1: int = datetime.datetime.now().microsecond
    with zipfile.ZipFile(zip_path, "w") as zf:
        for files in get_files(backup_path):
            zf.write(files)
    t2: int = datetime.datetime.now().microsecond
    return t2 - t1


def backup_statistics(backup_path: str, zip_path: str) -> None:
    operation_time: int = create_backup(backup_path, zip_path)
    with zipfile.ZipFile(zip_path, "r") as zf:
        zip_info: list = zf.infolist()
        num_files: int = len(zip_info)
        sizes: list = [info.file_size for info in zip_info]
        total_size = sum(sizes)
        mean_size = statistics.mean(sizes)
        print(f"Number of files: {num_files}")
        print(f"Total size: {total_size} bytes")
        print(f"Mean size: {mean_size} bytes")
        print(f"Total time of compression: 00.00{operation_time} seconds")


def directories(backup_path: str, zip_path: str) -> None:
    """
    backup_path = directorio del que quieres hacer la copia
    zip_path = directorio donde quieres guardar la copia
    """
    while True:
        day_name: str = datetime.datetime.today().strftime("%A") + ".zip"
        zip_path_name: str = zip_path + "/" + day_name
        print(f"Created compressed archive '{zip_path_name}' from {backup_path}")
        backup_statistics(backup_path, zip_path_name)
        print("Compression done: sleeping 24 hours for the next one!")
        time.sleep(86400)


extensions = [".py", ".csv"]

directories("../eoi/02-core", "../eoi/05-libs")
