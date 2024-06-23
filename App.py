import pygame
import os, sys
pygame.init()


os.environ["SDL_VIDEODRIVER"] = "dummy"

import pygame.transform
running = True

useage = """-scale inputimage outputimage new_width new_height
eg.  -scale in.png out.png 50 50

"""

if 1:
    import pygame.display
    pygame.display.init()
    screen = pygame.display.set_mode([1, 1])

def scaleit(fin, fout, w, h):
    i = pygame.image.load(fin)

    if hasattr(pygame.transform, "smoothscale"):
        scaled_image = pygame.transform.smoothscale(i, (w,h))
    else:
        scaled_image = pygame.transform.scale(i, (w,h))
    pygame.image.save(scaled_image, fout)

if __name__ == "__main__":
    if "-scale" in sys.argv:
        fin, fout, w, h = sys.argv[2:]
        w, h = map(int, [w, h])
        scaleit(fin, fout, w, h)

    else:
        print(useage)


