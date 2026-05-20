from functions.get_files_info import get_files_info


def test_get_files_info(working_directory: str, directory: str = ".") -> None:
    dir_name = "current directory" if directory == "." else f"'{directory}'"
    print(f"Result for {dir_name}:")

    result = get_files_info(working_directory, directory)
    if "Error:" in result:
        print(f"    {result}")
    else:
        for line in result.splitlines():
            print(f"  {line}")

if __name__ == "__main__":
    test_get_files_info("calculator", ".")
    test_get_files_info("calculator", "pkg")
    test_get_files_info("calculator", "/bin")
    test_get_files_info("calculator", "../")
    test_get_files_info("calculator", "main.py")
