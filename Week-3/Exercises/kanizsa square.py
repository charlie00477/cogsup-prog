# Import the main modules of expyriment
from expyriment import design, control, stimuli

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "edges")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

background_color = colour=(128,128,128)

width, height = exp.screen.size
radius_circle =width//20
square_size = width//4

circle = stimuli.Circle(radius=radius_circle)
colour_circle=[(255,255,255), (0,0,0)]
x, y = square_size//2
position_circle = [(-x,y), (x,y), (x,-y), (-x,-y)]


# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()