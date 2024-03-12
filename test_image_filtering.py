"""" Tarea 5
Autores: Laura Sofia Garza Villarreal
Contacto: laura.garzav@udem.edu
Organizacion: Universidad de Monterrey
Fecha de entrega: 12/03/2023"""

# Importar las bibliotecas necesarias
import cv2
import numpy as np
import argparse
import cvlib as cvl

# Definir una función para analizar los datos del usuario desde la línea de comandos
def parse_user_data():
    # Crear un objeto ArgumentParser con una descripción
    parser = argparse.ArgumentParser(description='Apply image filtering')
    # Agregar un argumento para la ruta de la imagen de entrada
    parser.add_argument('--input_image', 
                        type=str, 
                        required = True,
                        help='Input image to be filtered')
    # Analizar los argumentos proporcionados por el usuario
    return parser.parse_args()

# Definir una función para cargar una imagen desde un archivo
# def load_image(filename):
    # Leer la imagen desde el archivo especificado
    # img = cv2.imread(filename)
    # Verificar si la imagen se cargó correctamente
    # if img is None:
        # Imprimir un mensaje de error y salir del programa
        # print("Error: Unable to load image.")
        # exit()
    # Devolver la imagen cargada
    # return img

# Definir una función para aplicar un filtro de medina a una imagen usando OpenCV
def median_filter(img):
    median_image = cv2.medianBlur(img, 5)
    # Devolver la imagen con el filtro de mediana aplicado
    return median_image

# Definir una función para aplicar un filtro de promedio a una imagen usando OpenCV
def average_filter(img):
    average_image = cv2.blur(img, (5, 5))
    # Devolver la imagen con el filtro de promedio aplicado
    return average_image

# Definir una función para aplicar un filtro Gaussiano a una imagen usando OpenCV
def gaussian_filter(img):
    gaussian_image = cv2.GaussianBlur(img, (5, 5), 0)
    # Devolver la imagen con el filtro de promedio aplicado
    return gaussian_image

# Definir una función para visualizar una imagen en una ventana
def visualise_image(img, title):
    # Mostrar la imagen en una ventana con el título especificado
    cv2.imshow(title, img)
    # Esperar un milisegundo para asegurar que la ventana se cree antes de cambiar su tamaño
    cv2.waitKey(1)

# Definir una función para cerrar todas las ventanas abiertas
def close_windows():
    # Esperar indefinidamente hasta que se presione una tecla
    cv2.waitKey(0)
    # Cerrar todas las ventanas
    cv2.destroyAllWindows()

# Definir una función para ejecutar el proceso completo de filtrado de imágenes
def run_pipeline():
    # Analizar los argumentos proporcionados por el usuario
    args = parse_user_data()
    # Obtener la ruta de la imagen de entrada desde los argumentos analizados
    input_image = args.input_image

    # Cargar la imagen de entrada desde el archivo
    # img = load_image(input_image)
    img = cvl.read_image(args.input_image)

    # Directorio para guardar las imagenes
    import os
    output_dir = "Filtered_images"
    os.makedirs(output_dir, exist_ok=True)

    # Aplicar median filter a la imagen
    img_median = median_filter(img)
    cv2.imwrite(os.path.join(output_dir, "median_immage.jpg"), img_median)

    # Aplicar average filter a la imagen
    img_average = average_filter(img)
    cv2.imwrite(os.path.join(output_dir, "average_immage.jpg"), img_average)

    # Aplicar Gaussian filter a la imagen
    img_gaussian = gaussian_filter(img)
    cv2.imwrite(os.path.join(output_dir, "gaussian_immage.jpg"), img_gaussian)

    # Visualizar las imagenes
    ventana = (350,350)
    # Visualizar la imagen de entrada
    cv2.namedWindow("Input Image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Input Image", ventana)
    cv2.imshow("Input Image", img)
    cv2.imwrite(os.path.join(output_dir, "input_immage.jpg"), img)

    # Visualizar la imagen con filtro de mediana
    cv2.namedWindow("Median Filter Image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Median Filter Image", ventana)
    cv2.imshow("Median Filter Image", img_median)

    # Visualizar la imagen con filtro de promedio
    cv2.namedWindow("Average Filter Image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Average Filter Image", ventana)
    cv2.imshow("Average Filter Image", img_average)

    # Visualizar la imagen con filtro Gaussiano
    cv2.namedWindow("Gaussian Filter Image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Gaussian Filter Image", ventana)
    cv2.imshow("Gaussian Filter Image", img_gaussian)

    # Cerrar todas las ventanas
    close_windows()
    # Imprimir un mensaje de finalización del programa
    print('Program finished!\n')

# Punto de entrada del programa
if __name__ == "__main__":
    # Ejecutar el proceso completo de filtrado de imágenes
    run_pipeline()