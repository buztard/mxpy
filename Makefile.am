SUBDIRS = build mx examples

mxpy-$(MXPY_MAJOR_VERSION).$(MXPY_MINOR_VERSION).pc: mxpy.pc
	@cp -f $< $(@F)

pkgfiles = mxpy-$(MXPY_MAJOR_VERSION).$(MXPY_MINOR_VERSION).pc
pkgconfigdir = $(libdir)/pkgconfig
pkgconfig_DATA = $(pkgfiles)

DISTCHECK_CONFIGURE_FLAGS = --enable-docs

DIST_SUBDIRS = \
	mx \
	build \
	examples

EXTRA_DIST = createdefs.py py-compile Makefile.tmpl

CLEANFILES = $(pkgfiles)

# Extra clean files so that maintainer-clean removes *everything*
MAINTAINERCLEANFILES = \
	aclocal.m4 \
	compile \
	config.guess \
	config.sub \
	configure \
	depcomp \
	install-sh \
	ltmain.sh \
	Makefile.in \
	missing \
	config.h.in

