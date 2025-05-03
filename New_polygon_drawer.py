import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from  fractions import Fraction


# Diccionario con los poligonos y todos sus lados
st.set_page_config(layout="wide")


polygons = {
    "Cuadrilatero": 4,
    "pentagon": 5,
    "hexagon": 6,
    "heptagon": 7,
    "octagon": 8,
    "nonagon": 9,
    "decagon": 10,
    "hendecagon": 11,
    "dodecagon": 12,
    "tridecagon": 13,
    "tetradecagon": 14,
    "pentadecagon": 15,
    "hexadecagon": 16,
    "heptadecagon": 17,
    "octadecagon": 18,
    "enneadecagon": 19,
    "icosagon": 20
}


st.title("Actividad # 4 - Tarea Geometría")
st.header("Punto # 1:  Complete la siguiente tabla que se muestra en el link adjunto")
link = "https://campusvirtual.ibero.edu.co/repositorio/Cursos-Matriz/Pregrados/Ingenieria/Pensamiento-matematico/MD/Actividad4.pdf"
st.markdown(f"[Haz clic aquí para ir a la actividad]({link})")
    
side_choice = st.number_input("De cuantos lados sera tu poligono?", min_value=4, max_value=20)
longitud_choice = st.number_input("Cual sera la longitud de los lados en CM?", min_value=20, max_value=50)


# funcion para crear el poligono a traves del modulo  Turtle()

def draw_polygon(longitud, sides):
    rad = longitud / (2 * np.sin(np.pi / sides))
    k_values = np.arange(sides)
    if sides == 4:
        angle_step = (2 * np.pi) / sides 
        angles = k_values * angle_step + (np.pi / sides)
        xs = rad * np.cos(angles)
        ys = rad * np.sin(angles)
        
        xs = np.append(xs, xs[0])
        ys = np.append(ys, ys[0])
        
        plt.plot(xs, ys)
        plt.axis("equal")
        st.pyplot(plt)
    
    else:
           
        angle_step = (2 * np.pi) / sides
        angles = k_values * angle_step + (np.pi / sides)
        
        xs = rad * np.cos(angles)
        ys = rad * np.sin(angles)
        
        xs = np.append(xs, xs[0])
        ys = np.append(ys, ys[0])
        
        plt.plot(xs, ys)
        plt.axis("equal")
        st.pyplot(plt)
    
if st.button("Draw Polygon"):
    draw_polygon(longitud_choice, side_choice)
    

def data_frame_creation(polygon_dict, longitud):
    polygon_name = []
    polygon_sides = []
    new_polygon_dict = {}
        
    for name, side in polygon_dict.items():
        polygon_name.append(name)
        polygon_sides.append(side)
        
    new_polygon_dict = {
        "Polygon Names":  polygon_name,
        "Sides": polygon_sides        
    }
    
    df = pd.DataFrame(new_polygon_dict)
    df['Suma de Angulos internos'] = (df['Sides'] - 2) * 180
    df['Suma Numero de Diagonales'] = df['Sides'] * (df['Sides'] - 3) / 2
    df['Perimetro CM'] = df['Sides'] * longitud
    df['Apotema'] = longitud / (2 * np.tan(np.pi / df['Sides']))
    df['Area CM²'] = (df['Perimetro CM'] * df['Apotema']) / 2
    df = df.round(2)
    new_df = st.dataframe(df)


if st.button("Create Data Frame"):
    data_frame_creation(polygons, longitud_choice)
        


# Punto # 4:

# Pirámide, con base rectangular, de lado 4𝑚 por 3𝑚, con una altura de 400 𝑐𝑚.
# Cono, con diámetro en la base de 3𝑚, y altura de 4000𝑚𝑚.
# Cilindro, con diámetro en la base de 3
# Esferico con diametro de 300 cm

def pyramind_area(height, side_one, side_two):
    base = side_one * side_two
    altura_lateral_1  = np.sqrt(height**2 + (side_one/2)**2)
    altura_lateral_2  = np.sqrt(height**2 + (side_two/2)**2)
    lateral_area_one = 2 * Fraction(1, 2) * side_one * altura_lateral_1
    lateral_area_two = 2 * Fraction(1, 2) * side_two * altura_lateral_2
    area_total = round((lateral_area_one + lateral_area_two) + base,2)
    
    return area_total


height_input = 400 / 100
base_one = 4
base_two = 3
base_area = base_one * base_two


resultado_piramide = pyramind_area(height_input, base_one, base_two)


st.header("Punto # 4: Se construyen cuatro tranques de diferente forma, los cuales se describen a continuación")
st.caption("Pirámide, con base rectangular, de lado 4𝑚 por 3𝑚, con una altura de 400 𝑐𝑚.")
st.caption("Cono, con diámetro en la base de 3𝑚, y altura de 4000𝑚𝑚")
st.caption("Clindro, con diametro en la base de 3000mm y altura de 0.004 km")
st.caption("Esferico con diametro de 300cm")



