import os
import numpy as np
from PIL import Image


root_directory = "Python/Pillow/Manipulação de imagens-2/fotos"
percentage_of_reduction = 50
new_file_name = root_directory[:root_directory.rfind("/")] + "/new_" + root_directory[root_directory.rfind("/"):][1:]
files = []


#Criando a pasta que receberá os arquivos
try:
    for i in os.listdir(root_directory[:root_directory.rfind("/")]):
        if i == new_file_name:
            break
        else:
            os.mkdir(new_file_name)
except:
    pass


# copiando
for image_name in os.listdir(root_directory):
    if os.path.isfile(os.path.join(root_directory, image_name)):
        image = Image.open(os.path.join(root_directory, image_name))
        image = image.resize(size=(np.array(image.size)*percentage_of_reduction/100).astype(int))
        image.save(os.path.join(new_file_name, image_name))
        

        