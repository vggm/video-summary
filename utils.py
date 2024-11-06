from collections import defaultdict
import re


def codec_filename(filename: str) -> str:
  freq = defaultdict(int)
  for c in re.sub(r'[-_\.\d ]', '', filename.lower()):
    freq[c] += 1
  return ''.join(f'{char}{cnt}' for char, cnt in freq.items())


def remove_special_characters(s: str) -> str:
  return re.sub(r'[-_\. ]', '', s)


if __name__ == '__main__':
  codec_test_1 = 'hola._- mundo'
  output = codec_filename(codec_test_1)
  assert output == 'h1o2l1a1m1u1n1d1', f'Got {output}'
