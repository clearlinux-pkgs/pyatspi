#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyatspi
Version  : 2.38.1
Release  : 32
URL      : https://download.gnome.org/sources/pyatspi/2.38/pyatspi-2.38.1.tar.xz
Source0  : https://download.gnome.org/sources/pyatspi/2.38/pyatspi-2.38.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0 Python-2.0
Requires: pyatspi-license = %{version}-%{release}
Requires: pyatspi-python = %{version}-%{release}
Requires: pyatspi-python3 = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : pkgconfig(atk)
BuildRequires : pkgconfig(atspi-2)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(pygobject-3.0)

%description
D-Bus AT-SPI
------------
This version of at-spi is a major break from version 1.x.
It has been completely rewritten to use D-Bus rather than
ORBIT / CORBA for its transport protocol.

%package license
Summary: license components for the pyatspi package.
Group: Default

%description license
license components for the pyatspi package.


%package python
Summary: python components for the pyatspi package.
Group: Default
Requires: pyatspi-python3 = %{version}-%{release}

%description python
python components for the pyatspi package.


%package python3
Summary: python3 components for the pyatspi package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pyatspi package.


%prep
%setup -q -n pyatspi-2.38.1
cd %{_builddir}/pyatspi-2.38.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1615910562
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1615910562
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyatspi
cp %{_builddir}/pyatspi-2.38.1/COPYING %{buildroot}/usr/share/package-licenses/pyatspi/e8d05da65f87ed0a4a38615cd4f1d9c21cce531b
cp %{_builddir}/pyatspi-2.38.1/COPYING.GPL %{buildroot}/usr/share/package-licenses/pyatspi/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
cp %{_builddir}/pyatspi-2.38.1/tests/pyatspi/pasytest/COPYING-PSF %{buildroot}/usr/share/package-licenses/pyatspi/1cd860a7e028ea38573d27165b529439037321f3
%make_install

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyatspi/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/pyatspi/1cd860a7e028ea38573d27165b529439037321f3
/usr/share/package-licenses/pyatspi/e8d05da65f87ed0a4a38615cd4f1d9c21cce531b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
