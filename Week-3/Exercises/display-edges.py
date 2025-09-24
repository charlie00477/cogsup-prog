# Import the main modules of expyriment
from expyriment import design, control, stimuli

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "edges")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

rectangle = stimuli.Rectangle(size=(100,100), colour=(255,0,0), line_width=(1), position=(-350,150))
rectangle.present(clear = True, update = True)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()