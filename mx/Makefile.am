include $(top_srcdir)/Makefile.tmpl

CLEANFILES =
EXTRA_DIST = 
INCLUDES = $(pymx_common_includes)

CREATEDEFS = $(PYTHON) $(top_srcdir)/createdefs.py

# mx python extension modules
pymxexecdir = $(pkgpyexecdir)/mx

# mx python scripts
pymxdir = $(pkgpythondir)/mx
pymx_PYTHON = __init__.py

# mx headers
pkgincludedir = $(includedir)/pymx-$(PLATFORM_VERSION)/pymx

MX_DEFS = mx-base.defs

MX_TYPES_DEFS = mx-base-types.defs

MX_OVERRIDES = 			\
	mx.override

CLEANFILES += 			\
	mx.c 			\
	mx-types.defs 	\
	mx.defs

EXTRA_DIST += 			\
	$(MX_DEFS)		\
	$(MX_TYPES_DEFS)	\
	$(MX_OVERRIDES)

mx.defs: $(MX_DEFS) Makefile
	$(QUIET_GEN)$(CREATEDEFS) $@ $(MX_DEFS)


mx-types.defs: $(MX_TYPES_DEFS) Makefile
	$(QUIET_GEN)$(CREATEDEFS) $@ $(MX_TYPES_DEFS)

mx.c: mx-types.defs mx.defs $(MX_OVERRIDES)

_mx_la_CFLAGS  = $(PYCAIRO_CFLAGS) $(PYTHON_INCLUDES) $(PYGTK_CFLAGS) $(MX_CFLAGS) $(MXGTK_CFLAGS)
_mx_la_LDFLAGS = $(pymx_common_ldflags) -module -export-symbols-regex init_mx
_mx_la_LIBADD  = $(PYCAIRO_LIBS) $(PYGTK_LIBS) $(MX_LIBS) $(MXGTK_LIBS)
_mx_la_SOURCES = 		\
	mxmodule.c
nodist__mx_la_SOURCES = mx.c

pymxexec_LTLIBRARIES = _mx.la

# defs files
defsdir = $(pymx_defsdir)
defs_DATA = \
	$(MX_DEFS) 	\
	$(MX_TYPES_DEFS) 	\
	mx.defs		\
	mx-types.defs

.defs.c:
	$(QUIET_GEN)( $(PYGOBJECT_CODEGEN) \
	   $(PYGOBJECT_CODEGEN_DEFINES) \
	    -I $(srcdir) \
	    --py_ssize_t-clean \
	    --register $(PYGTK_DEFSDIR)/gdk-types.defs \
	    --register $(PYGTK_DEFSDIR)/pango-types.defs \
	    --register $(PYCLUTTER_DEFSDIR)/clutter-base-types.defs \
	    --register mx-types.defs \
	    --override $(srcdir)/$*.override \
	    --prefix py$* $< ) > gen-$*.c \
	&& cp -f gen-$*.c $*.c \
	&& rm -f gen-$*.c

# this is a hack - do not remove
# this rule is needed to prevent generating mx-types.c because
# we have mx-types.defs
#mx-types.c:
#	@:

