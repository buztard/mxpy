"""
This test is adopted form mx, but since it's summer it uses
Munich's most famous Beergarden instead of places in London ;)
"""
import clutter
import mxpy as mx

def title_changed_cb(box, pspec):
    print 'title now:', box.get_title()

def index_changed_cb(box, pspec):
    print 'index now:', box.get_index()

def stage_key_press_cb(actor, event, box):
    from clutter import keysyms
    if event.keyval == keysyms.r:
        box.set_title('Munich')
    elif event.keyval >= ord('0') and event.keyval <= ord('9'):
        box.set_index(event.keyval - 48)

if __name__ == '__main__':
    stage = clutter.Stage()
    stage.connect('destroy', clutter.main_quit)

    combo = mx.ComboBox()
    stage.add(combo)
    combo.set_title('Munich')

    combo.append_text('Augustinerkeller')
    combo.append_text('Hirschgarten')
    combo.append_text('Nockherberg')
    combo.append_text('Seehaus')
    combo.append_text('Chinesischer Turm')
    combo.append_text('Zum Flaucher')

    combo.connect('notify::title', title_changed_cb)
    combo.connect('notify::index', index_changed_cb)
    stage.connect('key-press-event', stage_key_press_cb, combo)

    stage.show()
    clutter.main()
