%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		yelp-tools
Version:	3.32.2
Release:	2
Summary:	Create, manage, and publish documentation for Yelp
Group:		System/Internationalization
License:	GPLv2+
URL:		http://projects.gnome.org/yelp/
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	itstool
BuildRequires:	libxml2-utils
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(yelp-xsl)
Requires:	itstool
Requires:	libxml2-utils
Requires:	yelp-xsl

%description
yelp-tools is a collection of scripts and build utilities to help create,
manage, and publish documentation for Yelp and the web. Most of the heavy
lifting is done by packages like yelp-xsl and itstool. This package just
wraps things up in a developer-friendly way.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%doc AUTHORS README
%{_bindir}/yelp-build
%{_bindir}/yelp-check
%{_bindir}/yelp-new
%{_datadir}/yelp-tools
%{_datadir}/aclocal/yelp.m4
