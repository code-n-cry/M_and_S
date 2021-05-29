import pygame
import sys
from piano import create_warning


def play_music(midi_filename='output.mid'):
  clock = pygame.time.Clock()
  pygame.mixer.music.load(midi_filename)
  pygame.mixer.music.play()
  while pygame.mixer.music.get_busy():
    clock.tick(30)



freq = 44100
bitsize = -16
channels = 2
buffer = 1024
pygame.mixer.init(freq, bitsize, channels, buffer)
if __name__ == '__main__':
    play_music(sys.argv[1])