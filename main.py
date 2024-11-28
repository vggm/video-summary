from summarizer import Summarizer
from transcriber import Transcriber
from utils import remove_special_characters, files_from_path
from audiovisual_manipulator import AudiovisualManipulator
from consts import VIDEOS_PATH
from logger import log as print


def process_file(file: str):
  filename, ext = file.rsplit('.', 1)
  output_name = remove_special_characters(filename)
  
  audio= avm.get_audio_from_filename(file)
  avm.save_audio(audio, output_name)
  
  text = transcriber.transcribe_file(output_name)
  transcriber.save_transcription(output_name)   
  
  summarizer.summarize_text(text, output_name) 


if __name__ == '__main__':
  avm = AudiovisualManipulator()
  transcriber = Transcriber()
  summarizer = Summarizer()
  
  files = list(files_from_path(VIDEOS_PATH))
  print("~> Files founds: ", files)
  
  opt = -1
  for file in files:
    if opt != 'a':
      opt = input(f"!> Process file: {file}? ('n' to skip | 'a' to process all | 'q' to end):\n")
    
    if opt == 'n':
      continue
    
    if opt == 'q':
      exit(0)

    # process_file(file)
    
    
    
    
      
      
      