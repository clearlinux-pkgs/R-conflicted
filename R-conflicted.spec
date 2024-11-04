#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-conflicted
Version  : 1.2.0
Release  : 15
URL      : https://cran.r-project.org/src/contrib/conflicted_1.2.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/conflicted_1.2.0.tar.gz
Summary  : An Alternative Conflict Resolution Strategy
Group    : Development/Tools
License  : MIT
Requires: R-cli
Requires: R-memoise
Requires: R-rlang
BuildRequires : R-cli
BuildRequires : R-dplyr
BuildRequires : R-memoise
BuildRequires : R-rlang
BuildRequires : buildreq-R

%description
recently loaded package precedence. This can make it hard to detect
    conflicts, particularly when they arise because a package update
    creates ambiguity that did not previously exist. 'conflicted' takes a
    different approach, making every conflict an error and forcing you to
    choose which function to use.

%prep
%setup -q -n conflicted
cd %{_builddir}/conflicted

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1678813546

%install
export SOURCE_DATE_EPOCH=1678813546
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/conflicted/DESCRIPTION
/usr/lib64/R/library/conflicted/INDEX
/usr/lib64/R/library/conflicted/LICENSE
/usr/lib64/R/library/conflicted/Meta/Rd.rds
/usr/lib64/R/library/conflicted/Meta/features.rds
/usr/lib64/R/library/conflicted/Meta/hsearch.rds
/usr/lib64/R/library/conflicted/Meta/links.rds
/usr/lib64/R/library/conflicted/Meta/nsInfo.rds
/usr/lib64/R/library/conflicted/Meta/package.rds
/usr/lib64/R/library/conflicted/NAMESPACE
/usr/lib64/R/library/conflicted/NEWS.md
/usr/lib64/R/library/conflicted/R/conflicted
/usr/lib64/R/library/conflicted/R/conflicted.rdb
/usr/lib64/R/library/conflicted/R/conflicted.rdx
/usr/lib64/R/library/conflicted/help/AnIndex
/usr/lib64/R/library/conflicted/help/aliases.rds
/usr/lib64/R/library/conflicted/help/conflicted.rdb
/usr/lib64/R/library/conflicted/help/conflicted.rdx
/usr/lib64/R/library/conflicted/help/paths.rds
/usr/lib64/R/library/conflicted/html/00Index.html
/usr/lib64/R/library/conflicted/html/R.css
/usr/lib64/R/library/conflicted/tests/testthat.R
/usr/lib64/R/library/conflicted/tests/testthat/_snaps/disambiguate.md
/usr/lib64/R/library/conflicted/tests/testthat/_snaps/favor.md
/usr/lib64/R/library/conflicted/tests/testthat/_snaps/find.md
/usr/lib64/R/library/conflicted/tests/testthat/_snaps/prefer.md
/usr/lib64/R/library/conflicted/tests/testthat/data/DESCRIPTION
/usr/lib64/R/library/conflicted/tests/testthat/data/NAMESPACE
/usr/lib64/R/library/conflicted/tests/testthat/data/data/mtcars.rda
/usr/lib64/R/library/conflicted/tests/testthat/funmatch/DESCRIPTION
/usr/lib64/R/library/conflicted/tests/testthat/funmatch/NAMESPACE
/usr/lib64/R/library/conflicted/tests/testthat/funmatch/R/test.R
/usr/lib64/R/library/conflicted/tests/testthat/primitive/DESCRIPTION
/usr/lib64/R/library/conflicted/tests/testthat/primitive/NAMESPACE
/usr/lib64/R/library/conflicted/tests/testthat/primitive/R/sum.R
/usr/lib64/R/library/conflicted/tests/testthat/test-disambiguate.R
/usr/lib64/R/library/conflicted/tests/testthat/test-favor.R
/usr/lib64/R/library/conflicted/tests/testthat/test-find.R
/usr/lib64/R/library/conflicted/tests/testthat/test-package.R
/usr/lib64/R/library/conflicted/tests/testthat/test-prefer.R
/usr/lib64/R/library/conflicted/tests/testthat/test-shim.R
/usr/lib64/R/library/conflicted/tests/testthat/test-zzz.R
