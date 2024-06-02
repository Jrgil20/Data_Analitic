# Importar la biblioteca pandas
import pandas as pd

try:
    # Intentar leer datos de la hoja llamada '5W - RMRP 2023'
    df = pd.read_excel('5w_rmrp_2023.xlsx', sheet_name='5W - RMRP 2023')

    # Ver todos los datos del DataFrame
    print(df)
except Exception as e:
    # Si ocurre un error, imprimir el mensaje de error
    print("Ocurrió un error al leer el archivo Excel:")
    print(e)