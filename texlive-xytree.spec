# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/xytree
# catalog-date 2007-03-13 09:23:19 +0100
# catalog-license lppl
# catalog-version 1.5
Name:		texlive-xytree
Version:	1.5
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The aim of xytree is to draw linguistic syntactic trees with
ease and to support hopefully sufficient functionalities, that
the linguist may need. The package (of course) depends on the
XY-Pic package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/xytree/xytree.sty
%doc %{_texmfdistdir}/doc/latex/xytree/README
%doc %{_texmfdistdir}/doc/latex/xytree/xytree-doc-en.pdf
%doc %{_texmfdistdir}/doc/latex/xytree/xytree-doc-en.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
