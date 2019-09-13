%define pkgname 	RedHatFont

%define fontname 	redhat
%define	ttffontdir	%{_datadir}/fonts/TTF/%{fontname}
%define otffontdir	%{_datadir}/fonts/OTF/%{fontname}
%define fontconfdir	%{_sysconfdir}/X11/fontpath.d

Summary:	Red Hat's Open Source Fonts - Red Hat Display and Red Hat Text
Name:		fonts-ttf-redhat
Version:	2.3.2
Release:	1
License:	OFL
Group:		System/Fonts/True type
URL:		https://github.com/RedHatOfficial/RedHatFont/
Source0:	https://github.com/RedHatOfficial/RedHatFont/archive/%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	fontconfig
BuildRequires:	mkfontscale
BuildRequires:	mkfontdir

%description
Red Hat's Open Source Fonts - Red Hat Display and Red Hat Text

%package -n fonts-otf-redhat
Group:		System/Fonts/Open type
Summary:	Red Hat's Open Source Fonts - Red Hat Display and Red Hat Text

%description -n fonts-otf-redhat
Red Hat's Open Source Fonts - Red Hat Display and Red Hat Text

%prep
%setup -qn %{pkgname}-%{version}

%build


%install
mkdir -p %{buildroot}%{fontconfdir}/

# TTF fonts
install -dm 0755 %{buildroot}/%{ttffontdir}/
install -m 644 TTF/*.ttf %{buildroot}%{_xfontdir}/TTF/redhat
mkfontscale %{buildroot}%{ttffontdir}/
mkfontdir %{buildroot}%{ttffontdir}/
ln -s ../../..%{buildroot}%{ttffontdir} %{buildroot}%{fontconfdir}/ttf-%{fontname}:pri=50

# OTF fonts
install -dm 0755 %{buildroot}/%{otffontdir}/
install -m 644 OTF/*.otf %{buildroot}%{_xfontdir}/OTF/redhat
mkfontscale %{buildroot}%{otffontdir}/
mkfontdir %{buildroot}%{otffontdir}/
ln -s ../../..%{buildroot}%{otffontdir} %{buildroot}%{fontconfdir}/otf-%{fontname}:pri=50


%files
%dir %{ttffontdir}
%{fontconfdir}/ttf-%{fontname}:pri=50
%{ttffontdir}/*.ttf
%verify(not mtime)%{ttffontdir}/fonts.dir
%{ttffontdir}/fonts.scale
%license LICENSE

%files -n fonts-otf-redhat
%dir %{otffontdir}
%{fontconfdir}/otf-%{fontname}:pri=50
%{otffontdir}/*.otf
%verify(not mtime)%{otffontdir}/fonts.dir
%{otffontdir}/fonts.scale
%license LICENSE
