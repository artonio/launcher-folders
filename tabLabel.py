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

        # setup css provider for buttons
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

        # icon
        if drawerIconFileName:
            self.icon = Gtk.Image.new_from_pixbuf(self.getPixBuffFromFile(drawerIconFileName))
        else:
            self.icon = Gtk.Image.new_from_stock(Gtk.STOCK_FILE, Gtk.IconSize.MENU) 
        icon_button = Gtk.Button.new()
        icon_button.set_relief(Gtk.ReliefStyle.NONE)
        icon_button.set_focus_on_click(False)
        icon_button.add(self.icon)
        #TODO write on_click function for icon selection
        icon_button.connect("clicked", self.on_label_click)
        icon_button.get_style_context().add_provider(provider, 600)
        self.pack_start(icon_button, True, True, 0)

        # label
        self.label = Gtk.Label(label_text)
        label_button = Gtk.Button.new()
        label_button.set_relief(Gtk.ReliefStyle.NONE)
        label_button.set_focus_on_click(False)
        label_button.add(self.label)
        #label_button.set_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        label_button.connect("clicked", self.on_label_click)
        label_button.get_style_context().add_provider(provider, 600) 
        self.pack_start(label_button, True, True, 0)
        
        # close button
        close_button = Gtk.Button.new()
        close_button.set_relief(Gtk.ReliefStyle.NONE)
        close_button.set_focus_on_click(False)
        close_button.add(Gtk.Image.new_from_stock(Gtk.STOCK_CLOSE, Gtk.IconSize.MENU))
        close_button.connect("clicked", self.on_close_click)
        # 600 = GTK_STYLE_PROVIDER_PRIORITY_APPLICATION
        close_button.get_style_context().add_provider(provider, 600) 
        self.pack_start(close_button, False, False, 0)
        
        self.show_all()

    def on_label_click(self, button, data=None):
        #if event.type == Gdk.EventType._2BUTTON_PRESS:
        #    self.emit("edit-drawer-name")
        self.emit("edit-drawer-name")
    
    def on_close_click(self, button, data=None):
        self.emit("close-clicked")

    def getPixBuffFromFile(self, fileName):
        pixbuf = GdkPixbuf.Pixbuf.new_from_file(fileName)
        pixbuf = pixbuf.scale_simple(32, 32, GdkPixbuf.InterpType.BILINEAR)
        
        return pixbuf
