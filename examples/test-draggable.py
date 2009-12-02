import gobject
import clutter
import mx


class DraggableRectangle(clutter.Rectangle, mx.Draggable):
    __gtype_name__ = 'DraggableRectangle'
    __gproperties__ = {
        'enabled': (gobject.TYPE_BOOLEAN, 'enabled', 'enabled', False,
                    gobject.PARAM_READWRITE),
        'axis': (mx.DragAxis, 'axis', 'axis', mx.NO_AXIS,
                 gobject.PARAM_READWRITE),
        'drag-threshold': (gobject.TYPE_UINT,
                           'drag threshold','drag threshold',
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
        self.set_opacity(224)
        self.set_rotation(clutter.Y_AXIS, 30.0, self.get_width()/2, 0,
                self.get_height()/2)

    def do_drag_motion(self, delta_x, delta_y):
        self.move_by(delta_x, delta_y)

    def do_drag_end(self, event_x, event_y):
        self.set_opacity(255)
        self.set_rotation(clutter.Y_AXIS, 0.0, 0, 0, 0)


if __name__ == '__main__':
    stage = clutter.Stage()
    stage.connect('destroy', clutter.main_quit)
    stage.set_title('Draggable Example')
    stage.set_size(800, 600)

    draggable = DraggableRectangle()
    stage.add(draggable)
    draggable.set_color((204, 204, 204, 255))
    draggable.set_size(100, 100)
    draggable.set_position(350, 100)
    draggable.set_reactive(True)
    draggable.set_name('h-handle')
    draggable.set_axis(mx.X_AXIS)
    draggable.enable()

    draggable = DraggableRectangle()
    stage.add(draggable)
    draggable.set_color((204, 204, 204, 255))
    draggable.set_size(100, 100)
    draggable.set_position(350, 300)
    draggable.set_reactive(True)
    draggable.set_name('v-handle')
    draggable.set_axis(mx.Y_AXIS)
    draggable.enable()

    stage.show()
    clutter.main()
