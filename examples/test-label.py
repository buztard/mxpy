import clutter
import nbtk

if __name__ == '__main__':
    stage = clutter.Stage()
    stage.connect('destroy', clutter.main_quit)
    stage.set_size(400, 200)

    style = nbtk.style_get_default()
    style.load_from_file('style/default.css')

    label = nbtk.Label("Hello World!")
    label.set_position(50, 50)
    stage.add(label)

    stage.show()
    clutter.main()
