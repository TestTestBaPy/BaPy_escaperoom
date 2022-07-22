from display_components import *
import pygame
import matplotlib
import matplotlib.backends.backend_agg as agg
import pygame
from pygame.locals import *
from game_timer import get_needed_time
from handle_userinput import *
import pylab
import os.path, csv


def save_user_data():
    
    with open("Escaperoom_stats.csv", "a") as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow([get_input_text(), get_clicks(), get_needed_time()])

    csv_file.close()
def open_scipy():
   
    matplotlib.use("Agg")
    fig = pylab.figure(figsize=[4, 4], # Inches
                    dpi=150,        # 100 dots per inch, so the resulting buffer is 400x400 pixels
                    )
    ax = fig.gca()
    ax.plot([1, 2, 4])

    canvas = agg.FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()
    
    pygame.init()


    # window = pygame.display.set_mode((disp, 200*3), DOUBLEBUF)
    # screen = pygame.display.get_surface()

    size = canvas.get_width_height()

    surf = pygame.image.fromstring(raw_data, size, "RGB")
    game_screen.fill(white)
    game_screen.blit(surf, (0,0))

    textSurf, textRect = text_objects('You needed exaclty ' + str(get_clicks()) + 'clicks and ' + str(get_needed_time())+' in time! Your name is ' + str(get_input_text()), smallText)
    textRect.bottomleft = ( (200,520) )
    game_screen.blit(textSurf, textRect)

    #TO-DO: save clicks to a csv-file 
    # add sound effects 
    # select a username at beginning