#include <pygobject.h>
#include <clutter/clutter.h>
 
void pynbtk_register_classes (PyObject *d); 
void pynbtk_add_constants (PyObject *module, const gchar *prefix);

extern PyMethodDef pynbtk_functions[];
 
DL_EXPORT(void)
init_nbtk(void)
{
    PyObject *m, *d;
 
    init_pygobject_check (2, 12, 0);
 
    m = Py_InitModule ("_nbtk", pynbtk_functions);
    d = PyModule_GetDict (m);
 
    pynbtk_register_classes (d);
    pynbtk_add_constants (m, "NBTK_");
 
    if (PyErr_Occurred ()) {
        Py_FatalError ("can't initialise module nbtk");
    }
}
