---
title: Multi-IA
emoji: 🤖
colorFrom: indigo
colorTo: blue
sdk: gradio
app_file: app.py
pinned: false
---
# App Multi-IA (Gradio)




## Descripción
Aplicación web con Gradio que integra tres capacidades de IA generativa:
- **Análisis de sentimiento** (HuggingFace Transformers)
	- Detecta si el texto expresa un sentimiento positivo o negativo.
	- Ejemplo: `I love this new phone, it works perfectly and the battery lasts all day!`
- **Extracción de entidades (NER)** (HuggingFace Transformers)
	- Extrae entidades nombradas como personas, lugares u organizaciones del texto.
	- Ejemplo: `Barack Obama was born in Hawaii and became the president of the United States.`
- **Predicción de palabra faltante (Fill-mask)** (HuggingFace Transformers)
	- Predice la(s) palabra(s) más probable(s) para el lugar donde aparece <mask> en la frase.
	- **Importante:** Debes escribir exactamente <mask> (con los signos < y >) en la frase. No uses [MASK], MASK ni variantes.
	- Ejemplo: `The capital of France is <mask>`

**Nota importante:** Los modelos utilizados funcionan óptimamente con textos en inglés. Los resultados en otros idiomas pueden no ser precisos.

El usuario puede elegir la operación en pestañas y ver los resultados de cada IA.



## ¿Por qué no se utiliza Gemini?

A pesar de que se generó una API key válida para Gemini (Google AI), la integración no funcionó correctamente. El error recibido fue:

```
Error: PERMISSION_DENIED: API key not valid. Please pass a valid API key.
```

Esto se debió a limitaciones de acceso y posibles restricciones en la activación del servicio para la cuenta utilizada.

Otras razones para no usar Gemini en esta app:
- **Compatibilidad:** La integración directa con Gemini no es tan sencilla como con HuggingFace Transformers, especialmente en entornos locales o sin dependencias específicas de Google.
- **Facilidad de despliegue:** HuggingFace Transformers permite ejecutar modelos de IA de manera local y sin depender de servicios externos, facilitando la portabilidad y el uso sin restricciones adicionales.

Por estas razones, todas las funciones de IA en esta app se implementan usando modelos de HuggingFace Transformers, que son de código abierto y ampliamente soportados.

---
## Tecnologías utilizadas
- Gradio
- HuggingFace Transformers
- Python


## Nota importante sobre el resumen de textos
**Nota:** Por limitaciones de la versión de transformers y compatibilidad de modelos, la app no puede realizar resumen ni traducción automática directa. Las funciones disponibles son análisis de sentimiento, clasificación de texto y question answering (QA).

## Instrucciones de instalación y ejecución local

1. Clona el repositorio y entra a la carpeta:
	```bash
	# Checklist de requisitos del proyecto

	- [x] Interfaz web (Gradio)
	- [x] Modelo de IA integrado (HuggingFace Transformers)
	- [x] Repositorio GitHub con el código
	- [ ] Deployment online (HuggingFace Spaces o Streamlit Cloud)

	git clone <URL_DEL_REPO>
	cd app_multi_ia
	```
2. Instala las dependencias:
	```bash
	pip install -r requirements.txt
	```
3. Crea un archivo `.env` con tu clave de Gemini:
	```env
	GEMINI_API_KEY=TU_CLAVE_AQUI
	```
4. Ejecuta la app:
	```bash
	python app.py
	```

## Despliegue
- [App en HuggingFace Spaces](https://huggingface.co/spaces/camangar/multi-ia)
- [Repositorio en GitHub](https://github.com/cgarcicr/app_multi_ia)
