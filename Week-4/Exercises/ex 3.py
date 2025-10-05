from expyriment import design, control, stimuli

exp = design.Experiment(name="ex 3")

control.set_develop_mode()
control.initialize(exp)

def load(stims):
    for stim in stims:
        stim.preload()

def draw(stims, canvas):
    canvas.clear_surface()
    canvas.preload()

    for stim in stims():
        stim.plot(canvas)
    
    canvas.present()

    
    