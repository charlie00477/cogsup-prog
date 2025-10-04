from expyriment import design, control, stimuli


def ternus_display(exp, radius=50, isi=50, duration=200):
    w,h = exp.screen.size
    y = 0  
    spacing = radius * 3  
    frame1_positions = [(-spacing, y), (0, y)]
    frame2_positions = [(0, y), (spacing, y)]

    frame1 = [stimuli.Circle(radius=radius, colour=(255,255,255), position=pos) for pos in frame1_positions]
    frame2 = [stimuli.Circle(radius=radius, colour=(255,255,255), position=pos) for pos in frame2_positions]
    
    exp.screen.clear()
    for circle in frame1:
        circle.present(clear=False, update=False)
    exp.screen.update()
    exp.clock.wait(duration)

    exp.screen.clear()
    exp.screen.update()
    exp.clock.wait(isi)

    exp.screen.clear()
    for circle in frame2:
        circle.present(clear=False, update=False)
    exp.screen.update()
    exp.clock.wait(duration)

    exp.screen.clear()
    exp.screen.update()

exp = design.Experiment(name="Ternus Display")
control.initialize(exp)
control.start()

fixation = stimuli.FixCross()
fixation.present(clear=True, update=True)
exp.clock.wait(1000)

ternus_display(exp, radius=40, isi=50, duration=200)
exp.clock.wait(1000)  

exp.keyboard.wait()
control.end()
    