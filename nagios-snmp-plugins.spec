Summary:	Plugins for Nagios to monitor remote disk and processes via SNMP
Name:		nagios-snmp-plugins
Version:	1.0
Release:	%mkrel 3
License:	GPL
Group:		Networking/Other
URL:		ftp://ftp.hometree.net:/pub/nagios-snmp-plugins/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		nagios-snmp-plugins-1.0-gcc4.diff
BuildRequires:	net-snmp-devel
BuildRequires:	autoconf2.5
BuildRequires:	automake1.7
Provides:	netsaint-plugins
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
These plugins allow you to monitor disk space and running processes on
a remote machine via SNMP.

%prep

%setup -q
%patch0 -p0

%build
export WANT_AUTOCONF_2_5="1"
libtoolize --copy --force; aclocal-1.7; autoheader; automake-1.7 --copy --add-missing; autoconf

%configure2_5x

%make

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

install -d %{buildroot}%{_libdir}/nagios/plugins
install -m0755 check_snmp_disk %{buildroot}%{_libdir}/nagios/plugins/
install -m0755 check_snmp_proc %{buildroot}%{_libdir}/nagios/plugins/

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README AUTHORS NEWS
%attr(0755,root,root) %{_libdir}/nagios/plugins/check_snmp_disk
%attr(0755,root,root) %{_libdir}/nagios/plugins/check_snmp_proc

