import os
import whisper
from utils import remove_special_characters
from audiovisual_manipulator import AudiovisualManipulator

VIDEOS_PATH = './videos-to-summary/'
AUDIOS_PATH = './audios-from-videos/'
TEXTS_PATH = './text-from-videos/'

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
      
      
      
      