#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v16
# autospec commit: b858a2a
#
Name     : libdnf
Version  : 0.73.2
Release  : 63
URL      : https://github.com/rpm-software-management/libdnf/archive/0.73.2/libdnf-0.73.2.tar.gz
Source0  : https://github.com/rpm-software-management/libdnf/archive/0.73.2/libdnf-0.73.2.tar.gz
Summary  : Library providing simplified C and Python API to libsolv
Group    : Development/Tools
License  : LGPL-2.1 LGPL-2.1+
Requires: libdnf-lib = %{version}-%{release}
Requires: libdnf-license = %{version}-%{release}
Requires: libdnf-locales = %{version}-%{release}
Requires: libdnf-python = %{version}-%{release}
Requires: libdnf-python3 = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : gettext-dev
BuildRequires : git
BuildRequires : glibc-bin
BuildRequires : gtk-doc-data
BuildRequires : libassuan-dev
BuildRequires : perl
BuildRequires : pkg-config
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(cppunit)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gobject-introspection-1.0)
BuildRequires : pkgconfig(gtk-doc)
BuildRequires : pkgconfig(json-c)
BuildRequires : pkgconfig(librepo)
BuildRequires : pkgconfig(libsolv)
BuildRequires : pkgconfig(modulemd-2.0)
BuildRequires : pkgconfig(rpm)
BuildRequires : pkgconfig(smartcols)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : pypi-sphinx
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : swig
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Fix-lookup-for-LibSolv-package.patch
Patch2: 0002-do-fewer-fsyncs.patch

%description
A Library providing simplified C and Python API to libsolv.

%package dev
Summary: dev components for the libdnf package.
Group: Development
Requires: libdnf-lib = %{version}-%{release}
Provides: libdnf-devel = %{version}-%{release}
Requires: libdnf = %{version}-%{release}

%description dev
dev components for the libdnf package.


%package lib
Summary: lib components for the libdnf package.
Group: Libraries
Requires: libdnf-license = %{version}-%{release}

%description lib
lib components for the libdnf package.


%package license
Summary: license components for the libdnf package.
Group: Default

%description license
license components for the libdnf package.


%package locales
Summary: locales components for the libdnf package.
Group: Default

%description locales
locales components for the libdnf package.


%package python
Summary: python components for the libdnf package.
Group: Default
Requires: libdnf-python3 = %{version}-%{release}

%description python
python components for the libdnf package.


%package python3
Summary: python3 components for the libdnf package.
Group: Default
Requires: python3-core

%description python3
python3 components for the libdnf package.


%prep
%setup -q -n libdnf-0.73.2
cd %{_builddir}/libdnf-0.73.2
%patch -P 1 -p1
%patch -P 2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1721346258
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DWITH_BINDINGS=ON \
-DWITH_GTKDOC=OFF \
-DWITH_HTML=OFF \
-DWITH_MAN=ON \
-DWITH_ZCHUNK=OFF \
-DENABLE_RHSM_SUPPORT=OFF \
-DENABLE_SOLV_URPMREORDER=OFF \
-DPYTHON_DESIRED=3  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test || :

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1721346258
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libdnf
cp %{_builddir}/libdnf-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libdnf/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang libdnf

%files
%defattr(-,root,root,-)
/usr/lib64/libdnf/plugins/README

%files dev
%defattr(-,root,root,-)
/usr/include/libdnf/conf/Config.hpp
/usr/include/libdnf/conf/ConfigMain.hpp
/usr/include/libdnf/conf/ConfigParser.hpp
/usr/include/libdnf/conf/ConfigRepo.hpp
/usr/include/libdnf/conf/Option.hpp
/usr/include/libdnf/conf/OptionBinds.hpp
/usr/include/libdnf/conf/OptionBool.hpp
/usr/include/libdnf/conf/OptionChild.hpp
/usr/include/libdnf/conf/OptionEnum.hpp
/usr/include/libdnf/conf/OptionNumber.hpp
/usr/include/libdnf/conf/OptionPath.hpp
/usr/include/libdnf/conf/OptionSeconds.hpp
/usr/include/libdnf/conf/OptionString.hpp
/usr/include/libdnf/conf/OptionStringList.hpp
/usr/include/libdnf/config.h
/usr/include/libdnf/dnf-advisory.h
/usr/include/libdnf/dnf-advisorypkg.h
/usr/include/libdnf/dnf-advisoryref.h
/usr/include/libdnf/dnf-conf.h
/usr/include/libdnf/dnf-context.h
/usr/include/libdnf/dnf-db.h
/usr/include/libdnf/dnf-enums.h
/usr/include/libdnf/dnf-goal.h
/usr/include/libdnf/dnf-keyring.h
/usr/include/libdnf/dnf-lock.h
/usr/include/libdnf/dnf-package.h
/usr/include/libdnf/dnf-packagedelta.h
/usr/include/libdnf/dnf-reldep-list.h
/usr/include/libdnf/dnf-reldep.h
/usr/include/libdnf/dnf-repo-loader.h
/usr/include/libdnf/dnf-repo.h
/usr/include/libdnf/dnf-rpmts.h
/usr/include/libdnf/dnf-sack.h
/usr/include/libdnf/dnf-state.h
/usr/include/libdnf/dnf-transaction.h
/usr/include/libdnf/dnf-types.h
/usr/include/libdnf/dnf-utils.h
/usr/include/libdnf/dnf-version.h
/usr/include/libdnf/hy-goal.h
/usr/include/libdnf/hy-nevra.h
/usr/include/libdnf/hy-package.h
/usr/include/libdnf/hy-packageset.h
/usr/include/libdnf/hy-query.h
/usr/include/libdnf/hy-repo.h
/usr/include/libdnf/hy-selector.h
/usr/include/libdnf/hy-subject.h
/usr/include/libdnf/hy-types.h
/usr/include/libdnf/hy-util.h
/usr/include/libdnf/libdnf.h
/usr/include/libdnf/log.hpp
/usr/include/libdnf/nevra.hpp
/usr/include/libdnf/nsvcap.hpp
/usr/include/libdnf/plugin/plugin.h
/usr/include/libdnf/utils/PreserveOrderMap.hpp
/usr/include/libdnf/utils/logger.hpp
/usr/lib64/libdnf.so
/usr/lib64/pkgconfig/libdnf.pc
/usr/share/man/man3/hawkey.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libdnf.so.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libdnf/01a6b4bf79aca9b556822601186afab86e8c4fbf

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files locales -f libdnf.lang
%defattr(-,root,root,-)

