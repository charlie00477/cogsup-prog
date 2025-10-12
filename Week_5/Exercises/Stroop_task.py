from expyriment import design, control, stimuli
from expyriment.misc.constants import K_DOWN, K_UP, K_LEFT, K_RIGHT, C_WHITE, C_BLACK, K_SPACE, K_1, K_2

""" Global settings """
exp = design.Experiment(name="Blindspot", background_colour=C_WHITE, foreground_colour=C_BLACK)
control.set_develop_mode()
control.initialize(exp)

exp.add_data_variable_names(["eye", "key_pressed","radius_data", "x_coord", "y_coord"]) 

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

    text = stimuli.TextScreen("Find your blind spot", "Cover your left eye, fixate the cross, move the circle with the arrows until finding your blind spot, press space when done")
    text.present()
    exp.keyboard.wait()
    exp.keyboard.clear()

    fixation.present(True, False)
    circle.present(False, True)

    while True:
        key = exp.keyboard.check()  

        if key == K_DOWN:
            circle.move((0, -10))
            x_coord, y_coord = circle.position
            eye = "left" if x_coord < fixation.position[0] else "right"
            key_pressed = key
            exp.data.add([eye, key_pressed, radius, x_coord, y_coord])
        elif key == K_UP:
            circle.move((0, 10))
            x_coord, y_coord = circle.position
            eye = "left" if x_coord < fixation.position[0] else "right"
            key_pressed = key
            exp.data.add([eye, key_pressed, radius, x_coord, y_coord])
        elif key == K_RIGHT:
            circle.move((10, 0))
            x_coord, y_coord = circle.position
            eye = "left" if x_coord < fixation.position[0] else "right"
            key_pressed = key
            exp.data.add([eye, key_pressed, radius, x_coord, y_coord])
        elif key == K_LEFT:
            circle.move((-10, 0))
            x_coord, y_coord = circle.position
            eye = "left" if x_coord < fixation.position[0] else "right"
            key_pressed = key
            exp.data.add([eye, key_pressed, radius, x_coord, y_coord])
        elif key == K_1: 
            radius = max(5, radius - 5)  
            circle = make_circle(radius, pos=circle.position)
            x_coord, y_coord = circle.position
            eye = "left" if x_coord < fixation.position[0] else "right"
            key_pressed = key
            exp.data.add([eye, key_pressed, radius, x_coord, y_coord])
        elif key == K_2:  
            radius += 5
            circle = make_circle(radius, pos=circle.position)
            x_coord, y_coord = circle.position
            eye = "left" if x_coord < fixation.position[0] else "right"
            key_pressed = key
            exp.data.add([eye, key_pressed, radius, x_coord, y_coord])
        elif key == K_SPACE:
            x_coord, y_coord = circle.position
            eye = "left" if x_coord < fixation.position[0] else "right"
            key_pressed = key
            exp.data.add([eye, key_pressed, radius, x_coord, y_coord])
            break

        exp.screen.clear()
        fixation.present(clear=False, update=False)
        circle.present(clear=False, update=True)

        exp.clock.wait(20)

        

control.start(subject_id=1)

run_trial()
    
control.end()