from utils import split_text, write_on_file
from logger import log as print
from consts import SUMMARY_PATH
from dotenv import load_dotenv
from ollama import chat
from ollama import ChatResponse
from ollama import list as models_list
import ollama
import openai as oai
import os


class Summarizer:
  def __init__(self, model='llama3.2'):
    self.model = model
    if model not in [m.model for m in models_list().models]:
      ollama.pull(model)
      
    print("~> Summarizer Initialiced ✅")
    
  
  def summarize_text(self, text_to_summarize: str, file='', method='ollama') -> str:
    match method:
      case 'ollama':
        summary = self.__summarize_text_ollama(text_to_summarize)
      
      case 'gpt':
        summary = self.__summarize_text_gpt(text_to_summarize)
        
      case _:
        raise Exception(f"Method to summarize {method} doesn't exists.")
    
    if file:
      if not file.endswith('.txt'):
        file += '.txt'
      
      write_on_file(SUMMARY_PATH + file, summary)
    
    return summary
  
  
  def __summarize_text_ollama(self, text_to_summarize: str) -> str:
    fragments = split_text(text_to_summarize)
    summary_parts = []
    
    for fragment in fragments:
      
      response: ChatResponse = chat(model=self.model, messages=[
        {
          'role': 'user',
          'content': f"Por favor, resume el siguiente fragmento de la clase, ten en cuenta que son varios fragmentos, empieza o termina en otro fragmento: {fragment}.",
        },
      ])
      
      summary = response['message']['content']
      summary_parts.append(summary)
      
      final_summary = ''.join(summary_parts)
    
    return final_summary
  
  
  def __summarize_text_gpt(self, text_to_summarize: str) -> str:
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