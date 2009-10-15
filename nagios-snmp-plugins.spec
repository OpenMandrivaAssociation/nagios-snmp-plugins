Summary:	Plugins for Nagios to monitor remote disk and processes via SNMP
Name:		nagios-snmp-plugins
Version:	1.1.1
Release:	%mkrel 5
License:	GPL
Group:		Networking/Other
URL:		http://nagios.manubulon.com/
Source0:	http://nagios.manubulon.com/%{name}.%{version}.tgz
Source1:	ftp://ftp.hometree.net/pub/nagios-snmp-plugins/nagios-snmp-plugins-1.2.tar.gz
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
BuildRequires:	openssl-devel
BuildRequires:	autoconf2.5
BuildRequires:	automake1.7
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
These plugins allow you to monitor disk space, processes and a lot of other 
stuff on a remote machine via SNMP.

%package -n	nagios-check_snmp_disk
Summary:	The check_snmp_disk plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-snmp-plugins < 1.1

%description -n	nagios-check_snmp_disk
Checks the disks for a given host via snmp and the ucd snmp interface.

%package -n	nagios-check_snmp_proc
Summary:	The check_snmp_proc plugin for nagios
Group:		Networking/Other
Conflicts:	nagios-snmp-plugins < 1.1

%description -n	nagios-check_snmp_proc
Checks the running processes for a given host via snmp and the ucd snmp
interface.

%package -n	nagios-check_snmp_boostedge
Summary:	The check_snmp_boostedge plugin for nagios
Group:		Networking/Other
Requires:	net-snmp-utils
Conflicts:	nagios-snmp-plugins < 1.1

%description -n	nagios-check_snmp_boostedge
SNMP Boostedge service monitor for Nagios.

%package -n	nagios-check_snmp_cpfw
Summary:	The check_snmp_cpfw plugin for nagios
Group:		Networking/Other
Requires:	net-snmp-utils
Conflicts:	nagios-snmp-plugins < 1.1

%description -n	nagios-check_snmp_cpfw
SNMP Checkpoint FW-1 Monitor for Nagios.

%package -n	nagios-check_snmp_css_main
Summary:	The check_snmp_css_main plugin for nagios
Group:		Networking/Other
Requires:	net-snmp-utils
Conflicts:	nagios-snmp-plugins < 1.1

%description -n	nagios-check_snmp_css_main
SNMP Cisco CSS monitor MAIN script for Nagios.

%package -n	nagios-check_snmp_css
Summary:	The check_snmp_css plugin for nagios
Group:		Networking/Other
Requires:	net-snmp-utils
Conflicts:	nagios-snmp-plugins < 1.1

%description -n	nagios-check_snmp_css
SNMP Cisco CSS monitor for Nagios.


%package -n	nagios-check_snmp_env
Summary:	The check_snmp_env plugin for nagios
Group:		Networking/Other
Requires:	net-snmp-utils
Conflicts:	nagios-snmp-plugins < 1.1

%description -n	nagios-check_snmp_env
SNMP environmental Monitor for Nagios.

%package -n	nagios-check_snmp_int
Summary:	The check_snmp_int plugin for nagios
Group:		Networking/Other
Requires:	net-snmp-utils
Conflicts:	nagios-snmp-plugins < 1.1

%description -n	nagios-check_snmp_int
SNMP Network Interface Monitor for Nagios.

%package -n	nagios-check_snmp_linkproof_nhr
Summary:	The check_snmp_linkproof_nhr plugin for nagios
Group:		Networking/Other
Requires:	net-snmp-utils
Conflicts:	nagios-snmp-plugins < 1.1

%description -n	nagios-check_snmp_linkproof_nhr
SNMP Radware Linkproof NHR monitor for Nagios.

%package -n	nagios-check_snmp_load
Summary:	The check_snmp_load plugin for nagios
Group:		Networking/Other
Requires:	net-snmp-utils
Conflicts:	nagios-snmp-plugins < 1.1

%description -n	nagios-check_snmp_load
SNMP Load & CPU Monitor for Nagios.

%package -n	nagios-check_snmp_mem
Summary:	The check_snmp_mem plugin for nagios
Group:		Networking/Other
Requires:	net-snmp-utils
Conflicts:	nagios-snmp-plugins < 1.1

%description -n	nagios-check_snmp_mem
SNMP Memory Monitor for Nagios.

%package -n	nagios-check_snmp_nsbox
Summary:	The check_snmp_nsbox plugin for nagios
Group:		Networking/Other
Requires:	net-snmp-utils
Conflicts:	nagios-snmp-plugins < 1.1

%description -n	nagios-check_snmp_nsbox
SNMP NetSecureOne Netbox monitor for Nagios.

