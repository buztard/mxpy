import clutter
import nbtk

def stage_size_notify_cb(stage, pspec, scroll):
    scroll.set_size(stage.get_width()-100, stage.get_height()-100)

def swap_orientation(button, grid):
    grid.set_column_major(not grid.get_column_major())

def set_max_stride(actor, event, grid):
    grid.set_max_stride(event.keyval - 48)

if __name__ == '__main__':
    stage = clutter.Stage()
    stage.connect('destroy', clutter.main_quit)
    stage.set_user_resizable(True)
    stage.set_color((255, 255, 255, 255))

    scroll = nbtk.ScrollView()
    stage.add(scroll)

    grid = nbtk.Grid()
    scroll.add(grid)

    for i in range(200):
        button = nbtk.Button("Button %i" % i)
        button.set_tooltip_text("Tooltip %i" % i)
        button.connect('clicked', swap_orientation, grid)
        grid.add(button)
    
    stage.connect('notify::width', stage_size_notify_cb, scroll)
    stage.connect('notify::height', stage_size_notify_cb, scroll)
    stage.connect('key-release-event', set_max_stride, grid)

    stage.show()
    clutter.main()


