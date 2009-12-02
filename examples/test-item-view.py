from random import randint
import gobject
import clutter
import mx

sort_set = False
filter_set = False

def sort_func(model, a, b, data):
    return int(a.to_hls()[0] - b.to_hls()[0])

def filter_func(model, iter, data):
    color = iter.get(0)[0]
    h = color.to_hls()[0]
    return (h > 90 and h < 180)

def key_release_cb(stage, event, model):
    from clutter import keysyms
    global sort_set, filter_set
    if event.keyval == keysyms.s:
        if not sort_set:
            model.set_sort(0, sort_func, None)
        else:
            model.set_sort(-1, None, None)
        sort_set = not sort_set
    elif event.keyval == keysyms.f:
        if not filter_set:
            model.set_filter(filter_func)
        else:
            model.set_filter(None, None)
        filter_set = not filter_set


if __name__ == '__main__':
    stage = clutter.Stage()
    stage.connect('destroy', clutter.main_quit)
    stage.set_color((255, 255, 255, 255))
    stage.set_size(320, 240)
    color = clutter.Color(0x0, 0xf, 0xf, 0xf)

    scroll = mx.ScrollView()
    scroll.set_size(*stage.get_size())
    stage.add(scroll)

    view = mx.ItemView()
    scroll.add(view)

    model = clutter.ListModel(clutter.Color, "color", float, "size")

    for i in range(360):
        color = clutter.color_from_hls(randint(0, 255), 0.6, 0.6)
        color.alpha = 0xff
        model.append(0, color, 1, 32.0)

    view.set_model(model)
    view.set_item_type(clutter.Rectangle)
    view.add_attribute("color", 0)
    view.add_attribute("width", 1)
    view.add_attribute("height", 1)

    stage.connect('key-release-event', key_release_cb, model)
    
    stage.show()
    clutter.main()