%package -n	nagios-check_snmp_process
Summary:	The check_snmp_process plugin for nagios
Group:		Networking/Other
Requires:	net-snmp-utils
Conflicts:	nagios-snmp-plugins < 1.1

%description -n	nagios-check_snmp_process
SNMP Process Monitor for Nagios.

%package -n	nagios-check_snmp_storage
Summary:	The check_snmp_storage plugin for nagios
Group:		Networking/Other
Requires:	net-snmp-utils
Conflicts:	nagios-snmp-plugins < 1.1

%description -n	nagios-check_snmp_storage
SNMP Disk Monitor for Nagios.

%package -n	nagios-check_snmp_win
Summary:	The check_snmp_win plugin for nagios
Group:		Networking/Other
Requires:	net-snmp-utils
Conflicts:	nagios-snmp-plugins < 1.1

%description -n	nagios-check_snmp_win
SNMP Windows Monitor for Nagios.

%package -n	nagios-check_snmp_vrrp
Summary:	The check_snmp_vrrp plugin for nagios
Group:		Networking/Other
Requires:	net-snmp-utils
Conflicts:	nagios-snmp-plugins < 1.1

%description -n	nagios-check_snmp_vrrp
SNMP VRRP Monitor for Nagios.

%prep

%setup -q -n nagios_plugins -a1

mkdir plugins.d
# magic by anssi
pushd plugins.d; %{expand:%(for i in {2..17}; do echo "cp %%SOURCE$i ."; done)}; popd

# fix strange perms
find . -type d -exec chmod 755 {} \;
find . -type f -exec chmod 644 {} \;

# strip away annoying ^M
find . -type f|xargs file|grep 'CRLF'|cut -d: -f1|xargs perl -p -i -e 's/\r//'
find . -type f|xargs file|grep 'text'|cut -d: -f1|xargs perl -p -i -e 's/\r//'

perl -pi -e "s|^use lib \"/usr/local/nagios/libexec\"|use lib \"%{_libdir}/nagios/plugins\"|g" *.pl

%build

pushd nagios-snmp-plugins-1.2
#export WANT_AUTOCONF_2_5="1"
#libtoolize --copy --force; aclocal-1.7; autoheader; automake-1.7 --copy --add-missing; autoconf

sh ./build.sh

%configure2_5x

%make
popd

