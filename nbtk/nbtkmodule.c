#include <pygobject.h>
#include <nbtk/nbtk.h>
 
void pynbtk_register_classes (PyObject *d); 
void pynbtk_add_constants (PyObject *module, const gchar *prefix);

extern PyMethodDef pynbtk_functions[];
 
static void
sink_nbtkaction (GObject *object)
{
  if (g_object_is_floating (object))
    g_object_ref_sink (object);
}

DL_EXPORT(void)
init_nbtk(void)
{
    PyObject *m, *d;
 
    init_pygobject_check (2, 12, 0);
 
    pygobject_register_sinkfunc (NBTK_TYPE_ACTION, sink_nbtkaction);

    m = Py_InitModule ("_nbtk", pynbtk_functions);
    d = PyModule_GetDict (m);
 
    pynbtk_register_classes (d);
    pynbtk_add_constants (m, "NBTK_");
 
    if (PyErr_Occurred ()) {
        Py_FatalError ("can't initialise module nbtk");
    }
}
