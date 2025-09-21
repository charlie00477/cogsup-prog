# expyriment.control.defaults.initialise_delay = 0 # No countdown
# expyriment.control.defaults.window_mode = True # Not full-screen
# 
# expyriment.control.defaults.fast_quit = True # No goodbye message

# Import the main modules of expyriment
from expyriment import design, control, stimuli

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Two_Squares")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

# Create a fixation cross (color, size, and position will take on default values)
fixation = stimuli.FixCross() # At this stage the fixation cross is not yet rendered

# Create a 50px-radius circle
Rectangle1 = stimuli.Rectangle(size=(50,50), colour=(255,0,0), position=(-400,0))
Rectangle2 = stimuli.Rectangle(size=(50,50), colour=(0,255,0))

# Start running the experiment
control.start(subject_id=1)

# Present the fixation cross
fixation.present(clear=True, update=True)

# Leave it on-screen for 1,000 ms
exp.clock.wait(1000)

# Remove the cross and replace it with a circle
Rectangle1.present(clear=True, update=False)
Rectangle2.present(clear=False, update=True)

while Rectangle1.position[0]<-50:
    Rectangle1.clear_surface()
    Rectangle2.clear_surface()
    Rectangle1.move((10,0))
    Rectangle1.present(clear=True, update=False)
    Rectangle2.present(clear=False, update=True)
    exp.clock.wait(10)

exp.clock.wait(50)

for _ in range (400):
    Rectangle1.clear_surface()
    Rectangle2.clear_surface()
    Rectangle2.move((10,0))
    Rectangle1.present(clear=True, update=False)
    Rectangle2.present(clear=False, update=True)
    exp.clock.wait(10)

# Hold final displat
exp.clock.wait(200)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()