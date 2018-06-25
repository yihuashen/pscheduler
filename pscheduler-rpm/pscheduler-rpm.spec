#
# RPM Spec for pScheduler RPM Macros
#

Name:		pscheduler-rpm
Version:	1.1
Release:	0.1.b1%{?dist}

Summary:	Macros for use by pScheduler RPM specs
BuildArch:	noarch
License:	ASL 2.0
Vendor:	perfSONAR
Group:		Unspecified

Provides:	%{name} = %{version}-%{release}

%description
Macros for use by pScheduler RPM specs

# Where macros live
%define macro_dir %{_sysconfdir}/rpm
%define macro_prefix %{macro_dir}/macros.

# No punctuation between these is intentional.
%define macro_file %{macro_prefix}%{name}

%install
%{__mkdir_p} $RPM_BUILD_ROOT/%{macro_dir}
cat > $RPM_BUILD_ROOT/%{macro_prefix}%{name} <<EOF
#
# Macros used in building pScheduler RPMs  (Version %{version})
#

%if %{?_rundir:0}%{!?_rundir:1}
# This didn't appear until EL7
%%_rundir %{_localstatedir}/run
%endif

# Minimum-required PostgreSQL version
%%_pscheduler_postgresql_version_major 9
%%_pscheduler_postgresql_version_minor 5
%%_pscheduler_postgresql_version %{_pscheduler_postgresql_version_major}.%{_pscheduler_postgresql_version_minor}
%%_pscheduler_postgresql_package postgresql%{_pscheduler_postgresql_version_major}%{_pscheduler_postgresql_version_minor}


%%_pscheduler_libexecdir %{_libexecdir}/pscheduler
%%_pscheduler_sysconfdir %{_sysconfdir}/pscheduler
%%_pscheduler_sudoersdir %{_sysconfdir}/sudoers.d
%%_pscheduler_docdir %{_defaultdocdir}/pscheduler
%%_pscheduler_datadir %{_datadir}/pscheduler
%%_pscheduler_vardir %{_var}/lib/pscheduler

# Where RPM Macros live
%%_pscheduler_rpmmacrodir %{macro_dir}
# Prefix for all macro files.  Use as %{_pscheduler_rpmmacroprefix}foo
%%_pscheduler_rpmmacroprefix %{macro_prefix}

# Internal commands
%%_pscheduler_internals %{_pscheduler_libexecdir}/internals

# Where all classes live
%%_pscheduler_classes %{_pscheduler_libexecdir}/classes

# Tests
%%_pscheduler_test_libexec %{_pscheduler_classes}/test
%%_pscheduler_test_doc %{_pscheduler_docdir}/test
%%_pscheduler_test_confdir %{_pscheduler_sysconfdir}/test

# Tools
%%_pscheduler_tool_libexec %{_pscheduler_classes}/tool
%%_pscheduler_tool_doc %{_pscheduler_docdir}/tool
%%_pscheduler_tool_confdir %{_pscheduler_sysconfdir}/tool
%%_pscheduler_tool_vardir %{_pscheduler_vardir}/tool

# Archivers
%%_pscheduler_archiver_libexec %{_pscheduler_classes}/archiver
%%_pscheduler_archiver_doc %{_pscheduler_docdir}/archiver

# Context Changers
%%_pscheduler_context_libexec %{_pscheduler_classes}/context
%%_pscheduler_context_doc %{_pscheduler_docdir}/context

# pScheduler front-end comands
%%_pscheduler_commands %{_pscheduler_libexecdir}/commands

# pScheduler daemons
%%_pscheduler_daemons %{_pscheduler_libexecdir}/daemons

EOF


%files
%attr(444,root,root) %{macro_prefix}*
