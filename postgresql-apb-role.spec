%if 0%{?copr}
%define build_timestamp .%(date +"%Y%m%d%H%M%%S")
%else
%define build_timestamp %{nil}
%endif

Name: 		postgresql-apb-role
Version:	1.0.3
Release:	1%{build_timestamp}%{?dist}
Summary:	Ansible Playbook for PostgreSQL APB

License:	ASL 2.0
URL:		https://github.com/ansibleplaybookbundle/RHSCL-PostgreSQL-APB
Source0:	https://github.com/ansibleplaybookbundle/RHSCL-PostgreSQL-APB/archive/%{name}-%{version}.tar.gz
BuildArch:  	noarch

%description
%{summary}

%prep
%setup -q -n %{name}-%{version}

%install
mkdir -p %{buildroot}/opt/apb/ %{buildroot}/opt/ansible/
mv playbooks %{buildroot}/opt/apb/actions
mv roles %{buildroot}/opt/ansible/roles

%files
%doc
/opt/apb/actions
/opt/ansible/roles

%changelog
* Tue Sep 19 2017 Jason Montleon <jmontleo@redhat.com> 1.0.3-1
- new package built with tito

* Mon Aug 21 2017 Jason Montleon <jmontleo@redhat.com> 1.0.2-1
- Fix rhscl-postgresql-apb deprovision (#116) (jmontleo@redhat.com)

* Fri Aug 18 2017 Jason Montleon <jmontleo@redhat.com> 1.0.1-1
- new package built with tito

