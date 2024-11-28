from moviepy.editor import VideoFileClip as VideoFile, AudioFileClip as AudioFile
from consts import VIDEOS_PATH, AUDIOS_PATH
from logger import log as print


class AudiovisualManipulator:
  def __init__(self):
    self.mp4_files : list[VideoFile] = []
    print("~> AudioVisualManipulator Initialiced ✅")
  
  def __del__(self):
    for mp4 in self.mp4_files:
      mp4.close()
    
  def get_audio_from_filename(self, filename: str) -> AudioFile:
    mp4_file = VideoFile(VIDEOS_PATH + filename)
    self.mp4_files.append(mp4_file)
    return mp4_file.audio

  def save_audio(self, audio: AudioFile, filename: str) -> None:
    if not filename.endswith('.mp3'):
      filename += '.mp3'
    audio.write_audiofile(AUDIOS_PATH + filename)
    audio.close()
  