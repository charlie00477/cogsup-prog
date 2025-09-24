# Import the main modules of expyriment
from expyriment import design, control, stimuli

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "edges")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

width, height = exp.screen.size
side = 5/100*width
sizee = (side,  side)

x = (width//2) - (side//2)
y = (height//2) - (side//2)

positions = [(-x,y), (x,y), (x,-y), (-x,-y)]

corners = []
for pos in positions :
    rectangle = stimuli.Rectangle(size=(sizee), colour=(255,0,0), line_width=(1), position=(pos))
    corners.append(rectangle)

for rectangle in corners :
    rectangle.present(clear = False, update = False)

exp.screen.update()

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()