import pandas as pd
from datetime import datetime

# Diccionario para mapear tipos de movimiento
tipos_movimiento = {
    1: "Ingreso",
    2: "Click",
    3: "Consulta",
    4: "Descarga"
}

# Cargar el archivo CSV
def cargar_datos(ruta_archivo):
    try:
        df = pd.read_csv(ruta_archivo)
        return df
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta_archivo}")
        return None

# Analizar y mostrar reporte
def generar_reporte(df):
    if df is None or df.empty:
        print("No hay datos para analizar")
        return
    
    print("\n" + "="*60)
    print("REPORTE DE ANÁLISIS - COMPORTAMIENTO DE CLIENTES")
    print("="*60 + "\n")
    
    # 1. Información general
    print("📊 INFORMACIÓN GENERAL")
    print(f"Total de registros: {len(df)}")
    print(f"Usuarios únicos: {df['id_usuario'].nunique()}")
    print(f"Período analizado: {df['fecha_hora'].min()} a {df['fecha_hora'].max()}\n")
    
    # 2. Análisis por tipo de movimiento
    print("🔍 DISTRIBUCIÓN POR TIPO DE MOVIMIENTO")
    movimientos = df['tipo_movimiento'].value_counts().sort_index()
    for tipo, cantidad in movimientos.items():
        nombre = tipos_movimiento.get(tipo, "Desconocido")
        porcentaje = (cantidad / len(df)) * 100
        print(f"  {nombre}: {cantidad} ({porcentaje:.1f}%)")
    print()
    
    # 3. Análisis por origen
    print("📱 USUARIOS POR ORIGEN")
    origenes = df['origen'].value_counts()
    for origen, cantidad in origenes.items():
        porcentaje = (cantidad / len(df)) * 100
        print(f"  {origen}: {cantidad} registros ({porcentaje:.1f}%)")
    print()
    
    # 4. Elementos más interactuados
    print("👕 ELEMENTOS MÁS INTERACTUADOS")
    elementos = df['elementos_involucrados'].value_counts().head(10)
    for elemento, cantidad in elementos.items():
        print(f"  {elemento}: {cantidad} interacciones")
    print()
    
    # 5. Usuarios más activos
    print("👤 TOP 5 USUARIOS MÁS ACTIVOS")
    usuarios_activos = df['id_usuario'].value_counts().head(5)
    for ip, cantidad in usuarios_activos.items():
        print(f"  {ip}: {cantidad} acciones")
    print()
    
    # 6. Resumen estadístico
    print("📈 RESUMEN ESTADÍSTICO")
    print(f"Registros por usuario (promedio): {len(df) / df['id_usuario'].nunique():.2f}")
    print(f"Origen más común: {df['origen'].mode()[0]}")
    print(f"Movimiento más frecuente: {tipos_movimiento.get(df['tipo_movimiento'].mode()[0], 'Desconocido')}")
    print("\n" + "="*60 + "\n")

# Ejecutar análisis
if __name__ == "__main__":
    ruta = "comportamientos.csv"  # Cambiar por la ruta de tu archivo
    datos = cargar_datos(ruta)
    generar_reporte(datos)