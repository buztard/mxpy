include $(top_srcdir)/Makefile.tmpl

CLEANFILES =
EXTRA_DIST = 
INCLUDES = $(pynbtk_common_includes)

CREATEDEFS = $(PYTHON) $(top_srcdir)/createdefs.py

# nbtk python extension modules
pynbtkexecdir = $(pkgpyexecdir)/nbtk

# nbtk python scripts
pynbtkdir = $(pkgpythondir)/nbtk
pynbtk_PYTHON = __init__.py

# nbtk headers
pkgincludedir = $(includedir)/pynbtk-$(PLATFORM_VERSION)/pynbtk

NBTK_DEFS = nbtk-base.defs

NBTK_TYPES_DEFS = nbtk-base-types.defs

NBTK_OVERRIDES = 			\
	nbtk.override

CLEANFILES += 			\
	nbtk.c 			\
	nbtk-types.defs 	\
	nbtk.defs

EXTRA_DIST += 			\
	$(NBTK_DEFS)		\
	$(NBTK_TYPES_DEFS)	\
	$(NBTK_OVERRIDES)

nbtk.defs: $(NBTK_DEFS) Makefile
	$(QUIET_GEN)$(CREATEDEFS) $@ $(NBTK_DEFS)


nbtk-types.defs: $(NBTK_TYPES_DEFS) Makefile
	$(QUIET_GEN)$(CREATEDEFS) $@ $(NBTK_TYPES_DEFS)

nbtk.c: nbtk-types.defs nbtk.defs $(NBTK_OVERRIDES)

_nbtk_la_CFLAGS  = $(PYCAIRO_CFLAGS) $(NBTK_CFLAGS) $(NBTKGTK_CFLAGS)
_nbtk_la_LDFLAGS = $(pynbtk_common_ldflags) -export-symbols-regex init_nbtk
_nbtk_la_LIBADD  = $(PYCAIRO_LIBS) $(PYGTK_LIBS) $(NBTK_LIBS) $(NBTKGTK_LIBS)
_nbtk_la_SOURCES = 		\
	nbtkmodule.c
nodist__nbtk_la_SOURCES = nbtk.c

pynbtkexec_LTLIBRARIES = _nbtk.la

# defs files
defsdir = $(pynbtk_defsdir)
defs_DATA = \
	$(NBTK_DEFS) 	\
	$(NBTK_TYPES_DEFS) 	\
	nbtk.defs		\
	nbtk-types.defs

.defs.c:
	$(QUIET_GEN)( $(PYGOBJECT_CODEGEN) \
	   $(PYGOBJECT_CODEGEN_DEFINES) \
	    -I $(srcdir) \
	    --py_ssize_t-clean \
	    --register $(PYGTK_DEFSDIR)/gdk-types.defs \
	    --register $(PYGTK_DEFSDIR)/pango-types.defs \
	    --register $(PYCLUTTER_DEFSDIR)/clutter-base-types.defs \
	    --register nbtk-types.defs \
	    --override $(srcdir)/$*.override \
	    --prefix py$* $< ) > gen-$*.c \
	&& cp -f gen-$*.c $*.c \
	&& rm -f gen-$*.c

# this is a hack - do not remove
# this rule is needed to prevent generating nbtk-types.c because
# we have nbtk-types.defs
#nbtk-types.c:
#	@:

