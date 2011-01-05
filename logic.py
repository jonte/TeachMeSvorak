import gtk, os, pygtk, pynotify, sys, time, threading

class TMS:
    def __init__(self, layouts):
        self.layouts = layouts
        self.workers = []
        self.alive = True
        self.timeout = None
        self.callback = None

    def run(self):
        t = threading.Thread(target=self._run)
        self.workers.append(t)
        t.start()

    def _run(self):
        self._cycleSet()
        self.timeout = self.layouts[0][0] * 60
        while self.alive:
            if self.callback != None:
                self.callback()
            time.sleep(1)
            self.timeout -= 1
            if self.timeout == 0:
                self._cycleSet()
                self.timeout = self.layouts[0][0] * 60

    def registerCallback(self, cb):
        self.callback = cb

    def stop(self):
        self.alive = False

    def getTimeLeft(self):
        return (self.timeout, self.layouts[0][0] * 60)

    def flash(self, message):
        n = pynotify.Notification("Switching layout", message, "")
        n.show()

    def cycleLayouts(self):
        self.layouts = self.layouts[1:] + [self.layouts[0]]

    def setLayout(self):
        os.system("setxkbmap " + self.layouts[0][1])
    
    def notifyLayout(self):
        self.flash("Setting layout to %s for %s minutes." % (self.layouts[0][1], 
                                              self.layouts[0][0]))

    def _cycleSet(self):
        self.cycleLayouts()
        self.notifyLayout()
        self.setLayout()

    def getCurrentLayout(self):
        return self.layouts[0][1]
    

if __name__ == "__main__":
    tms = TMS([(20, "se"), (5, "se -variant dvorak")])
    tms.run()