if st.button("Calculate Pyramid area"):
    st.write(f'La base de la piramide es de {base_one} m * {base_two} m y una altura de {int(height_input)} m')
    volumen = (base_area * height_input) / 3
    st.write(f'El area de la piramide es de {resultado_piramide} m²')
    st.write(f'El Volumen de la piramide es de {volumen} m³')
    capacidad = volumen * 1000
    st.write(f'La capacidad de la piramide en es de {capacidad} Litros')
    capacidad_mililitros = capacidad * 1000
    st.write(f'La capacidad de la piramide en ml es de {capacidad_mililitros} siendo el segundo en la lista')

    
    
    

def cono_area(diametro, inclinacion):
    radio = diametro / 2
    Generatriz = np.sqrt(radio**2 + inclinacion**2)
    area_base = np.pi * radio**2
    area_lateral = np.pi * radio * Generatriz
    cono_formula_area = area_base + area_lateral

    return cono_formula_area

diametro_input = 3
radio = diametro_input / 2
area_base = np.pi * radio**2
inclinacion_input = 4000 / 1000
resultado_cono = cono_area(diametro_input, inclinacion_input)

if st.button("Calculate Cono area"):
    st.write(f'La base del cono tiene un Diametro de {diametro_input} m y una altura de {int(inclinacion_input)} m')
    volumen_cono = round((area_base * inclinacion_input) / 3, 2)
    st.write(f'El area del cono es de {round(resultado_cono, 2)} m²')
    st.write(f'El Volumen del cono es de {volumen_cono} m³')
    capacidad_cono = round(volumen_cono * 1000, 2)
    st.write(f'La capacidad del cono es de {capacidad_cono} Litros')
    capacidad_mililitros_cono = capacidad_cono * 1000
    st.write(f'La capacidad del cono en ml es de {capacidad_mililitros_cono} siendo el ultimo en la lista')
    
    
def cilindro_area(radio, altura):
    formula_cilindro_area = (2*np.pi*radio**2) + (2*np.pi*radio*altura)
    return formula_cilindro_area

Diametro_base = int(3000 / 1000)
radio_cilindro = Diametro_base / 2
altura_cilindro = 0.004 * 1000
resultado_cilindro = cilindro_area(radio_cilindro, altura_cilindro)

if st.button("Calculate Cilindro area"):
    st.write(f'La base del cilindro tiene un diametro de {Diametro_base} m y una altura de {int(altura_cilindro)} m')
    volumen_cilindro = np.pi * radio_cilindro**2 * altura_cilindro
    st.write(f'El area del cilindro es de {round(resultado_cilindro,2)}m²')
    st.write(f'El volumen del cilindro es de {round(volumen_cilindro,2)}m³')
    capacidad_cilindro = round(volumen_cilindro * 1000, 2)
    st.write(f'La capacidad del cilindro es de {capacidad_cilindro} Litros')
    capacidad_ml_cilindro = capacidad_cilindro * 1000
    st.write(f'La capacidad del cilindro en ml es de {capacidad_ml_cilindro} siendo el primero en la lista')

    

def area_esfera(radio):
    formula_esfera = 4*np.pi*radio**2
    return formula_esfera


esfera_diametro = int(300 / 100)
esfera_radio = esfera_diametro / 2
resultado_esfera = area_esfera(esfera_radio)

if st.button("Calculate Sphere area"):
    st.write(f'La esfera tiene un diametro de {esfera_diametro}m')
    volumen_esfera = Fraction(4, 3) * np.pi * esfera_radio**3
    st.write(f'El area de la esfera es de {round(resultado_esfera, 2)}')
    st.write(f'El volumen de la esfera es de {round(volumen_esfera,2)}m³')
    capacidad_esfera = round(volumen_esfera * 1000, 2)
    st.write(f'La capacidad de la esfera {capacidad_esfera} Litros')
    capacidad_ml_esfera = capacidad_esfera * 1000
    st.write(f'La capacidad de la esfera en ml es de {capacidad_ml_esfera} siendo la tercera en la lista')
    
area_dictionary = {
    "Area_piramide": resultado_piramide,
    "Area_cono": resultado_cono,
    "Area_cilindro": resultado_cilindro,
    "Area_esfera": resultado_esfera
}



Column_1 = list(area_dictionary.keys())
Column_2 = list(area_dictionary.values())
data_list = []

for keys, values in zip(Column_1, Column_2):
    new_dict = {'Areas': keys, "Valor en m²": values}
    data_list.append(new_dict)


def create_frame():
    df = pd.DataFrame(data_list)
    df['Material necesario en cm²'] = df['Valor en m²'] * 10000
    df['Diferencia (3 Laminas)'] = 72 - df['Valor en m²']
    df['Relacion Area - Laminas'] = np.where(df["Diferencia (3 Laminas)"] > 0, "Completo", "Hace Falta Material")
    df = df.round(2)
    
    return df

area_data_frame = create_frame()

if st.button("Create new data frame"):
    area_laminas = 24 * 3
    st.write(f'El area de las 3 laminas es de {area_laminas} m²')
    Sum_areas = sum(Column_2)
    Diferencia = Sum_areas - area_laminas
    st.write(f'Para construir todas las figuras con 3 laminas de 6m * 4m cada una hacen falta {round(Diferencia, 2)} m²')
    st.dataframe(area_data_frame)    

    
    