import clutter
import mx

def expand_completed_cb (expander):
    print "expand complete", expander.get_expanded()

def set_expanded(actor, event, expander):
    if event.keyval != 32:
        return
    expander.set_expanded(not expander.get_expanded())

def stage_size_notify_cb(stage, pspec, table):
    width, height = stage.get_size()

if __name__ == '__main__':
    stage = clutter.Stage()
    stage.connect('destroy', clutter.main_quit)
    stage.set_color((255, 255, 255, 255))
    stage.set_user_resizable(True)

    expander = mx.Expander()
    expander.set_label("Expander")
    expander.set_position(10, 10)
    expander.connect('expand-complete', expand_completed_cb)
    stage.add(expander)

    scroll = mx.ScrollView()
    expander.add(scroll)
    scroll.set_size(320, 240)

    grid = mx.Grid()
    scroll.add(grid)

    for i in range(50):
        button = mx.Button("Button %i" % i)
        grid.add(button)

    stage.connect('notify::width', stage_size_notify_cb, expander)
    stage.connect('notify::height', stage_size_notify_cb, expander)
    stage.connect('key-release-event', set_expanded, expander)
    
    stage.show()
    clutter.main()