perl -pi -e "s|\@libexecdir\@|%{_libdir}/nagios/plugins|g" plugins.d/*.cfg

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_sysconfdir}/nagios/plugins.d
install -d %{buildroot}%{_libdir}/nagios/plugins

pushd nagios-snmp-plugins-1.2
    install -m0755 check_snmp_disk %{buildroot}%{_libdir}/nagios/plugins/
    install -m0755 check_snmp_proc %{buildroot}%{_libdir}/nagios/plugins/
popd

cp nagios-snmp-plugins-1.2/README README.nagios-snmp-plugins-1.2
cp nagios-snmp-plugins-1.2/AUTHORS AUTHORS.nagios-snmp-plugins-1.2
cp nagios-snmp-plugins-1.2/NEWS NEWS.nagios-snmp-plugins-1.2

# binaries
install -m0644 plugins.d/check_snmp_disk.cfg %{buildroot}%{_sysconfdir}/nagios/plugins.d/check_snmp_disk.cfg
install -m0644 plugins.d/check_snmp_proc.cfg %{buildroot}%{_sysconfdir}/nagios/plugins.d/check_snmp_proc.cfg

# scripts
install -m0755 *.pl %{buildroot}%{_libdir}/nagios/plugins/

# config
install -m0644 plugins.d/check_snmp_boostedge.cfg %{buildroot}%{_sysconfdir}/nagios/plugins.d/check_snmp_boostedge.cfg
install -m0644 plugins.d/check_snmp_cpfw.cfg %{buildroot}%{_sysconfdir}/nagios/plugins.d/check_snmp_cpfw.cfg
install -m0644 plugins.d/check_snmp_css_main.cfg %{buildroot}%{_sysconfdir}/nagios/plugins.d/check_snmp_css_main.cfg
install -m0644 plugins.d/check_snmp_css.cfg %{buildroot}%{_sysconfdir}/nagios/plugins.d/check_snmp_css.cfg
install -m0644 plugins.d/check_snmp_env.cfg %{buildroot}%{_sysconfdir}/nagios/plugins.d/check_snmp_env.cfg
install -m0644 plugins.d/check_snmp_int.cfg %{buildroot}%{_sysconfdir}/nagios/plugins.d/check_snmp_int.cfg
install -m0644 plugins.d/check_snmp_linkproof_nhr.cfg %{buildroot}%{_sysconfdir}/nagios/plugins.d/check_snmp_linkproof_nhr.cfg
install -m0644 plugins.d/check_snmp_load.cfg %{buildroot}%{_sysconfdir}/nagios/plugins.d/check_snmp_load.cfg
install -m0644 plugins.d/check_snmp_mem.cfg %{buildroot}%{_sysconfdir}/nagios/plugins.d/check_snmp_mem.cfg
install -m0644 plugins.d/check_snmp_nsbox.cfg %{buildroot}%{_sysconfdir}/nagios/plugins.d/check_snmp_nsbox.cfg
install -m0644 plugins.d/check_snmp_process.cfg %{buildroot}%{_sysconfdir}/nagios/plugins.d/check_snmp_process.cfg
install -m0644 plugins.d/check_snmp_storage.cfg %{buildroot}%{_sysconfdir}/nagios/plugins.d/check_snmp_storage.cfg
install -m0644 plugins.d/check_snmp_win.cfg %{buildroot}%{_sysconfdir}/nagios/plugins.d/check_snmp_win.cfg
install -m0644 plugins.d/check_snmp_vrrp.cfg %{buildroot}%{_sysconfdir}/nagios/plugins.d/check_snmp_vrrp.cfg

%post -n nagios-check_snmp_disk
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_snmp_disk
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_snmp_proc
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_snmp_proc
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_snmp_boostedge
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_snmp_boostedge
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_snmp_cpfw
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_snmp_cpfw
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_snmp_css_main
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_snmp_css_main
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_snmp_css
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_snmp_css
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_snmp_env
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_snmp_env
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_snmp_int
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_snmp_int
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_snmp_linkproof_nhr
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_snmp_linkproof_nhr
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_snmp_load
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_snmp_load
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_snmp_mem
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_snmp_mem
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_snmp_nsbox
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_snmp_nsbox
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_snmp_process
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_snmp_process
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_snmp_storage
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_snmp_storage
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_snmp_win
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_snmp_win
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%post -n nagios-check_snmp_vrrp
%{_initrddir}/nagios condrestart > /dev/null 2>&1 || :

%postun -n nagios-check_snmp_vrrp
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart > /dev/null 2>&1 || :
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changelog LICENSE README* AUTHORS* NEWS* doc/*

%files -n nagios-check_snmp_disk
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_snmp_disk.cfg
%{_libdir}/nagios/plugins/check_snmp_disk

%files -n nagios-check_snmp_proc
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_snmp_proc.cfg
%{_libdir}/nagios/plugins/check_snmp_proc

%files -n nagios-check_snmp_boostedge
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_snmp_boostedge.cfg
%{_libdir}/nagios/plugins/check_snmp_boostedge.pl

%files -n nagios-check_snmp_cpfw
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_snmp_cpfw.cfg
%{_libdir}/nagios/plugins/check_snmp_cpfw.pl

%files -n nagios-check_snmp_css_main
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_snmp_css_main.cfg
%{_libdir}/nagios/plugins/check_snmp_css_main.pl

%files -n nagios-check_snmp_css
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_snmp_css.cfg
%{_libdir}/nagios/plugins/check_snmp_css.pl

%files -n nagios-check_snmp_env
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_snmp_env.cfg
%{_libdir}/nagios/plugins/check_snmp_env.pl

%files -n nagios-check_snmp_int
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_snmp_int.cfg
%{_libdir}/nagios/plugins/check_snmp_int.pl

%files -n nagios-check_snmp_linkproof_nhr
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_snmp_linkproof_nhr.cfg
%{_libdir}/nagios/plugins/check_snmp_linkproof_nhr.pl

%files -n nagios-check_snmp_load
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_snmp_load.cfg
%{_libdir}/nagios/plugins/check_snmp_load.pl

%files -n nagios-check_snmp_mem
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_snmp_mem.cfg
%{_libdir}/nagios/plugins/check_snmp_mem.pl

%files -n nagios-check_snmp_nsbox
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_snmp_nsbox.cfg
%{_libdir}/nagios/plugins/check_snmp_nsbox.pl


%files -n nagios-check_snmp_process
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_snmp_process.cfg
%{_libdir}/nagios/plugins/check_snmp_process.pl

%files -n nagios-check_snmp_storage
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_snmp_storage.cfg
%{_libdir}/nagios/plugins/check_snmp_storage.pl

%files -n nagios-check_snmp_win
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_snmp_win.cfg
%{_libdir}/nagios/plugins/check_snmp_win.pl

%files -n nagios-check_snmp_vrrp
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/plugins.d/check_snmp_vrrp.cfg
%{_libdir}/nagios/plugins/check_snmp_vrrp.pl
