import pathlib
import platform

def mainpath():
    if platform.system() == "Windows":
        f = "C:\\Users"
    elif platform.system() == "Darwin":
        f = "/Users"
    elif platform.system() == "Linux":
        f = None
    else:
        print("System not found!")
    return pathlib.Path(f).glob('**/*') 


def search(path, file):
    for x in path:
        if (x.name == file):
            return x

if __name__ == "__main__":
    m = mainpath()
    fname = search(m, "stockphoto.jpg")
    print(fname)
    print("Done")
