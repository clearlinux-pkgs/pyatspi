#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyatspi
Version  : 2.26.0
Release  : 8
URL      : https://download.gnome.org/sources/pyatspi/2.26/pyatspi-2.26.0.tar.xz
Source0  : https://download.gnome.org/sources/pyatspi/2.26/pyatspi-2.26.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0
Requires: pyatspi-python3
Requires: pyatspi-python
BuildRequires : pkgconfig(atk)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(dbus-glib-1)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(pygobject-3.0)

%description
D-Bus AT-SPI
------------
This version of at-spi is a major break from version 1.x.
It has been completely rewritten to use D-Bus rather than
ORBIT / CORBA for its transport protocol.

%package python
Summary: python components for the pyatspi package.
Group: Default
Requires: pyatspi-python3

%description python
python components for the pyatspi package.


%package python3
Summary: python3 components for the pyatspi package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pyatspi package.


%prep
%setup -q -n pyatspi-2.26.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1518716595
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1518716595
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
