%define 	module	cryptkit
Summary:	Small, fast cryptographic toolkit for python
Summary(pl.UTF-8):	Mały i szybki zbiór narzędzi kryptograficznych dla pythona
Name:		python-%{module}
Version:	0.9
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/project/cryptkit/_cryptkit/Complete%20Kit/cryptkit-%{version}.tar.gz
# Source0-md5:	77e4693a153c31170e9ef6f4e29819ff
URL:		http://sourceforge.net/projects/cryptkit/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
#Requires:		python-libs
Requires:	python-modules
# BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CryptKit is a small, fast cryptographic toolkit for python. It
implements Rijndael(AES), SHA 256, Elliptic Curve PKI, Diffie-Hellman
key exchange and Nyberg-Ruppel signature/verification. Comprehensive
enough to provide a secure socket alternative to SSL

%description -l pl.UTF-8
CryptKit to mały, szybki zbiór narzędzi kryptograficznych dla
pythona. Implementuje Rijndael(AES), SHA 256, kryptografię krzywych
eliptycznych, wymianę kluczy Diffie-Hellman i sytem Nyberg-Ruppel.
Wystarczająco jasny aby być alternatywą dla SSL.

%prep
%setup -q -n %{module}-%{version}

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
# %{py_sitedir}/*.py[co]
# %{py_sitescriptdir}/%{module}
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/aes
%{py_sitedir}/cryptsock
%{py_sitedir}/ecc
%{py_sitedir}/entropy
%{py_sitedir}/sha256
%if "%{py_ver}" > "2.4"
%{py_sitedir}/TEMPLATE-*.egg-info
%endif
