import whisper
from consts import TEXTS_PATH, AUDIOS_PATH
from utils import write_on_file

MODELS = ['tiny', 'small', 'base', 'medium', 'large', 'turbo']

class Transcriber:
  def __init__(self, model_type='medium'):
    self.last_transcription = ''
    self.model = whisper.load_model(model_type)
  
  def transcribe_file(self, filename: str) -> str:
    path = AUDIOS_PATH + filename
    if not filename.endswith('.mp3'):
      path += '.mp3'
    self.last_transcription = self.model.transcribe(path)['text']
    return self.last_transcription

  def save_transcription(self, file: str, data=None):
    if not file.endswith('txt'):
      file += '.txt'
      
    if data:
      write_on_file(TEXTS_PATH + file, data)
    else:
      write_on_file(TEXTS_PATH + file, self.last_transcription)