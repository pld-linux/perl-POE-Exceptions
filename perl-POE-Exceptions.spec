#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	POE
%define	pnam	Exceptions
Summary:	POE::Exceptions - POE class for handling exceptions
Summary(pl):	POE::Exceptions - klasa POE do obs�ugi wyj�tk�w
Name:		perl-POE-Exceptions
Version:	0.02
Release:	1
License:	BSD-like
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	599004002a158c9fdd095258c0a9afd8
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{!?_without_tests:1}0
BuildRequires:	perl-POE >= 0.22
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
POE::Exceptions rozszerza POE o mi�y spos�b przechwytywania wyj�tk�w.
Wprowadza nowy sygna� "DIE". Ten sygna� zostanie wys�any przy ka�dym
wyst�pieniu wyj�tku (na wypadek, gdyby termin "wyj�tek" wydawa� si�
obcy - wyj�tek wyst�puje wtedy, kiedy kod decyduje si� na awaryjne
zako�czenie poprzez "die"). Je�li procedura obs�ugi sygna�u zwr�ci 1,
POE za�o�y, �e procedura poradzi�a sobie w�a�ciwie z tym sygna�em.
Je�li jednak zwr�ci 0, POE za�o�y, �e procedura nie chce zajmowa� si�
tym sygna�em, wi�c przeka�e wyj�tek tak, jakby procedury obs�ugi nie
by�o.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/*/*.pm
%{_mandir}/man3/*
