import os

path = './0/'


def format(id):
    if id < 10:
        return "00" + str(id)
    elif id < 100:
        return "0" + str(id)
    else:
        return str(id)


for id, file in enumerate(os.listdir(path)):
    filename = format(id) + ".png"
    os.rename(os.path.join(path, file), os.path.join(path, filename))
