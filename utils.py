from collections import defaultdict
import os
import re


def files_from_path(path: str):
  for _, _, files in os.walk(path):
    for file in files:
      yield file


def codec_filename(filename: str) -> str:
  freq = defaultdict(int)
  for c in re.sub(r'[-_\.\d ]', '', filename.lower()):
    freq[c] += 1
  return ''.join(f'{char}{cnt}' for char, cnt in freq.items())


def remove_special_characters(s: str) -> str:
  return re.sub(r'[-_\. ]', '', s)


def split_text(text, max_length=3000):
    return [text[i:i + max_length] for i in range(0, len(text), max_length)]


def write_on_file(path: str, data: str):
  with open(path, 'w', encoding='utf-8') as fwrite:
    fwrite.write(data)


if __name__ == '__main__':
  codec_test_1 = 'hola._- mundo'
  output = codec_filename(codec_test_1)
  assert output == 'h1o2l1a1m1u1n1d1', f'Got {output}'
