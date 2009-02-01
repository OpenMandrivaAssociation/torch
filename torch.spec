%define name torch
%define version 3.1
%define release %mkrel 1
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



