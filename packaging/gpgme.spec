#
# spec file for package gpgme
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name:           gpgme
BuildRequires:  gpg2 >= 2.0.10
Version:        1.3.2
Release:        0
Summary:        A Library Designed to Give Applications Easy Access to GnuPG
License:        GPL-2.0+
Group:          Productivity/Security
Url:            http://www.gnupg.org/related_software/gpgme/
Source:         ftp://ftp.gnupg.org/gcrypt/gpgme/%{name}-%{version}.tar.bz2
Patch0:         gpgme-1.3.2-gpgme-config-remove-extraneous-libs.patch
Source2:        baselibs.conf
BuildRequires:  automake
BuildRequires:  libassuan-devel >= 2.0.2
BuildRequires:  libgpg-error-devel >= 1.8

%description
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG
easier for applications. It provides a high-level Crypto API for
encryption, decryption, signing, signature verification, and key
management. Currently it uses GnuPG as its back-end, but the API is not
restricted to this engine.

Because the direct use of GnuPG from an application can be a
complicated programming task, it is suggested that all software should
try to use GPGME instead. This way bug fixes or improvements can be
done at a central place and every application benefits from this.
Authors of MUAs should especially consider using GPGME. Creating a set
of standard widgets for common key selection tasks is even planned.

%package -n libgpgme
Summary:        A Library Designed to give Applications easy Access to GnuPG
Group:          Development/Libraries
Requires:       gpg2

%description -n libgpgme
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG
easier for applications. It provides a high-level Crypto API for
encryption, decryption, signing, signature verification, and key
management. Currently it uses GnuPG as its back-end, but the API is not
restricted to this engine.

Who Should use GPGME?

Because the direct use of GnuPG from an application can be a
complicated programming task, it is suggested that all software should
try to use GPGME instead. This way bug fixes or improvements can be
done at a central place and every application benefits from this.
Authors of MUAs should especially consider using GPGME. Creating a set
of standard widgets for common key selection tasks is even planned.

%package -n libgpgme-devel
Summary:        A Library Designed to give Applications easy Access to GnuPG
Group:          Development/Libraries
Requires:       glibc-devel
Requires:       libgpg-error-devel
Requires:       libgpgme = %{version}

%description -n libgpgme-devel
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG
easier for applications. It provides a high-level Crypto API for
encryption, decryption, signing, signature verification, and key
management. Currently it uses GnuPG as its back-end, but the API is not
restricted to this engine.

Who Should use GPGME?

Because the direct use of GnuPG from an application can be a
complicated programming task, it is suggested that all software should
try to use GPGME instead. This way bug fixes or improvements can be
done at a central place and every application benefits from this.
Authors of MUAs should especially consider using GPGME. Creating a set
of standard widgets for common key selection tasks is even planned.

%prep
%setup -q
%patch0

%build
sh autogen.sh
# Ensure that a (re)build uses fixed binaries with minimum version because
# in case configure picks GnuPG-1.x, e.g. from /usr/local, this would cause
# testsuite failures:
%configure --without-pth --disable-static \
	--with-gpg-version=2.0.10	\
	--with-gpgsm-version=2.0.10	\
	--with-gpgconf-version=2.0.10	\
	--with-gpg=%{_bindir}/gpg2	\
	--with-gpgsm=%{_bindir}/gpgsm	\
	--with-gpgconf=%{_bindir}/gpgconf

%install
%make_install

%check
%if ! 0%{?qemu_user_space_build}
make check
%endif


%post -n libgpgme -p /sbin/ldconfig

%postun -n libgpgme -p /sbin/ldconfig


%files
%defattr(-,root,root)
%license COPYING
%{_datadir}/common-lisp
%{_datadir}/common-lisp/source
%{_infodir}/gpgme*

%files -n libgpgme
%defattr(-,root,root)
%{_libdir}/libgpgme.so.*
%{_libdir}/libgpgme-pthread.so.*

%files -n libgpgme-devel
%defattr(-,root,root)
%{_libdir}/libgpgme.so
%{_libdir}/libgpgme-pthread.so
%{_bindir}/gpgme-config
%{_datadir}/aclocal/gpgme.m4
%{_includedir}/gpgme.h

%changelog
