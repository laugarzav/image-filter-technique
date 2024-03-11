"""" Tarea 5
Autores: Laura Sofia Garza Villarreal
Contacto: laura.garzav@udem.edu
Organizacion: Universidad de Monterrey
Fecha de entrega: 12/03/2023"""

# Importar las bibliotecas necesarias
import cv2
import numpy as np
import argparse

# Definir una función para analizar los datos del usuario desde la línea de comandos
def parse_user_data():
    # Crear un objeto ArgumentParser con una descripción
    parser = argparse.ArgumentParser(description='Apply geometric transformations to an image')
    # Agregar un argumento para la ruta de la imagen de entrada
    parser.add_argument('--input_image', 
                        type=str, 
                        help='Path to the input image')
    # Analizar los argumentos proporcionados por el usuario
    return parser.parse_args()

# Definir una función para cargar una imagen desde un archivo
def read_image(filename):
    # Leer la imagen desde el archivo especificado
    img = cv2.imread(filename)
    # Verificar si la imagen se cargó correctamente
    if img is None:
        # Imprimir un mensaje de error y salir del programa
        print("Error: Unable to load image.")
        exit()
    # Devolver la imagen cargada
    return img

# Definir una función para aplicar una rotación a una imagen
def rotate_image(img):
    # Obtener las dimensiones de la imagen (número de filas y columnas)
    rows, cols, _ = img.shape
    # Crear una matriz de rotación para rotar la imagen 45 grados alrededor de su centro
    rotation_matrix = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
    # Aplicar la transformación de rotación a la imagen
    img_rotated = cv2.warpAffine(img, rotation_matrix, (cols, rows))
    # Devolver la imagen rotada
    return img_rotated

# Definir una función para aplicar una traslación a una imagen
def translate_image(img):
    # Obtener las dimensiones de la imagen (número de filas y columnas)
    rows, cols, _ = img.shape
    # Definir una matriz de traslación para mover la imagen 50 píxeles a la derecha
    translation_matrix = np.float32([[1, 0, 50], [0, 1, 0]])
    # Aplicar la transformación de traslación a la imagen
    img_translated = cv2.warpAffine(img, translation_matrix, (cols, rows))
    # Devolver la imagen trasladada
    return img_translated

# Definir una función para aplicar una reflexión a una imagen
def flip_image(img):
    # Reflejar la imagen horizontalmente (eje x)
    img_reflected = cv2.flip(img, 1)  # 1 para reflejo horizontal, 0 para reflejo vertical
    # Devolver la imagen reflejada
    return img_reflected

# Definir una función para visualizar una imagen en una ventana
def visualise_image(img, title):
    # Mostrar la imagen en una ventana con el título especificado
    cv2.imshow(title, img)
    # Esperar un milisegundo para asegurar que la ventana se cree antes de cambiar su tamaño
    cv2.waitKey(1)