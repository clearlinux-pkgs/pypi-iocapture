#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-iocapture
Version  : 0.1.2
Release  : 3
URL      : https://files.pythonhosted.org/packages/7a/9e/be3e278cec4f82b771b17a6c539a44d67081adb8042bc765776d77f3ea4a/iocapture-0.1.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/7a/9e/be3e278cec4f82b771b17a6c539a44d67081adb8042bc765776d77f3ea4a/iocapture-0.1.2.tar.gz
Summary  : Capture stdout, stderr easily.
Group    : Development/Tools
License  : LGPL-2.1 MIT
Requires: pypi-iocapture-license = %{version}-%{release}
Requires: pypi-iocapture-python = %{version}-%{release}
Requires: pypi-iocapture-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
.. highlight:: python
.. image:: https://secure.travis-ci.org/oinume/iocapture.png?branch=master

%package license
Summary: license components for the pypi-iocapture package.
Group: Default

%description license
license components for the pypi-iocapture package.


%package python
Summary: python components for the pypi-iocapture package.
Group: Default
Requires: pypi-iocapture-python3 = %{version}-%{release}

%description python
python components for the pypi-iocapture package.


%package python3
Summary: python3 components for the pypi-iocapture package.
Group: Default
Requires: python3-core
Provides: pypi(iocapture)

%description python3
python3 components for the pypi-iocapture package.


%prep
%setup -q -n iocapture-0.1.2
cd %{_builddir}/iocapture-0.1.2
pushd ..
cp -a iocapture-0.1.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656399593
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-iocapture
cp %{_builddir}/iocapture-0.1.2/COPYING %{buildroot}/usr/share/package-licenses/pypi-iocapture/01a6b4bf79aca9b556822601186afab86e8c4fbf
cp %{_builddir}/iocapture-0.1.2/LICENSE %{buildroot}/usr/share/package-licenses/pypi-iocapture/87d781b3a23bd13eef4b827bed888c9176d762d1
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-iocapture/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/pypi-iocapture/87d781b3a23bd13eef4b827bed888c9176d762d1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
