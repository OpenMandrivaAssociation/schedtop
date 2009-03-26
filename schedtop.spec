%define name	schedtop
%define version	1.0
%define release	%mkrel 2

Summary: 	Displays scheduler statistics
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL
Group: 		System/Kernel and hardware
URL: 		ftp://ftp.novell.com/dev/ghaskins/schedtop.tar.gz
Source0: 	%{name}-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	boost-devel ncurses-devel gcc-c++

%description
This utility will process statistics from /proc/schedstat such that the
busiest stats will bubble up to the top.  It can alternately be sorted by
the largest stat, or by name.  Stats can be included or excluded based on
reg-ex pattern matching.

Authors
--------------------------
  Gregory Haskins <ghaskins@novell.com>


%prep
%setup -q

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall PREFIX=$RPM_BUILD_ROOT/usr

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
