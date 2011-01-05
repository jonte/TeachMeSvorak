import logic, gui, gtk

def launch(settings):
    tms = logic.TMS(settings)#[(0.20, "se"), (0.5, "se -variant dvorak")])
    tms.registerCallback(lambda: gui.updateProgress(tms))
    gui.addCallback('exit', tms.stop)
    tms.run()

gtk.gdk.threads_init()
gui = gui.GUI()
gui.addCallback('apply', lambda x, y: launch(gui.getSettings()))
gui.main()
