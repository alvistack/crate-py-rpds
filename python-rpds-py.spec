# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-rpds-py
Epoch: 100
Version: 0.18.1
Release: 1%{?dist}
Summary: Python bindings to Rust's persistent data structures (rpds)
License: MIT
URL: https://github.com/crate-py/rpds/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: cargo
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-Cython3
BuildRequires: python3-devel
BuildRequires: python3-maturin >= 1.0.0
BuildRequires: python3-pip
BuildRequires: python3-setuptools
BuildRequires: rust >= 1.64.0

%description
Python bindings to the Rust rpds crate.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
maturin build --offline --sdist

%install
pip install \
    --no-deps \
    --ignore-installed \
    --root=%{buildroot} \
    --prefix=%{_prefix} \
    target/wheels/*.whl
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-rpds-py
Summary: Python bindings to Rust's persistent data structures (rpds)
Requires: python3
Provides: python3-rpds-py = %{epoch}:%{version}-%{release}
Provides: python3dist(rpds-py) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-rpds-py = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(rpds-py) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-rpds-py = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(rpds-py) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-rpds-py
Python bindings to the Rust rpds crate.

%files -n python%{python3_version_nodots}-rpds-py
%license LICENSE
%{python3_sitearch}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-rpds-py
Summary: Python bindings to Rust's persistent data structures (rpds)
Requires: python3
Provides: python3-rpds-py = %{epoch}:%{version}-%{release}
Provides: python3dist(rpds-py) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-rpds-py = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(rpds-py) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-rpds-py = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(rpds-py) = %{epoch}:%{version}-%{release}

%description -n python3-rpds-py
Python bindings to the Rust rpds crate.

%files -n python3-rpds-py
%license LICENSE
%{python3_sitearch}/*
%endif

%changelog
