Summary:	Plugins for Nagios to monitor remote disk and processes via SNMP
Name:		nagios-snmp-plugins
Version:	1.1
Release:	%mkrel 1
License:	GPL
Group:		Networking/Other
URL:		http://nagios.manubulon.com/
Source0:	http://nagios.manubulon.com/%{name}.%{version}.tgz
Source1:	ftp://ftp.hometree.net/pub/nagios-snmp-plugins/nagios-snmp-plugins-1.0.tar.gz
Source2:	check_snmp_disk.cfg
Source3:	check_snmp_proc.cfg
Source4:	check_snmp_boostedge.cfg
Source5:	check_snmp_cpfw.cfg
Source6:	check_snmp_css.cfg
Source7:	check_snmp_css_main.cfg
Source8:	check_snmp_env.cfg
Source9:	check_snmp_int.cfg
Source10:	check_snmp_linkproof_nhr.cfg
Source11:	check_snmp_load.cfg
Source12:	check_snmp_mem.cfg
Source13:	check_snmp_nsbox.cfg
Source14:	check_snmp_process.cfg
Source15:	check_snmp_storage.cfg
Source16:	check_snmp_vrrp.cfg
Source17:	check_snmp_win.cfg
Patch0:		nagios-snmp-plugins-1.0-gcc4.diff
Patch1:		nagios-snmp-plugins-format-report.patch
Requires:	nagios
BuildRequires:	net-snmp-devel
BuildRequires:	autoconf2.5
BuildRequires:	automake1.7
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
These plugins allow you to monitor disk space and running processes on a remote
machine via SNMP.

%prep

%setup -q -n nagios_plugins -a1

pushd nagios-snmp-plugins-1.0
%patch0 -p0
%patch1 -p1
popd

cp %{SOURCE2} check_snmp_disk.cfg
cp %{SOURCE3} check_snmp_proc.cfg
cp %{SOURCE4} check_snmp_boostedge.cfg
cp %{SOURCE5} check_snmp_cpfw.cfg
cp %{SOURCE6} check_snmp_css.cfg
cp %{SOURCE7} check_snmp_css_main.cfg
cp %{SOURCE8} check_snmp_env.cfg
cp %{SOURCE9} check_snmp_int.cfg
cp %{SOURCE10} check_snmp_linkproof_nhr.cfg
cp %{SOURCE11} check_snmp_load.cfg
cp %{SOURCE12} check_snmp_mem.cfg
cp %{SOURCE13} check_snmp_nsbox.cfg
cp %{SOURCE14} check_snmp_process.cfg
cp %{SOURCE15} check_snmp_storage.cfg
cp %{SOURCE16} check_snmp_vrrp.cfg
cp %{SOURCE17} check_snmp_win.cfg

# fix strange perms
find . -type d -exec chmod 755 {} \;
find . -type f -exec chmod 644 {} \;

# strip away annoying ^M
find . -type f|xargs file|grep 'CRLF'|cut -d: -f1|xargs perl -p -i -e 's/\r//'
find . -type f|xargs file|grep 'text'|cut -d: -f1|xargs perl -p -i -e 's/\r//'

perl -pi -e "s|^use lib \"/usr/local/nagios/libexec\"|use lib \"%{_libdir}/nagios/plugins\"|g" *.pl
perl -pi -e "s|_LIBDIR_|%{_libdir}|g" *.cfg

%build

pushd nagios-snmp-plugins-1.0
export WANT_AUTOCONF_2_5="1"
libtoolize --copy --force; aclocal-1.7; autoheader; automake-1.7 --copy --add-missing; autoconf

%configure2_5x

%make
popd

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_sysconfdir}/nagios/plugins.d
install -d %{buildroot}%{_libdir}/nagios/plugins

pushd nagios-snmp-plugins-1.0
install -m0755 check_snmp_disk %{buildroot}%{_libdir}/nagios/plugins/
install -m0755 check_snmp_proc %{buildroot}%{_libdir}/nagios/plugins/
popd

cp nagios-snmp-plugins-1.0/README README.nagios-snmp-plugins-1.0
cp nagios-snmp-plugins-1.0/AUTHORS AUTHORS.nagios-snmp-plugins-1.0
cp nagios-snmp-plugins-1.0/NEWS NEWS.nagios-snmp-plugins-1.0

install -m0755 *.pl %{buildroot}%{_libdir}/nagios/plugins/
install -m0644 *.cfg %{buildroot}%{_sysconfdir}/nagios/plugins.d/

%post
/sbin/service nagios condrestart > /dev/null 2>/dev/null || :

%postun
/sbin/service nagios condrestart > /dev/null 2>/dev/null || :

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changelog LICENSE README
%doc README.nagios-snmp-plugins-1.0
%doc AUTHORS.nagios-snmp-plugins-1.0
%doc NEWS.nagios-snmp-plugins-1.0
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_snmp_disk.cfg
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_snmp_proc.cfg
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_snmp_boostedge.cfg
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_snmp_cpfw.cfg
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_snmp_css.cfg
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_snmp_css_main.cfg
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_snmp_env.cfg
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_snmp_int.cfg
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_snmp_linkproof_nhr.cfg
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_snmp_load.cfg
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_snmp_mem.cfg
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_snmp_nsbox.cfg
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_snmp_process.cfg
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_snmp_storage.cfg
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_snmp_vrrp.cfg
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_snmp_win.cfg
%attr(0755,root,root) %{_libdir}/nagios/plugins/check_snmp_disk
%attr(0755,root,root) %{_libdir}/nagios/plugins/check_snmp_proc
%attr(0755,root,root) %{_libdir}/nagios/plugins/check_snmp_boostedge.pl
%attr(0755,root,root) %{_libdir}/nagios/plugins/check_snmp_cpfw.pl
%attr(0755,root,root) %{_libdir}/nagios/plugins/check_snmp_css_main.pl
%attr(0755,root,root) %{_libdir}/nagios/plugins/check_snmp_css.pl
%attr(0755,root,root) %{_libdir}/nagios/plugins/check_snmp_env.pl
%attr(0755,root,root) %{_libdir}/nagios/plugins/check_snmp_int.pl
%attr(0755,root,root) %{_libdir}/nagios/plugins/check_snmp_linkproof_nhr.pl
%attr(0755,root,root) %{_libdir}/nagios/plugins/check_snmp_load.pl
%attr(0755,root,root) %{_libdir}/nagios/plugins/check_snmp_mem.pl
%attr(0755,root,root) %{_libdir}/nagios/plugins/check_snmp_nsbox.pl
%attr(0755,root,root) %{_libdir}/nagios/plugins/check_snmp_process.pl
%attr(0755,root,root) %{_libdir}/nagios/plugins/check_snmp_storage.pl
%attr(0755,root,root) %{_libdir}/nagios/plugins/check_snmp_win.pl
%attr(0755,root,root) %{_libdir}/nagios/plugins/check_snmp_vrrp.pl
