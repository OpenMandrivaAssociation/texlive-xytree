# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/xytree
# catalog-date 2007-03-13 09:23:19 +0100
# catalog-license lppl
# catalog-version 1.5
Name:		texlive-xytree
Version:	1.5
Release:	6
Summary:	Tree macros using XY-Pic
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xytree
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xytree.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xytree.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.5-2
+ Revision: 757737
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.5-1
+ Revision: 719958
- texlive-xytree
- texlive-xytree
- texlive-xytree

