#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

class GUI:

    def __init__(self):
        self.exitCallback = None

    def hello(self, widget, data=None):
        print "Hello World"

    def delete_event(self, widget, event, data=None):
        self.exitCallback()
        return False

    def destroy(self, widget, data=None):
        print "destroy signal occurred"
        gtk.main_quit()

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)
        self.window.set_border_width(10)
        # Widgets
        self.vbox = gtk.VBox(False, 0)
        self.timesBox = gtk.HBox(False, 0)
        self.layoutBox = gtk.HBox(False, 0)
        self.leftTimeEdit = gtk.Entry()
        self.rightTimeEdit = gtk.Entry()
        self.leftLayoutEdit = gtk.Entry()
        self.rightLayoutEdit = gtk.Entry()
        self.progress = gtk.ProgressBar()
        self.applyButton = gtk.Button("Apply settings")

        # Some default values
        self.leftTimeEdit.set_text("5")
        self.rightTimeEdit.set_text("20")
        self.rightLayoutEdit.set_text("se")
        self.leftLayoutEdit.set_text("se -variant dvorak")

        # Packing
        self.vbox.pack_start(self.timesBox, False, False, 0)
        self.vbox.pack_start(self.layoutBox, False, False, 0)
        self.vbox.pack_start(self.progress, False, False, 0)
        self.vbox.pack_start(self.applyButton, False, False, 0)

        self.timesBox.pack_start(self.leftTimeEdit, False, False, 0)
        self.timesBox.pack_start(self.rightTimeEdit, False, False, 0)

        self.layoutBox.pack_start(self.leftLayoutEdit, False, False, 0)
        self.layoutBox.pack_start(self.rightLayoutEdit, False, False, 0)

        # Display
        self.vbox.show()
        self.timesBox.show()
        self.layoutBox.show()
        self.leftTimeEdit.show()
        self.rightTimeEdit.show()
        self.leftLayoutEdit.show()
        self.rightLayoutEdit.show()
        self.progress.show()
        self.applyButton.show()
        self.window.add(self.vbox)
        #self.button = gtk.Button("Hello World")
        #self.button.connect("clicked", self.hello, None)
        #self.button.connect_object("clicked", gtk.Widget.destroy, self.window)
        #self.window.add(self.button)
        #self.button.show()
        self.window.show()

    def updateProgress(self, logic):
        (left, total) =  logic.getTimeLeft()
        self.progress.set_fraction(float(left) / float(total))
        self.window.set_title("Current layout: " + logic.getCurrentLayout())

    def addCallback(self, t, cb):
        if t == 'exit':
            self.exitCallback = cb
        elif t == 'apply':
            self.applyButton.connect("clicked", cb, None)

    def getSettings(self):
        return [(int(self.leftTimeEdit.get_text()), self.leftLayoutEdit.get_text()),
                (int(self.rightTimeEdit.get_text()), self.rightLayoutEdit.get_text())]

    def main(self):
        gtk.main()

if __name__ == "__main__":
    #gtk.main_iteration(block=False)
    hello = GUI()
    hello.main()
