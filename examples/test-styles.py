import clutter
import mxpy as mx

def create_button(parent, text, x, y):
    button = mx.Button(text)
    parent.add(button)
    button.set_size(150, 100)
    button.set_position(x, y)
    return button

if __name__ == '__main__':
    stage = clutter.Stage()
    stage.connect('destroy', clutter.main_quit)

    style = mx.style_get_default()
    style.load_from_file('style/default.css')

    button = create_button(stage, "Default Style", 100, 100)
    button.set_name('default-button')

    button = create_button(stage, "Red Style", 100, 300)
    button.set_name('red-button')

    button = create_button(stage, "Green Style", 350, 100)
    button.set_name('green-button')

    button = create_button(stage, "Blue Style", 350, 300)
    button.set_name('blue-button')

    table = mx.Table()
    table.set_size(200, 80)
    stage.add(table)
    table.set_position(200, 215)

    button = mx.Button("Container Test")
    button.set_name('container-button')
    table.add_actor(button, 0, 0)

    stage.show()
    clutter.main()
