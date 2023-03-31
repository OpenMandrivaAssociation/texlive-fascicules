Name:		texlive-fascicules
Version:	54080
Release:	2
Summary:	Create mathematical manuals for schools
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fascicules
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fascicules.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fascicules.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fascicules.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package enables LaTeX users to create math books for
middle and high schools. It provides commands to create the
front page of the manual and the chapters. Each chapter can
consist of three sections: the lesson, the exercises and the
activities.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/fascicules
%{_texmfdistdir}/tex/latex/fascicules
%doc %{_texmfdistdir}/doc/latex/fascicules

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
