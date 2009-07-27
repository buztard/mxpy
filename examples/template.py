import clutter
import nbtk

if __name__ == '__main__':
    stage = clutter.Stage()
    stage.connect('destroy', clutter.main_quit)
    stage.set_color((255, 255, 255, 255))
    
    stage.show()
    clutter.main()


