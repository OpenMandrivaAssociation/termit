Summary:	Simple terminal emulator based on vte library
Name:		termit
Version:	2.9.3
Release:	1
Group:		Terminals
License:	GPLv2
URL:		http://wiki.github.com/nonstop/termit/
Source0:	http://cloud.github.com/downloads/nonstop/%{name}/%{name}-%{version}.tar.xz

BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(vte)

%description
TermIt is a simple terminal emulator based on vte library with a lot of 
features:
 * tabs
 * bookmarks
 * sessions
 * changing tab name
 * changing font for tabs
 * encodings (all available from GTK2)
 * integrated lua interpreter
Configuration can be changed via $HOME/.config/termit/termit.cfg file.

%prep
%setup -q
# fix paths in the README
sed -i 's!doc/!%{_docdir}/%{name}-%{version}!' ./doc/README
# add a generic icon to the desktop file
echo Icon=terminal >> ./doc/termit.desktop

%build
find . -type f -name CMakeCache.txt -exec rm -rf {} \;
%cmake
%make

%install
%makeinstall_std -C build

desktop-file-install \
	--delete-original \
	--remove-category=Utility \
	--add-category=System \
	--dir=%{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}
# we install the docfiles versioned
rm -rf %{buildroot}%{_datadir}/doc/termit/

%files -f %{name}.lang
%doc ChangeLog COPYING TODO
%doc doc/README doc/rc.lua.example doc/lua_api.txt doc/termit.svg
%{_bindir}/%{name}
%{_sysconfdir}/xdg/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1.*

