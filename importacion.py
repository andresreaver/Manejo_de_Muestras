import pandas as pd
from apps.clientes.models import Cliente
from apps.muestras.models import COMERCIAL_CHOICES
from django.conf import settings

excel_path = "C:/Users/nd.textiles/Downloads/clientes_Balalaika.xlsx"

df = pd.read_excel(excel_path, sheet_name='Hoja1')

for _, row in df.iterrows():
    Cliente.objects.get_or_create(
        nombre=row['nombre'].strip(),
        defaults={
            'estado': row['estado'],
            'nit': str(row['nit']),
            'nombre_contacto': row['nombre_contacto'],
            'direccion': row['direccion'],
            'ciudad':row['ciudad'],
            'departamento': row['departamento'],
            'pais': row['pais'],
            'telefono':str(row['telefono']),
            'celular':str(row['celular']),
            'email':row['email'],
            'observaciones': row['observaciones'],
            'comercial': row['comercial'],
        }
    )

