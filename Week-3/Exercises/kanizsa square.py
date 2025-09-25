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

x = square_size//2
y = square_size//2

#colour_circle=[(255,255,255), (255,255,255), (0,0,0), (0,0,0)]
position_circle = [(-x,y), (x,y), (x,-y), (-x,-y)]

circles = []
for pos in position_circle:
    circle = stimuli.Circle(radius=radius_circle, colour=(255,255,255), position=(pos))
    circles.append(circle)

for circle in circles:
    circle.present(clear=False, update=False)

grey_square = stimuli.Rectangle(size=(square_size,square_size), colour=(0,0,0))
grey_square.present(clear=False, update=False)

exp.screen.update()

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()