import clutter
import mxpy as mx

def btn_clicked_cb(button, entry):
    entry.set_text("Here is some text")

def clear_btn_clicked_cb(button, entry):
    entry.set_text("")

def primary_icon_clicked_cb(entry):
    print 'primary icon clicked'

def secondary_icon_clicked_cb(entry):
    print 'secondary icon clicked'

if __name__ == '__main__':
    stage = clutter.Stage()
    stage.connect('destroy', clutter.main_quit)
    stage.set_size(400, 300)

    entry = mx.Entry("Hello world!")
    entry.set_position(20, 20)
    entry.set_width(150)
    stage.add(entry)
    stage.set_key_focus(entry.get_clutter_text())

    entry = mx.Entry()
    entry.set_position(20, 70)
    stage.add(entry)
    entry.set_hint_text("hint hint...")

    button = mx.Button("Set")
    button.set_position(20, 120)
    button.connect('clicked', btn_clicked_cb, entry)

    clear_button = mx.Button("Clear")
    clear_button.set_position(70, 120)
    clear_button.connect('clicked', clear_btn_clicked_cb, entry)

    stage.add(button, clear_button)

    entry = mx.Entry()
    entry.set_position(20, 170)
    stage.add(entry)
    entry.set_hint_text("Search...")
    entry.set_primary_icon_from_file('edit-find.png')
    entry.set_secondary_icon_from_file('edit-clear.png')
    entry.connect('primary-icon-clicked', primary_icon_clicked_cb)
    entry.connect('secondary-icon-clicked', secondary_icon_clicked_cb)

    stage.show()
    clutter.main()
