import clutter
import nbtk

if __name__ == '__main__':
    stage = clutter.Stage()
    stage.connect('destroy', clutter.main_quit)
    stage.set_color((255, 255, 255, 255))

    progress_bar = nbtk.ProgressBar()
    progress_bar.set_size(280, 75)
    progress_bar.set_position(20, 20)
    stage.add(progress_bar)

    animation = progress_bar.animate(clutter.LINEAR, 5000, "progress", 1.0)
    animation.set_loop(True)

    
    stage.show()
    clutter.main()


