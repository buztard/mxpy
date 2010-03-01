#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

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

static void
sink_mxbuttongroup (GObject *object)
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
    pygobject_register_sinkfunc (MX_TYPE_BUTTON_GROUP, sink_mxbuttongroup);

    m = Py_InitModule ("_mx", pymx_functions);
    d = PyModule_GetDict (m);
 
    /* mxpy version */
    PyModule_AddObject (m, "__version__",
                        Py_BuildValue ("(iii)",
                                       MXPY_MAJOR_VERSION,
                                       MXPY_MINOR_VERSION,
                                       MXPY_MICRO_VERSION));

    /* mx version */
    PyModule_AddObject (m, "mx_version",
                        Py_BuildValue ("(iii)",
                                       MX_MAJOR_VERSION,
                                       MX_MINOR_VERSION,
                                       MX_MICRO_VERSION));

    pymx_register_classes (d);
    pymx_add_constants (m, "MX_");
 
    if (PyErr_Occurred ()) {
        Py_FatalError ("can't initialise module mx");
    }
}
