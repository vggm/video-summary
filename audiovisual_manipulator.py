from moviepy.editor import VideoFileClip as VideoFile, AudioFileClip as AudioFile


class AudiovisualManipulator:
  def __init__(self):
    self.mp4_files : list[VideoFile] = []
  
  def __del__(self):
    for mp4 in self.mp4_files:
      mp4.close()
    
  def get_audio_from_filename(self, filename: str) -> AudioFile:
    mp4_file = VideoFile(filename)
    self.mp4_files.append(mp4_file)
    return mp4_file.audio

  def save_audio(self, audio: AudioFile, filename: str) -> None:
    audio.write_audiofile(filename)
    audio.close()
  