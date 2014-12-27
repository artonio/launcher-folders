#!/usr/bin/python
from gi.repository import Gtk, Gdk, GdkPixbuf, GObject

class TabLabel(Gtk.Box):
    __gsignals__ = {
        "close-clicked": (GObject.SIGNAL_RUN_FIRST, GObject.TYPE_NONE, ()),
        "edit-drawer-name": (GObject.SIGNAL_RUN_FIRST, GObject.TYPE_NONE, ())
    }
    def __init__(self, label_text, drawerIconFileName):
        Gtk.Box.__init__(self)

        self.set_orientation(Gtk.Orientation.HORIZONTAL)
        self.set_spacing(5) # spacing: [icon|5px|label|5px|close]  
      
        # icon
        if drawerIconFileName:
            self.icon = Gtk.Image.new_from_pixbuf(self.getPixBuffFromFile(drawerIconFileName))
        else:
            self.icon = Gtk.Image.new_from_stock(Gtk.STOCK_FILE, Gtk.IconSize.MENU)
            
        self.pack_start(self.icon, False, False, 0)
        
        # label 
        lbl_event_box = Gtk.EventBox.new()
        self.label = Gtk.Label(label_text)
        lbl_event_box.add(self.label)
        lbl_event_box.set_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        lbl_event_box.connect("button-press-event", self.button_pressed)
        self.pack_start(lbl_event_box, True, True, 0)
        
        # close button
        button = Gtk.Button()
        button.set_relief(Gtk.ReliefStyle.NONE)
        button.set_focus_on_click(False)
        button.add(Gtk.Image.new_from_stock(Gtk.STOCK_CLOSE, Gtk.IconSize.MENU))
        button.connect("clicked", self.button_clicked)
        data =  ".button {\n" \
                "-GtkButton-default-border : 0px;\n" \
                "-GtkButton-default-outside-border : 0px;\n" \
                "-GtkButton-inner-border: 0px;\n" \
                "-GtkWidget-focus-line-width : 0px;\n" \
                "-GtkWidget-focus-padding : 0px;\n" \
                "padding: 0px;\n" \
                "}"
        provider = Gtk.CssProvider()
        provider.load_from_data(data)
        # 600 = GTK_STYLE_PROVIDER_PRIORITY_APPLICATION
        button.get_style_context().add_provider(provider, 600) 
        self.pack_start(button, False, False, 0)
        
        self.show_all()

    def button_pressed(self, button, event):
        if event.type == Gdk.EventType._2BUTTON_PRESS:
            self.emit("edit-drawer-name")
    
    def button_clicked(self, button, data=None):
        self.emit("close-clicked")

    def getPixBuffFromFile(self, fileName):
        pixbuf = GdkPixbuf.Pixbuf.new_from_file(fileName)
        pixbuf = pixbuf.scale_simple(32, 32, GdkPixbuf.InterpType.BILINEAR)
        
        return pixbuf
