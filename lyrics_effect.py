import time
import pygame
import sys

# Initialize music
pygame.mixer.init()
pygame.mixer.music.load("about_you.mp3")
pygame.mixer.music.play()

# Lyrics and their apporoximate timestamps (in seconds)
timed_lyrics = [
    (45, "I ||||||||know a place"),
    (55, "It's somewhere I go when I need to remember your |face"),
    (64.5, "We get married ||||||in our |heads"),
    (75, "Something to do while we try to recall how we |met"),
    (84, "Do you think I have |forgotten?"),
    (89, "Do you think I have |forgetten?"),
    (94, "Do you think I have |forgotten |||about you?")
]

#Typing effect
def type_line(line, delay=0.1, pause_marker="|", pause_duration=0.5):
    parts = line.split(pause_marker)
    for i, part in enumerate (parts):
        for char in part:
            print(char, end='', flush=True)
            time.sleep(delay)
        if i < len(parts) - 1: 
             time.sleep(pause_duration)
    print()

#Sync and display lyrics
start_time = time.time()

for timestamp, line in timed_lyrics:
    while time.time() - start_time < timestamp:
        time.sleep(0.1)
    type_line(line)

#Wait until the song ends
while pygame.mixer.music.get_busy():
        time.sleep(1)