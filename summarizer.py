from utils import split_text, write_on_file
from consts import SUMMARY_PATH
import openai as oai
import os


class Summarizer:
  def __init__(self, model='gpt-3.5-turbo'):
    oai.api_key = os.getenv('OPENAI_KEY')
    self.model = model
    self.context = {
      'role': 'system',
      'content': 'Eres un asistente que resume transcripciones de clases grabadas. Extrae los puntos clave de la charla, conceptos importantes y cualquier tema destacado, y presenta el resumen de forma clara y comprensible para un estudiante.'
    }
  
  def summarize_text(self, text_to_summarize: str, file='') -> str:
    fragments = split_text(text_to_summarize)
    summary_parts = []
    
    for fragment in fragments:
      
      messages = [
        self.context,  
        {'role': 'user', 'content': f"Por favor, resume el siguiente fragmento de la clase, ten en cuenta que son varios fragmentos, empieza o termina en otro fragmento: {fragment}"}
      ]
      
      response = oai.chat.completions.create(
        messages=messages,
        model=self.model
      )
      
      summary = response.choices[0].message.content
      summary_parts.append(summary)
    
    final_summary = ''.join(summary_parts)
    
    if file:
      if not file.endswith('.txt'):
        file += '.txt'
      
      write_on_file(SUMMARY_PATH + file, final_summary)
    
    return final_summary