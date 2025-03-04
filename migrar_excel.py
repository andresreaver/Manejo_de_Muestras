import pandas as pd
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gestion_muestras.settings")
django.setup()

from muestras_balalaika.models import Registro

archivo_excel = "C:/Users/nd.textiles/PycharmProjects/DjangoProject/REPORTE MUESTRAS N.D - MERCADEO 2024.xlsx"

df=pd.read_excel(archivo_excel, engine='openpyxl')

def limpiar_color(valor):
    try:
        return int(valor)
    except:
        return 9999

df['COLOR'] = df['COLOR'].apply(lambda x: limpiar_color(x) if pd.notna(x) else 9999)
df['M ENVIADOS'] = df['M ENVIADOS'].fillna(0)
df['KG ENVIADOS'] = df['KG ENVIADOS'].fillna(0)
df['TIPO'] = df['TIPO'].fillna('0')
df['FECHA SOLICITUD'] = pd.to_datetime(df['FECHA SOLICITUD'], errors='coerce')

columnas_fecha = ['FECHA DE ENVIO', 'FECHA DE LLEGADA', 'FECHA REMISION']

for col in columnas_fecha:
    df[col] = pd.to_datetime(df[col], errors='coerce')
    df[col] = df[col].fillna(df['FECHA SOLICITUD'])



print(df[df['FECHA SOLICITUD'].isna()])
print(df.isna().sum())

print(df['TIPO'].unique())  # Ver los valores únicos en la columna
print(df[df['TIPO'].str.len() > 3])  # Ver filas con valores más largos de 3 caracteres


columnas_nulas = ['CLIENTE', 'HDR', 'TIPO', 'REMISION', 'DOC.SAG']

for col in columnas_nulas:
    df[col] = df[col].fillna('NO DEFINIDO')  # Si son cadenas de texto

df.rename(columns={
    "FECHA SOLICITUD" : "fecha_solicitud",
    "CLIENTE" : "cliente",
    "COMERCIAL" : "comercial",
    "REFERENCIA" : "referencia",
    "COLOR" : "color",
    "M SOLICITADOS" : "metros_solicitados",
    "M ENVIADOS" : "metros_enviados",
    "KG ENVIADOS" : "kg_enviados",
    "HDR": "hdr",
    "TIPO" : "tipo",
    "ESTADO" : "estado",
    "FECHA DE ENVIO" : "fecha_envio",
    "FECHA DE LLEGADA" : "fecha_llegada",
    "REMISION" : "remision",
    "FECHA REMISION" : "fecha_remision",
    "DOC.SAG": "doc_sag",
}, inplace=True)

df= df.where(pd.notna(df), None)

registros_creados = []
for _, row in df.iterrows():
    registro = Registro(
        fecha_solicitud = row["fecha_solicitud"],
        cliente = row["cliente"],
        comercial = row["comercial"],
        referencia = row["referencia"],
        color = row["color"],
        metros_solicitados = row["metros_solicitados"],
        metros_enviados = row["metros_enviados"],
        kg_enviados = row["kg_enviados"],
        hdr = row["hdr"],
        tipo = row["tipo"],
        estado = row["estado"],
        fecha_envio = row["fecha_envio"],
        fecha_llegada = row["fecha_llegada"],
        remision = row["remision"],
        fecha_remision = row["fecha_remision"],
        doc_sag = row["doc_sag"]
    )
    registros_creados.append(registro)

Registro.objects.bulk_create(registros_creados)

print(f"{len(registros_creados)} registros importados exitosamente")


