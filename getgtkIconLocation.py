import gtk

print "enter the icon name (case sensitive):"
icon_name = raw_input(">>> ")
icon_theme = gtk.icon_theme_get_default()
icon = icon_theme.lookup_icon(icon_name, 48, 0)
if icon:
    print icon.get_filename()
else:
    print "not found"
