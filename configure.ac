AC_PREREQ(2.53)

# pynbtk package version number, (as distinct from shared library version)
# An odd micro number indicates in-progress development, (eg. from svn)
# An even micro number indicates a released version.
m4_define(pynbtk_version_major, 0)
m4_define(pynbtk_version_minor, 0)
m4_define(pynbtk_version_micro, 1)
m4_define(pynbtk_version, pynbtk_version_major.pynbtk_version_minor.pynbtk_version_micro)

m4_define(clutter_required_version,      1.0.0)
m4_define(nbtk_required_version,         1.1.4)
m4_define(nbtkgtk_required_version,      1.1.4)
m4_define(pyclutter_required_version,    1.0.0)
m4_define(pygtk_required_version,        2.8.0)

AC_INIT([pynbtk], [pynbtk_version],
        [http://bugzilla.o-hand.com/enter_bug.cgi?product=Clutter])

AC_DEFINE(PYNBTK_MAJOR_VERSION,
          [pynbtk_version_major], [pynbtk major version])
AC_SUBST(PYNBTK_MAJOR_VERSION, [pynbtk_version_major])
AC_DEFINE(PYNBTK_MINOR_VERSION,
          [pynbtk_version_minor], [pynbtk minor version])
AC_SUBST(PYNBTK_MINOR_VERSION, [pynbtk_version_minor])
AC_DEFINE(PYNBTK_MICRO_VERSION, [pynbtk_version_micro],
          [pynbtk micro version])
AC_SUBST(PYNBTK_MICRO_VERSION, [pynbtk_version_micro])
AC_DEFINE(PYNBTK_VERSION, [pynbtk_version], [pynbtk version])
AC_SUBST(PYNBTK_VERSION, [pynbtk_version])

AC_CONFIG_SRCDIR([nbtk/nbtkmodule.c])
AC_CONFIG_MACRO_DIR([build/autotools])
AM_CONFIG_HEADER(config.h)

AM_INIT_AUTOMAKE([1.9])

dnl put the ACLOCAL flags in the makefile
ACLOCAL="$ACLOCAL $ACLOCAL_FLAGS"

AC_CANONICAL_BUILD
AC_CANONICAL_HOST

AC_DISABLE_STATIC
AC_LIBTOOL_WIN32_DLL
AC_PROG_LIBTOOL

# uncomment in 0.7
#AM_PATH_PYTHON(2.5.0,,[AC_MSG_ERROR([could not find Python 2.5.0])])
AM_PATH_PYTHON(2.4.0,,[AC_MSG_ERROR([could not find Python 2.4.0])])
AM_CHECK_PYTHON_HEADERS(,[AC_MSG_ERROR([could not find Python headers])])

PLATFORM=`$PYTHON -c "from distutils import util; print util.get_platform()"`
AC_SUBST(PLATFORM)

dnl get rid of the -export-dynamic stuff from the configure flags ...
export_dynamic=`(./libtool --config; echo eval echo \\$export_dynamic_flag_spec) | sh`

# Checks for programs.
AC_PROG_CC

# Checks for header files.
AC_HEADER_STDC
AC_CHECK_HEADERS([fcntl.h stdlib.h string.h unistd.h])

# Checks for typedefs, structures, and compiler characteristics.
AC_C_CONST

dnl check for pygobject-codegen
AC_PATH_PROGS(PYGOBJECT_CODEGEN, pygobject-codegen-2.0 pygtk-codegen-2.0, no)
if test "x$PYGOBJECT_CODEGEN" = "xno"; then
  AC_MSG_ERROR([could not find pygobject-codegen-2.0 script])
fi

PYGOBJECT_CODEGEN_DEFINES=

dnl check for pyclutter
PKG_CHECK_MODULES(PYCLUTTER, pyclutter-1.0 >= pyclutter_required_version)
AC_SUBST(PYCLUTTER_CFLAGS)

AC_MSG_CHECKING(for pyclutter defs)
PYCLUTTER_DEFSDIR=`$PKG_CONFIG --variable=defsdir pyclutter-1.0`
AC_SUBST(PYCLUTTER_DEFSDIR)
AC_MSG_RESULT($PYCLUTTER_DEFSDIR)

dnl check for pygtk
PKG_CHECK_MODULES(PYGTK, pygtk-2.0 >= pygtk_required_version)
AC_SUBST(PYGTK_CFLAGS)

AC_MSG_CHECKING(for pygtk defs)
PYGTK_DEFSDIR=`$PKG_CONFIG --variable=defsdir pygtk-2.0`
AC_SUBST(PYGTK_DEFSDIR)
AC_MSG_RESULT($PYGTK_DEFSDIR)

dnl check for clutter
PKG_CHECK_MODULES(CLUTTER, clutter-1.0 >= clutter_required_version)
AC_SUBST(CLUTTER_CFLAGS)
AC_SUBST(CLUTTER_LIBS)
if test -n "$export_dynamic"; then
  CLUTTER_LIBS=`echo $CLUTTER_LIBS | sed -e "s/$export_dynamic//"`
fi

dnl check for nbtk
PKG_CHECK_MODULES(NBTK, nbtk-1.2 = nbtk_required_version)
AC_SUBST(NBTK_CFLAGS)
AC_SUBST(NBTK_LIBS)
if test -n "$export_dynamic"; then
  NBTK_LIBS=`echo $NBTK_LIBS | sed -e "s/$export_dynamic//"`
fi

dnl check for nbtk-gtk
PKG_CHECK_MODULES(NBTKGTK, nbtk-gtk-1.2 >= nbtkgtk_required_version)
AC_SUBST(NBTKGTK_CFLAGS)
AC_SUBST(NBTKGTK_LIBS)
if test -n "$export_dynamic"; then
  NBTKGTK_LIBS=`echo $NBTKGTK_LIBS | sed -e "s/$export_dynamic//"`
fi


dnl add required cflags ...
JH_ADD_CFLAG([-Wall])
#JH_ADD_CFLAG([-std=c9x])
JH_ADD_CFLAG([-fno-strict-aliasing])

SHAVE_INIT([build/autotools], [enable])

AC_CONFIG_FILES([
        Makefile
		build/Makefile
		build/autotools/Makefile
		build/autotools/shave-libtool
		build/autotools/shave
        pynbtk.pc
        nbtk/Makefile
		examples/Makefile
])

AC_OUTPUT

