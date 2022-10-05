import os
import matplotlib.pyplot as plt
from termcolor import colored


def get_size_format(b, factor=1024, suffix="B"):
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"


def get_directory_size(directory):
    """Returns the `directory` size in bytes."""
    total = 0
    try:
        for entry in os.scandir(directory):
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                try:
                    total += get_directory_size(entry.path)
                except FileNotFoundError:
                    pass
    except NotADirectoryError:
        return os.path.getsize(directory)
    except PermissionError:
        return 0
    return total


def plot_pie(sizes, names):
    """Plots a pie where `sizes` is the wedge sizes and `names` """
    plt.pie(sizes, labels=names, autopct=lambda pct: f"{pct:.2f}%")
    plt.title("Different Sub-directory sizes in bytes")
    plt.show()


if __name__ == "__main__":
    import sys
    try:
        folder_path = sys.argv[1]
    except IndexError:
        print(colored("please activate the file in the valid way:", 'red'), '\npython', colored(
            '<filename>.py', 'yellow'), colored('<path to directory>', 'blue'), '\nfor example:', colored('python a.py /Users/babamatzia/Documents/GitHub', 'green'))
        exit()
    try:
        os.listdir(folder_path)
    except FileNotFoundError:
        print(colored("invalid path!", 'red'))
        exit()

    print(f'sizes of directories inside {folder_path} are:')

    directory_sizes = []
    names = []
    i = 0
    # iterate over all the directories inside this path
    for directory in os.listdir(folder_path):
        i += 1
        directory = os.path.join(folder_path, directory)
        # get the size of this directory (folder)
        directory_size = get_directory_size(directory)
        if directory_size == 0:
            continue
        directory_sizes.append(directory_size)
        names.append(os.path.basename(directory) + ": " +
                     get_size_format(directory_size))
        print(f"[{i}]\tSize of", colored(directory, 'green'),
              'is:', colored(get_size_format(directory_size), 'blue'))

    print("--------------------------------\n Total directory size:",
          get_size_format(sum(directory_sizes)))
    plot_pie(directory_sizes, names)
