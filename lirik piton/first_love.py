import sys
import time

def jalanin_lirik () :
    lirik = [
        ("Don't go out and play", 0.1),
        ("I just dream all day", 0.9),
        ("They don't know what's wrong with me", 0.9),
        ("And I'm too shy to say", 0.9),
        ("It's my first love", 0.9),
        ("What I'm dreaming of", 0.9),
        ("When I go to bed", 0.9),
        ("When I lay my head upon my pillow", 0.9),
        ("Don't know what to do", 0.9),
        ("My first love", 0.9),
        ("Thinks that I'm too ", 0.9),
        ("She doesn't even know", 0.9),
        ("Wish that I could show her what I'm feeling", 0.9),
        ("Cause I'm feeling my first love", 0.9)
    ]
    
    delay = [0.3, 0.3, 0.4, 1, 0.2, 0.4, 0.3, 0.3, 0.3, 0.4, 1, 0.2, 0.4]
    print("\n==First Date - arditho")
    time.sleep(2)
for i,  (baris_lagu, delay_karakter) in enumerate(lirik):
    for karakter in baris_lagu:
        print(karakter, end='')
        sys.stdout.flush()
        time.sleep(delay_karakter)
    time.sleep(delay[i])
    print('')
print("// Code by VEEE")        
jalanin_lirik()