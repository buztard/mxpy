#include <pygobject.h>
#include <mx/mx.h>
 
void pymx_register_classes (PyObject *d); 
void pymx_add_constants (PyObject *module, const gchar *prefix);

extern PyMethodDef pymx_functions[];
 
static void
sink_mxaction (GObject *object)
{
  if (g_object_is_floating (object))
    g_object_ref_sink (object);
}

DL_EXPORT(void)
init_mx(void)
{
    PyObject *m, *d;
 
    init_pygobject_check (2, 12, 0);
 
    pygobject_register_sinkfunc (MX_TYPE_ACTION, sink_mxaction);

    m = Py_InitModule ("_mx", pymx_functions);
    d = PyModule_GetDict (m);
 
    pymx_register_classes (d);
    pymx_add_constants (m, "MX_");
 
    if (PyErr_Occurred ()) {
        Py_FatalError ("can't initialise module mx");
    }
}
