from expyriment import design, control, stimuli
from expyriment.misc.constants import K_DOWN, K_UP, K_LEFT, K_RIGHT, C_WHITE, C_BLACK

""" Global settings """
exp = design.Experiment(name="Blindspot", background_colour=C_WHITE, foreground_colour=C_BLACK)
control.set_develop_mode()
control.initialize(exp)

""" Stimuli """
def make_circle(r, pos=(0,0)):
    circle = stimuli.Circle(r, position=pos, anti_aliasing=10)
    circle.preload()
    return circle

""" Experiment """
def run_trial():
    fixation = stimuli.FixCross(size=(150, 150), line_width=10, position=[300, 0])
    fixation.preload()

    radius = 75
    circle = make_circle(radius)

    fixation.present(True, False)
    circle.present(False, True)

    while True:
        if exp.keyboard.wait(K_DOWN):
            circle.move((0,-10))
        if exp.keyboard.wait(K_UP):
            circle.move((0,10))
        if exp.keyboard.wait(K_RIGHT):
            circle.move((10,0))
        if exp.keyboard.wait(K_LEFT):
            circle.move((-10,0))

        exp.keyboard.wait()

control.start(subject_id=1)

run_trial()
    
control.end()