%define name torch
%define version 3.1
%define release %mkrel 3
%define oname Torch
%define oversion 3

Summary: State of the art machine learning library
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.torch.ch/archives/%{oname}%{oversion}src.tar.bz2
License: BSD
Group: System/Libraries
Url: http://www.torch.ch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Torch is a machine-learning library, written in C++. Its aim is to
provide the state-of-the-art of the best algorithms. It is, and it
will be, in development forever.

Main features:

* Many gradient-based methods, including multi-layered perceptrons,
  radial basis functions, and mixtures of experts. Many small
  "modules" (Linear module, Tanh module, SoftMax module, ...) can be
  plugged together.

* Support Vector Machine, for classification and regression.

* Distribution package, includes Kmeans, Gaussian Mixture Models,
  Hidden Markov Models, and Bayes Classifier, and classes for speech
  recognition with embedded training.

* Ensemble models such as Bagging and Adaboost.

* Non-parametric models such as K-nearest-neighbors, Parzen Regression
  and Parzen Density Estimator.

%package devel
Group: Development/C++
Summary: State of the art machine learning library

%description devel
Torch is a machine-learning library, written in C++. Its aim is to
provide the state-of-the-art of the best algorithms. It is, and it
will be, in development forever.

Main features:

* Many gradient-based methods, including multi-layered perceptrons,
  radial basis functions, and mixtures of experts. Many small
  "modules" (Linear module, Tanh module, SoftMax module, ...) can be
  plugged together.

* Support Vector Machine, for classification and regression.

* Distribution package, includes Kmeans, Gaussian Mixture Models,
  Hidden Markov Models, and Bayes Classifier, and classes for speech
  recognition with embedded training.

* Ensemble models such as Bagging and Adaboost.

* Non-parametric models such as K-nearest-neighbors, Parzen Regression
  and Parzen Density Estimator.

This package contains the static library and headers of Torch compiled
with single precision support.

%prep
%setup -q -n %oname%oversion
cp config/Makefile_options_Linux .

%build
%ifarch %ix86
export RPM_OPT_FLAGS="%optflags -malign-double"
%endif
make depend all CFLAGS_OPT_FLOAT="$RPM_OPT_FLAGS -ffast-math" LD="g++ -fPIC" PACKAGES="distributions gradients"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot%_includedir/%name
install */*.h %buildroot%_includedir/%name
install -m 644 -D lib/*/libtorch.a %buildroot%_libdir/libtorch.a

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(-,root,root)
%doc LICENSE ChangeLog
%_includedir/%name
%_libdir/libtorch.a





%changelog
* Thu Sep 22 2011 Götz Waschk <waschk@mandriva.org> 3.1-3mdv2012.0
+ Revision: 700804
- rebuild

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 3.1-2mdv2011.0
+ Revision: 445516
- rebuild

* Sun Feb 01 2009 Götz Waschk <waschk@mandriva.org> 3.1-1mdv2009.1
+ Revision: 336064
- set version number to 3.1

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 3-6mdv2009.0
+ Revision: 261623
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 3-5mdv2009.0
+ Revision: 254682
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 3mdv2008.1-current
+ Revision: 136550
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Feb 27 2007 Götz Waschk <waschk@mandriva.org> 3-3mdv2007.0
+ Revision: 126339
- enable packages required by imms

* Tue Feb 27 2007 Götz Waschk <waschk@mandriva.org> 3-2mdv2007.1
+ Revision: 126239
- release bump dedicated to blino
- Import torch

