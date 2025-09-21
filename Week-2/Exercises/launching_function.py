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

# Leave it on-screen for 1,000 ms
exp.clock.wait(1000)
def launching_event(exp, temporal_gap=False, spatial_gap=False, higher_speed=False):

    square_size = (50, 50)
    speed = 10 # for red
    green_speed = speed*2 if higher_speed else speed
    
    # Create a 50px-radius circle
    Rectangle1 = stimuli.Rectangle(square_size, colour=(255,0,0), position=(-400,0))
    green_start_x = 0 if not spatial_gap else 50  # green displaced to right if spatial gap
    Rectangle2 = stimuli.Rectangle(square_size, colour=(0,255,0), position=(green_start_x,0))  
    
    # Remove the cross and replace it 
    Rectangle1.present(clear=True, update=False)
    Rectangle2.present(clear=False, update=True)
    
    while Rectangle1.position[0]<-50:
        Rectangle1.clear_surface()
        Rectangle2.clear_surface()
        Rectangle1.move((speed,0))
        Rectangle1.present(clear=True, update=False)
        Rectangle2.present(clear=False, update=True)

    if temporal_gap:
        exp.clock.wait(300) 
        
    for _ in range (400):
        Rectangle1.clear_surface()
        Rectangle2.clear_surface()
        Rectangle2.move((green_speed,0))
        Rectangle1.present(clear=True, update=False)
        Rectangle2.present(clear=False, update=True)
        exp.clock.wait(10)

    # Hold final display 
    exp.clock.wait(200)

# Start running the experiment
control.start(subject_id=1)

# Create a fixation cross (color, size, and position will take on default values)
fixation = stimuli.FixCross() # At this stage the fixation cross is not yet rendered

# Present the fixation cross
fixation.present(clear=True, update=True)
exp.clock.wait(1000)

# 4 event types
# 1. Michottean launching 
launching_event(exp, temporal_gap=False, spatial_gap=False, higher_speed=False)
# 2. Temporal gap
launching_event(exp, temporal_gap=True, spatial_gap=False, higher_speed=False)
# 3. Spatial gap
launching_event(exp, temporal_gap=False, spatial_gap=True, higher_speed=False)
# 4. Triggering (green faster than red)
launching_event(exp, temporal_gap=False, spatial_gap=False, higher_speed=True)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()