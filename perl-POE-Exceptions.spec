#
# Conditional build:
%bcond_without	tests # do not perform "make test"

%define		pdir	POE
%define		pnam	Exceptions
Summary:	POE::Exceptions - POE class for handling exceptions
Summary(pl.UTF-8):	POE::Exceptions - klasa POE do obsługi wyjątków
Name:		perl-POE-Exceptions
Version:	0.0502
Release:	0.1
License:	BSD-like
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7038eaa58356a78d0af6f9d3a5d2c53d
URL:		http://search.cpan.org/dist/POE-Exceptions/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-POE >= 0.25
BuildRequires:	perl-Test-Distribution
%endif
Conflicts:	perl-POE >= 0.33
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

%description -l pl.UTF-8
POE::Exceptions rozszerza POE o miły sposób przechwytywania wyjątków.
Wprowadza nowy sygnał "DIE". Ten sygnał zostanie wysłany przy każdym
wystąpieniu wyjątku (na wypadek, gdyby termin "wyjątek" wydawał się
obcy - wyjątek występuje wtedy, kiedy kod decyduje się na awaryjne
zakończenie poprzez "die"). Jeśli procedura obsługi sygnału zwróci 1,
POE założy, że procedura poradziła sobie właściwie z tym sygnałem.
Jeśli jednak zwróci 0, POE założy, że procedura nie chce zajmować się
tym sygnałem, więc przekaże wyjątek tak, jakby procedury obsługi nie
było.

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
