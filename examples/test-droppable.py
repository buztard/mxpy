import clutter
import mxpy as mx
import gobject

class DraggableRectangle(clutter.Rectangle, mx.Draggable):
    __gtype_name__ = 'DraggableRectangle'
    __gproperties__ = {
        'enabled': (gobject.TYPE_BOOLEAN, 'enabled', 'enabled', False,
                    gobject.PARAM_READWRITE),
        'axis': (mx.DragAxis, 'axis', 'axis', mx.NO_AXIS,
                 gobject.PARAM_READWRITE),
        'drag-threshold': (gobject.TYPE_UINT,
                           'drag threshold', 'drag threshold',
                           0, gobject.G_MAXUINT, 0,
                           gobject.PARAM_READWRITE),
        'containment-type': (mx.DragContainment,
                             'containment type', 'containment type',
                             mx.DISABLE_CONTAINMENT, gobject.PARAM_READWRITE),
        'containment-area': (clutter.ActorBox,
                             'containment area', 'containment area',
                             gobject.PARAM_READWRITE),

    }
    def __init__(self):
        clutter.Rectangle.__init__(self)
        self._is_enabled = False
        self._axis = mx.NO_AXIS
        self._drag_threshold = 0
        self._containment_type = mx.DISABLE_CONTAINMENT
        self._containment_area = clutter.ActorBox()

    def do_get_property(self, pspec):
        if pspec.name == 'axis':
            return self._axis
        elif pspec.name == 'enabled':
            return self._is_enabled
        elif pspec.name == 'drag-threshold':
            return self._drag_threshold
        elif pspec.name == 'containment-type':
            return self._containment_type
        elif pspec.name == 'containment-area':
            return self._containment_area

    def do_set_property(self, pspec, value):
        if pspec.name == 'enabled':
            self._is_enabled = value
        elif pspec.name == 'axis':
            self._axis = value
        elif pspec.name == 'drag-threshold':
            self._drag_threshold = value
        elif pspec.name == 'containment-type':
            self._containment_type = value
        elif pspec.name == 'containment-area':
            self._containment_area = value

    def do_drag_begin(self, x, y, button, mod):
        orig_x, orig_y = self.get_transformed_position()
        self.reparent(stage)
        self.set_position(orig_x, orig_y)
        self.animate(clutter.EASE_OUT_CUBIC, 250, 'opacity', 224)

    def do_drag_motion(self, delta_x, delta_y):
        self.move_by(delta_x, delta_y)

    def do_drag_end(self, event_x, event_y):
        self.animate(clutter.EASE_OUT_CUBIC, 250, 'opacity', 255)


class DroppableGroup(clutter.Group, mx.Droppable):
    __gproperties__ = {
        'enabled': (gobject.TYPE_BOOLEAN, 'enabled', 'enabled', False,
                    gobject.PARAM_READWRITE),
    }
    def __init__(self):
        clutter.Group.__init__(self)
        self._is_enabled = False
        self._background = clutter.Rectangle()
        self._background.set_color((204, 204, 0, 255))
        self._background.set_size(200, 200)
        self.set_opacity(128)
        self.add(self._background)
        self.connect('over-in', self.on_over_in)
        self.connect('over-out', self.on_over_out)
        self.connect('drop', self.on_drop)

    def on_over_in(self, droppable, draggable):
        droppable.animate(clutter.EASE_OUT_CUBIC, 250, 'opacity', 255)

    def on_over_out(self, droppable, draggable):
        droppable.animate(clutter.EASE_OUT_CUBIC, 250, 'opacity', 128)

    def on_drop(self, droppable, draggable, event_x, event_y, button, modifier):
        draggable.reparent(self)
        x = 100
        if event_x < 100:
            x = 50
        y = 100
        if event_y < 100:
            y = 50
        draggable.set_position(x, y)


if __name__ == '__main__':
    stage = clutter.Stage()
    stage.connect('destroy', clutter.main_quit)
    stage.set_size(800, 600)

    rect_color1 = (146, 123,  81, 255)
    rect_color2 = (128, 195,  28, 255)
    rect_color3 = (255, 122,   2, 255)
    rect_color4 = (141, 195, 233, 255)

    droppable = DroppableGroup()
    stage.add(droppable)
    droppable.set_position(500, 50)
    droppable.set_reactive(True)
    droppable.set_name("Drop Target 1")
    droppable.enable()

    droppable = DroppableGroup()
    stage.add(droppable)
    droppable.set_position(500, 350)
    droppable.set_reactive(True)
    droppable.set_name("Drop Target 2")
    droppable.enable()

    draggable = DraggableRectangle()
    draggable.set_color(rect_color1)
    stage.add(draggable)
    draggable.set_size(50, 50)
    draggable.set_position(75, 250)
    draggable.set_reactive(True)
    draggable.enable()

    draggable = DraggableRectangle()
    draggable.set_color(rect_color2)
    stage.add(draggable)
    draggable.set_size(50, 50)
    draggable.set_position(125, 250)
    draggable.set_reactive(True)
    draggable.enable()

    draggable = DraggableRectangle()
    draggable.set_color(rect_color3)
    stage.add(draggable)
    draggable.set_size(50, 50)
    draggable.set_position(75, 300)
    draggable.set_reactive(True)
    draggable.enable()

    draggable = DraggableRectangle()
    draggable.set_color(rect_color4)
    stage.add(draggable)
    draggable.set_size(50, 50)
    draggable.set_position(125, 300)
    draggable.set_reactive(True)
    draggable.enable()

    stage.show()
    clutter.main()
