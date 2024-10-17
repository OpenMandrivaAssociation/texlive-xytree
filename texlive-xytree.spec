Name:		texlive-xytree
Version:	15878
Release:	2
Summary:	Tree macros using XY-Pic
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xytree
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xytree.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xytree.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The aim of xytree is to draw linguistic syntactic trees with
ease and to support hopefully sufficient functionalities, that
the linguist may need. The package (of course) depends on the
XY-Pic package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/xytree/xytree.sty
%doc %{_texmfdistdir}/doc/latex/xytree/README
%doc %{_texmfdistdir}/doc/latex/xytree/xytree-doc-en.pdf
%doc %{_texmfdistdir}/doc/latex/xytree/xytree-doc-en.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
