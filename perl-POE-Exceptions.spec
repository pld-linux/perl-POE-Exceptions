#
# Conditional build:
%bcond_without	tests # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	POE
%define		pnam	Exceptions
Summary:	POE::Exceptions - POE class for handling exceptions
Summary(pl):	POE::Exceptions - klasa POE do obs³ugi wyj±tków
Name:		perl-POE-Exceptions
Version:	0.03
Release:	2
License:	BSD-like
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b962d88f0bdcb2c9e63f0451cd7c4a29
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-POE >= 0.25
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
POE::Exceptions extends POE to catch exceptions neatly. A new signal,
"DIE", is introduced. This signal will be fired every time an
exception occurs. (For those of you new to the term exception, an
exception is whenever the code decides to bail out by "die"'ing.) If
the signal handler returns 1, POE will assume that the handler dealt
with the signal appropriately. If the signal handler returns 0, POE
will assume that the handler does not want to deal with the signal and
POE will propagate the exception as if the handler never existed.

%description -l pl
POE::Exceptions rozszerza POE o mi³y sposób przechwytywania wyj±tków.
Wprowadza nowy sygna³ "DIE". Ten sygna³ zostanie wys³any przy ka¿dym
wyst±pieniu wyj±tku (na wypadek, gdyby termin "wyj±tek" wydawa³ siê
obcy - wyj±tek wystêpuje wtedy, kiedy kod decyduje siê na awaryjne
zakoñczenie poprzez "die"). Je¶li procedura obs³ugi sygna³u zwróci 1,
POE za³o¿y, ¿e procedura poradzi³a sobie w³a¶ciwie z tym sygna³em.
Je¶li jednak zwróci 0, POE za³o¿y, ¿e procedura nie chce zajmowaæ siê
tym sygna³em, wiêc przeka¿e wyj±tek tak, jakby procedury obs³ugi nie
by³o.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES
%{perl_vendorlib}/POE/*.pm
%dir %{perl_vendorlib}/POE/Kernel
%{perl_vendorlib}/POE/Kernel/*.pm
%{perl_vendorlib}/POE/Session/*.pm
%{_mandir}/man3/*
