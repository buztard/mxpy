AC_PREREQ(2.53)

# pymx package version number, (as distinct from shared library version)
# An odd micro number indicates in-progress development, (eg. from svn)
# An even micro number indicates a released version.
m4_define(pymx_version_major, 0)
m4_define(pymx_version_minor, 0)
m4_define(pymx_version_micro, 1)
m4_define(pymx_version, pymx_version_major.pymx_version_minor.pymx_version_micro)

m4_define(clutter_required_version,      1.0.0)
m4_define(mx_required_version,         0.2.0)
m4_define(mxgtk_required_version,      0.2.0)
m4_define(pyclutter_required_version,    1.0.0)
m4_define(pygtk_required_version,        2.8.0)

AC_INIT([pymx], [pymx_version],
        [http://bugzilla.o-hand.com/enter_bug.cgi?product=Clutter])

AC_DEFINE(PYMX_MAJOR_VERSION,
          [pymx_version_major], [pymx major version])
AC_SUBST(PYMX_MAJOR_VERSION, [pymx_version_major])
AC_DEFINE(PYMX_MINOR_VERSION,
          [pymx_version_minor], [pymx minor version])
AC_SUBST(PYMX_MINOR_VERSION, [pymx_version_minor])
AC_DEFINE(PYMX_MICRO_VERSION, [pymx_version_micro],
          [pymx micro version])
AC_SUBST(PYMX_MICRO_VERSION, [pymx_version_micro])
AC_DEFINE(PYMX_VERSION, [pymx_version], [pymx version])
AC_SUBST(PYMX_VERSION, [pymx_version])

AC_CONFIG_SRCDIR([mx/mxmodule.c])
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

dnl check for mx
PKG_CHECK_MODULES(MX, mx-1.0 = mx_required_version)
AC_SUBST(MX_CFLAGS)
AC_SUBST(MX_LIBS)
if test -n "$export_dynamic"; then
  MX_LIBS=`echo $MX_LIBS | sed -e "s/$export_dynamic//"`
fi

dnl check for mx-gtk
PKG_CHECK_MODULES(MXGTK, mx-gtk-1.0 >= mxgtk_required_version)
AC_SUBST(MXGTK_CFLAGS)
AC_SUBST(MXGTK_LIBS)
if test -n "$export_dynamic"; then
  MXGTK_LIBS=`echo $MXGTK_LIBS | sed -e "s/$export_dynamic//"`
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
        pymx.pc
        mx/Makefile
        examples/Makefile
])

AC_OUTPUT

