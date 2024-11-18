from summarizer import Summarizer
from transcriber import Transcriber
from utils import remove_special_characters, files_from_path
from audiovisual_manipulator import AudiovisualManipulator
from consts import VIDEOS_PATH


if __name__ == '__main__':
  avm = AudiovisualManipulator()
  transcriber = Transcriber()
  summarizer = Summarizer()
  
  for file in files_from_path(VIDEOS_PATH):
    filename, ext = file.rsplit('.', 1)
    output_name = remove_special_characters(filename)
    
    audio= avm.get_audio_from_filename(file)
    avm.save_audio(audio, output_name)
    
    text = transcriber.transcribe_file(output_name)
    transcriber.save_transcription(output_name)   
    
    summarizer.summarize_text(text, output_name)     
    
    
    
      
      
      