%global tl_name fascicules
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1
Release:	%{tl_revision}.1
Summary:	Create mathematical manuals for schools
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fascicules
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fascicules.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fascicules.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fascicules.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package enables LaTeX users to create math books for middle and
high schools. It provides commands to create the front page of the
manual and the chapters. Each chapter can consist of three sections: the
lesson, the exercises and the activities.

