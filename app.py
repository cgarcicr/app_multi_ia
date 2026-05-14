import gradio as gr
from transformers import pipeline
from dotenv import load_dotenv
import os

# 3. Predicción de palabras faltantes (Fill-mask)
fill_mask = pipeline("fill-mask")
def fill_mask_tab(text):
    try:
        results = fill_mask(text)
        if not results:
            return "No predictions."
        return '\n'.join([f"{r['sequence']} (score: {r['score']:.2f})" for r in results])
    except Exception as e:
        return f"Error: {str(e)}"
tab_fillmask = gr.Interface(
    fn=fill_mask_tab,
    inputs=gr.Textbox(label="Frase con <mask>"),
    outputs="text",
    title="Predicción de palabra faltante (Fill-mask)",
    description="""
    **¿Qué hace?** Predice la(s) palabra(s) más probable(s) para el lugar donde aparece <mask> en la frase.\n\n**Importante:** Debes escribir exactamente mask (con los signos mayor que y menor que) en la frase.\n\n**Nota:** Los modelos funcionan óptimamente con textos en inglés.\n\n**Ejemplo:** The capital of France is <mask>
    """
)

# Cargar variables de entorno
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "<TU_API_KEY_AQUI>")

# 1. Analizador de sentimiento (HuggingFace)
sentiment_analyzer = pipeline("sentiment-analysis")
def sentiment_tab(text):
    result = sentiment_analyzer(text)[0]
    return f"Label: {result['label']}, Score: {result['score']:.2f}"



# 3. Extracción de entidades (NER)
ner_pipeline = pipeline("ner")
def ner_tab(text):
    entities = ner_pipeline(text)
    if not entities:
        return "No entities found."
    return "\n".join([f"{e['word']} ({e['entity']}, score: {e['score']:.2f})" for e in entities])

# Interfaz Gradio con tabs

tab1 = gr.Interface(
    fn=sentiment_tab,
    inputs=gr.Textbox(label="Texto a analizar"),
    outputs="text",
    title="Análisis de Sentimiento",
    description="""
    **¿Qué hace?** Detecta si el texto expresa un sentimiento positivo o negativo.\n\n**Nota:** Los modelos funcionan óptimamente con textos en inglés. Los resultados en otros idiomas pueden no ser precisos.\n\n**Ejemplo:**\nI love this new phone, it works perfectly and the battery lasts all day!
    """
)



tab3 = gr.Interface(
    fn=ner_tab,
    inputs=gr.Textbox(label="Texto para NER"),
    outputs="text",
    title="Extracción de entidades (NER)",
    description="""
    **¿Qué hace?** Extrae entidades nombradas como personas, lugares u organizaciones del texto.\n\n**Nota:** Los modelos funcionan óptimamente con textos en inglés. Los resultados en otros idiomas pueden no ser precisos.\n\n**Ejemplo:**\nBarack Obama was born in Hawaii and became the president of the United States.
    """
)

demo = gr.TabbedInterface([tab1, tab3, tab_fillmask], ["Sentimiento", "Entidades", "Fill-mask"])


def main():
    demo.launch()

if __name__ == "__main__":
    main()