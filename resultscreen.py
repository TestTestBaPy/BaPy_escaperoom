import pygame, pylab, csv, pandas
import matplotlib.backends.backend_agg as agg
from pygame.locals import *
from game_timer import get_needed_time
from handle_userinput import *
from os.path import exists
from display_components import *
from scipy import stats


def save_user_data():
    """Saves the username (if given), click and elapsed time of player in a csv
    """
    # check if file exists
    file_exists = exists("Escaperoom_stats.csv")

    # write user data in csv
    with open("Escaperoom_stats.csv", "a", newline='') as csv_file:
            writer = csv.writer(csv_file)

            if not file_exists:
                # if file does not exists write header first
                writer.writerow(["USERNAME", "CLICKS", "TIME"])
            writer.writerow([get_input_text(), get_clicks(), get_needed_time()])
        
    # Set current room
    set_current_room("RESU")
    csv_file.close()


def open_scipy_plot():
    """Displays a Clicks vs. Time plot from all user data"""
    pygame.mixer.Sound.play(button_pushed)

    # read the csv data
    df = pandas.read_csv("Escaperoom_stats.csv")

    # This is the last entry (so the current users entry)
    current_result = df.iloc[-1]

    # sort the dataframe
    df = sort_df(df)
   
    # create a figure with pylab
    fig = pylab.figure(figsize=[4, 4], dpi=150) 

    # get the axe and plot the clicks vs. time
    ax = fig.gca()
    ax.scatter((df["CLICKS"]), df[ "TIME"])
    ax.set(xlabel = "Clicks", ylabel = "Time", title = "Highscore Userdata - Clicks vs. Time")

    # plot a regression line
    ax.plot(linear_regression(list(df["CLICKS"]), list(df["TIME"]))[0], linear_regression(list(df["CLICKS"]), list(df[ "TIME"]))[1])

    # scatter the players result twice so they can see their score in comparison
    ax.scatter(current_result[1], current_result[2])

    # display the plot    
    figure_canvas = agg.FigureCanvasAgg(fig)
    figure_canvas.draw()
    renderer = figure_canvas.get_renderer()
    data = renderer.tostring_rgb()
    size = figure_canvas.get_width_height()
    surface = pygame.image.fromstring(data, size, "RGB")
    game_screen.fill(WHITE)
    game_screen.blit(surface, (0,0))

    y = 250
    x = 600
    textSurf = text_objects("Highscore Table", small_text)
    game_screen.blit(textSurf, (x + 60, y))
    y += 20
    textSurf = text_objects("NAME    CLICKS      TIME", small_text)
    game_screen.blit(textSurf, (x + 30, y))
    

    for row in df.head(5).iloc():
        y += 30
        x = 640
        for i in range(3):

            textSurf = text_objects(str(row[i]).replace("nan", "-"), small_text)
            game_screen.blit(textSurf, (x, y))
            x += 100
        
    
    # display infos for the user 
    textSurf = text_objects('You needed ' + str(get_clicks()) + ' clicks and ' + str(get_needed_time()) + ' minutes!', small_text)
    game_screen.blit(textSurf, (570,100))
    textSurf = text_objects('Great job,' + str(get_input_text()) + ', your grade is ' + str(calculate_grade(current_result[1])), small_text)
    game_screen.blit(textSurf, (570,130))

    textSurf = text_objects('The orange dot is you!', small_text)

    game_screen.blit(textSurf, (600,520))

def linear_regression(x,y):
    """Perform linear regression
        Args: 
            x: the x-values of datapoints (array)
            y: the y-values of datapoints (array)
        Returns:
            the values to plot the regressionline
    """

    # perform linear regression
    res = stats.linregress(x, y)

    # returns the needed values to plot
    def myfunc(x):
      return res.slope * x + res.intercept

    # create the modelvalues
    model = list(map(myfunc, x))

    return x, model
    
def sort_df(df):
    """Sorts the Dataframe in clicks and then in time
    """
    return df.sort_values(['CLICKS', 'TIME'])

def calculate_grade(click_amount):
    """This function calculates the users grade based on clicks. The minimum amout of clicks to solve door
        1 or door 2 is 30 clicks.
        Returns:
            A grade from 1 to 6. 1 is from 30-60, 2 is from 30-60 etc.
    """
    return min(click_amount//30, 6)
