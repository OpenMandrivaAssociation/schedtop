%define name	schedtop
%define version	0.5
%define release	%mkrel 1

Summary: 	Displays scheduler statistics
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL
Group: 		System/Kernel and hardware
URL: 		ftp://ftp.novell.com/dev/ghaskins/schedtop.tar.gz
Source0: 	%{name}-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root

%description

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
