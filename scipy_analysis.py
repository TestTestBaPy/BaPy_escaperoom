import matplotlib, pygame, pylab, csv, pandas
from matplotlib.pyplot import xlabel
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg
from pygame.locals import *
from game_timer import get_needed_time
from handle_userinput import *
from os.path import exists
from display_components import *
from scipy import stats


def save_user_data():
    """Saves the username (if given), click and elapsed time of player in a csv"""
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
    # This is the last entry
    current_result = df.iloc[-1]
    df = sort_df(df)
   
    matplotlib.use("Agg")
    fig = pylab.figure(figsize=[4, 4], dpi=150)   # 100 dots per inch, so the resulting buffer is 400x400 pixels
    ax = fig.gca()
    ax.scatter((df["CLICKS"]), df[ "TIME"])
    ax.set(xlabel = "Clicks", ylabel = "Time", title = "Highscore Userdata - Clicks vs. Time")

    ax.plot(linear_regression(list(df["CLICKS"]), list(df[ "TIME"]))[0], linear_regression(list(df["CLICKS"]), list(df[ "TIME"]))[1])

    # catter the players result twice so they can see their score in comparison
    ax.scatter(current_result[1], current_result[2])

    df_h = df.head(5)
    #print(df.loc())
   
    #x = (str(df[["CLICKS", "TIME"]][:5]))
    #textsurface = smallText.render(x, True, BLACK)

    
    canvas = agg.FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()
    size = canvas.get_width_height()
    surf = pygame.image.fromstring(raw_data, size, "RGB")
    game_screen.fill(white)
    game_screen.blit(surf, (0,0))

    x = 300
    textSurf, textRect = text_objects("Highscore Table", smallText)
    textRect.bottomleft = ((600, x))
    game_screen.blit(textSurf, textRect)
    x += 20
    textSurf, textRect = text_objects("CLICKS        TIME", smallText)
    textRect.bottomleft = ((580, x))
    game_screen.blit(textSurf, textRect)
    
    for row in df_h.iloc():
        x += 20
        textSurf, textRect = text_objects(str(row[0]) + "           " +  str(row[1]), smallText)
        textRect.bottomleft = ((600, x))
        game_screen.blit(textSurf, textRect)
        
    

    # display infos for the user 
    textSurf, textRect = text_objects('You needed ' + str(get_clicks()) + ' clicks and ' + str(get_needed_time()) + ' minutes!', smallText)
    textRect.bottomleft = ((570,100))
    game_screen.blit(textSurf, textRect)
    textSurf, textRect = text_objects('Great job,' + str(get_input_text()) + ', your grade is ' + str(calculate_grade(current_result[1])), smallText)
    textRect.bottomleft = ((570,130))
    game_screen.blit(textSurf, textRect)

    textSurf, textRect = text_objects('The orange dot is you!', smallText)
    textRect.bottomleft = ( (600,520) )

    game_screen.blit(textSurf, textRect)

def linear_regression(x,y):
    slope, intercept, r, p, std_err = stats.linregress(x, y)

    def myfunc(x):
      return slope * x + intercept

    mymodel = list(map(myfunc, x))

    return x, mymodel
    
def sort_df(df):
    """Sorts the Dataframe in Clicks and then in time
    """
    return df[["CLICKS", "TIME"]].sort_values(['CLICKS', 'TIME'], 
              ascending = [True, True])

def calculate_grade(click_amount):
    return min(click_amount//30, 6)
