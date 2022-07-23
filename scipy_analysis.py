import matplotlib, pygame, pylab, csv, pandas
import matplotlib.backends.backend_agg as agg
from pygame.locals import *
from game_timer import get_needed_time
from handle_userinput import *
from os.path import exists
from display_components import *


def save_user_data():
    """Saves the username (if given), click and elapsed time of player in a csv
    """

    file_exists = exists("Escaperoom_stats.csv")

    with open("Escaperoom_stats.csv", "a", newline='') as csv_file:
            writer = csv.writer(csv_file)

            if not file_exists:
                writer.writerow(["USERNAME", "CLICKS", "TIME"])
            writer.writerow([get_input_text(), get_clicks(), get_needed_time()])
        
    set_current_room("NAN")
    csv_file.close()


def open_scipy_plot():

    df = pandas.read_csv("Escaperoom_stats.csv")
    # this is the last entry
    current_result = df.iloc[-1]
    
    df = df[["CLICKS", "TIME"]].sort_values("CLICKS")
    print(df)
   
    matplotlib.use("Agg")
    fig = pylab.figure(figsize=[4, 4], dpi=150)   # 100 dots per inch, so the resulting buffer is 400x400 pixels
    ax = fig.gca()
    ax.scatter((df["CLICKS"]), df[ "TIME"])

    # scatter the players result twice so he/she can see their score in comparison
    ax.scatter(current_result[1], current_result[2])

    canvas = agg.FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()
    size = canvas.get_width_height()
    surf = pygame.image.fromstring(raw_data, size, "RGB")
    game_screen.fill(white)
    game_screen.blit(surf, (0,0))

    textSurf, textRect = text_objects('You needed ' + str(get_clicks()) + ' clicks and ' + str(get_needed_time()) + ' in time!', smallText)
    textRect.bottomleft = ((570,100))
    game_screen.blit(textSurf, textRect)

    textSurf, textRect = text_objects('Your name is ' + str(get_input_text()) + 'and your grade is ' + str(calculate_grade(current_result[1])), smallText)
    textRect.bottomleft = ((570,130))
    game_screen.blit(textSurf, textRect)

    textSurf, textRect = text_objects('The orange dot is you!', smallText)
    textRect.bottomleft = ( (250,520) )

    game_screen.blit(textSurf, textRect)


def calculate_grade(click_amount):
    return min(click_amount//30, 6)
