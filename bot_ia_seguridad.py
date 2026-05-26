import pandas as pd
import g4f

print("🤖 Iniciando NovaDigitalIA Automation Bot...")

# 1. Los datos desordenados que nos mandó el supuesto cliente
datos_recibidos = [
    "Reclamo de cliente: El sistema se cae seguido y la contraseña se ve en texto plano en la URL.",
    "Consulta comercial: Hola, quería saber el precio de sus servicios de automatización de datos.",
    "Alerta de seguridad: Detectamos un intento de ingreso no autorizado desde una IP sospechosa.",
    "Nota interna: Acordarse de comprar café para la oficina técnica."
]

reporte_procesado = []

print("\n🧠 Conectando con el cerebro de IA para procesar los datos...")

# 2. El bucle automático: la IA procesa cada dato por separado sin que vos hagas nada
for item in datos_recibidos:
    print(f"-> Analizando: '{item[:30]}...'")
    
    # Le armamos la orden (Prompt) de forma profesional para que actúe como experto
    instruccion = f"""
    Actúa como un experto en Ciberseguridad y Automatización. 
    Analiza el siguiente texto y clasifícalo en una sola palabra como: 'URGENTE', 'SEGURIDAD' o 'GENERAL'. 
    Luego, da una breve recomendación técnica de 1 sola frase.
    Texto a analizar: "{item}"
    Responde estrictamente en este formato, separado por una barra:
    Clasificación / Recomendación
    """
    
    try:
        # La IA de g4f genera la respuesta automática usando modelos públicos
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_4,
            messages=[{"role": "user", "content": instruccion}],
        )
        
        # Guardamos lo que nos respondió la IA y lo acomodamos
        resultado = response.strip()
        clasificacion, recomendacion = resultado.split("/")
    except Exception:
        # Por si el servidor se satura, ponemos una respuesta de respaldo automática
        clasificacion = "REVISAR"
        recomendacion = "Requiere auditoría manual de NovaDigitalIA."

    reporte_procesado.append({
        "Información Original": item,
        "Análisis de IA (Prioridad)": clasificacion.strip(),
        "Solución Técnica Recomendada": recomendacion.strip()
    })

# 3. Guardamos el laburo terminado en el Excel del empresario
df = pd.DataFrame(reporte_procesado)
df.to_excel("/sdcard/Download/Reporte_Automatizado_IA.xlsx", index=False)

print("\n✨ ¡Operación completada con éxito!")
print("📁 El archivo 'Reporte_Automatizado_IA.xlsx' ya está guardado en tus Descargas listo para entregar.")
