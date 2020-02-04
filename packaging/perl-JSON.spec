Name:       perl-JSON
Version:    4.02
Release:    1
Summary:    A Perl module for JSON (JavaScript Object Notation) encoder/decoder
Group:      Development/Libraries
License:    GPL-2.0+ or Artistic
URL:        http://search.cpan.org/dist/JSON
Source0:    %{name}-%{version}.tar.gz
Source1001: perl-JSON.manifest
BuildArch:  noarch
BuildRequires:  perl

%description
This module is a thin wrapper for JSON::XS-compatible modules with a few additional features. All the backend modules convert a Perl data structure to a JSON text and vice versa.

%prep
%setup -q -n JSON-%{version}
cp %{SOURCE1001} .

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
