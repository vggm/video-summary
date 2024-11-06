import os
import openai
import whisper
from dotenv import load_dotenv
from utils import remove_special_characters, split_text
from audiovisual_manipulator import AudiovisualManipulator

SUMMARY_PATH = './summary-from-videos'
VIDEOS_PATH  = './videos-to-summary/'
AUDIOS_PATH  = './audios-from-videos/'
TEXTS_PATH   = './text-from-videos/'

if __name__ == '__main__':
  avm = AudiovisualManipulator()
  for _, _, files in os.walk(VIDEOS_PATH):
    for file in files:
      filename, ext = file.rsplit('.', 1)
      audio = avm.get_audio_from_filename(VIDEOS_PATH + file)
      
      output_name = remove_special_characters(filename)
      
      audio_name = output_name + '.mp3'
      avm.save_audio(audio, AUDIOS_PATH + audio_name)
      
      model = whisper.load_model('base')
      result = model.transcribe(AUDIOS_PATH + audio_name)

      with open(TEXTS_PATH + output_name + '.txt', 'w') as fwrite:
        fwrite.write(result['text'])
      
      
      load_dotenv()
      openai.api_key = os.getenv("OPENAI_KEY")
      
      context = {
        'role': 'system',
        'content': 'Eres un asistente que resume transcripciones de clases grabadas. Extrae los puntos clave de la charla, conceptos importantes y cualquier tema destacado, y presenta el resumen de forma clara y comprensible para un estudiante.'
      }
      
      fragments = split_text(result['text'])
      summary_parts = []
      
      for fragment in fragments:
        
        messages = [
          context,  
          {'role': 'user', 'content': f"Por favor, resume el siguiente fragmento de la clase: {fragment}"}
        ]
        
        response = openai.chat.completions.create(
          messages=messages,
          model='gpt-3.5-turbo'
        )
        
        summary = response.choices[0].message.content
        summary_parts.append(summary)
      
      final_summary = ''.join(summary_parts)
      with open(SUMMARY_PATH + output_name + '_summary.txt', 'w') as wfile:
        wfile.write(final_summary)
      
      
      