#!/usr/bin/python
from gi.repository import Gtk, Gdk, GObject
import os, subprocess, signal

CURR_WORK_DIR = os.getcwd()

class MainWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="Shell Script Running")
		self.set_position(Gtk.WindowPosition.CENTER)
		self.set_opacity(0.9)
		#self.p = None
		
		self.connect("delete-event", self.on_quit)

		screen = Gdk.Screen.get_default()
		css_provider = Gtk.CssProvider()
		css_provider.load_from_path(CURR_WORK_DIR + '/themed.css')

		self.scrolledTextView = ScrolledWindowTextView()

		hbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
		hbox.pack_start(self.scrolledTextView, False, True, 0)
		self.add(hbox)

	def on_quit(self, widget, event):
		GObject.source_remove(self.io_id)
		self.p.kill()
		Gtk.main_quit()

	def runProcess(self):
		self.p = subprocess.Popen([CURR_WORK_DIR + '/test.sh'], stdout=subprocess.PIPE, shell=False)
		self.io_id = GObject.io_add_watch(self.p.stdout, GObject.IO_IN, self.read_data)
		print self.p.pid
	def read_data(self, source, condition):
		line = source.readline() # might block
		if not line:
			source.close()
			return False # stop reading
		# update text
		buf = self.scrolledTextView.textbuffer
		buf.insert_at_cursor(line.rstrip() + "\n")
		return True # continue reading

class ScrolledWindowTextView(Gtk.ScrolledWindow):
	def __init__(self):
		Gtk.ScrolledWindow.__init__(self)

		self.set_min_content_height(400)
		self.set_min_content_width(400)

		self.set_border_width(0)
		self.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.ALWAYS)

		self.textview = Gtk.TextView()
		self.textbuffer = self.textview.get_buffer()
		self.add(self.textview)

if __name__ == "__main__":
	win = MainWindow()
	win.set_default_size(400, 400)
	win.show_all()
	win.runProcess()
	Gtk.main()
	