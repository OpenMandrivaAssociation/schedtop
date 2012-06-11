%define	gitrev	68dee64

Summary: 	Displays scheduler statistics
Name: 		schedtop
Version: 	1.1
Release: 	0.%{gitrev}.1
License: 	GPLv2
Group: 		System/Kernel and hardware
URL: 		https://github.com/ghaskins/schedtop
Source0: 	%{name}-%{gitrev}.tar.xz
Patch0:		schedtop_linking.patch

BuildRequires:	boost-devel
BuildRequires:	ncurses-devel

%description
This utility will process statistics from /proc/schedstat such that the
busiest stats will bubble up to the top.  It can alternately be sorted by
the largest stat, or by name.  Stats can be included or excluded based on
reg-ex pattern matching.

%prep
%setup -qn %{name}
%apply_patches

%build
%setup_compile_flags
%make CFLAGS='%optflags -DBOOST_FILESYSTEM_VERSION=2 %ldflags' 

%install
%makeinstall_std PREFIX=%{buildroot}


%files
%{_bindir}/%{name}
