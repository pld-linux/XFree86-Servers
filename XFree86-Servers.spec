Summary:	XFree86 servers
Name:		XFree86-Servers
Version:	3.3.6
Release:	36
License:	MIT
Group:		X11/Servers
Source0:	ftp://ftp.xfree86.org/pub/XFree86/3.3.6/source/X336src-1.tgz
# Source0-md5:	bbfa360d10ce91ab37f24f197a31b485
Source1:	ftp://ftp.dcs.ed.ac.uk/pub/jec/programs/xfsft/xfsft-1.1.6.tar.gz
# Source1-md5:	88c65d3c314dab6b000499861a7f4865
Source2:	xserver.pamd
Patch0:		%{name}-rh.patch
Patch1:		%{name}-parallelmake.patch
Patch2:		%{name}-fix-01-r128.patch
Patch3:		%{name}-joy.patch
Patch4:		%{name}-ssa50.patch
Patch5:		%{name}-cyrix.patch
Patch6:		%{name}-sis.patch
Patch7:		%{name}-3dfxalpha.patch
Patch8:		%{name}-sparc.patch.gz
# Patch8-md5:	447f47d07a629771a075939e198d0597
Patch9:		%{name}-new-i810.patch
Patch10:	%{name}-5480mem.patch
Patch11:	%{name}-ragemobility.patch
Patch12:	%{name}-fixreleasedate.patch
Patch13:	%{name}-svgaprobe.patch
Patch14:	%{name}-morecyrix.patch
Patch15:	%{name}-security.patch
Patch16:	%{name}-xkbstack.patch
Patch17:	%{name}-fix-04-s3trio3d2x.patch
Patch18:	%{name}-fix-05-s3trio3d.patch
Patch19:	%{name}-fbdev-compile.patch
Patch20:	%{name}-alpha.patch
Patch21:	%{name}-serversonly.patch
Patch22:	%{name}-sparc-asmflags.patch
Patch23:	%{name}-HasZlib.patch
Patch24:	%{name}-period.patch
ExclusiveArch:	%{ix86} alpha m68k armv4l sparc
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	pam-devel
BuildRequires:	zlib-devel
Requires:	pam >= 0.77.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		docsrc		xc/programs/Xserver/hw/xfree86/doc

%description
This package contains old XFree86 servers (taken from version 3.3.6)
to use with old video cards, not supported by XFree86 4.x.

%description -l pl.UTF-8
Ten pakiet zawiera stare serwery XFree86 (wzięte z wersji 3.3.6) dla
starych kart graficznych, nie obsługiwanych przez XFree86 4.x.

%package common
Summary:	The XFree86 servers - common files
Summary(pl.UTF-8):	Pliki wspólne dla serwerów XFree86
Group:		X11/Servers
Requires:	XFree86-fonts
Obsoletes:	XFree86-Xserver

%description common
Files common for all XFree86 servers, i.e. modules, Xwrapper and PAM
configuration files. Install this package with appropriate X server
package if you have old video card which was supported by XFree 3.3.6
but is not supported by XFree 4.x. If your card is well supported by
XFree 4.x, use Xserver with appropriate driver from XFree 4.x instead.

Please see the XFree86 video card/server list available from the
XFree86 Project's website at http://www.xfree86.org/ for a definitive
list of X servers and which video cards they support.

%description common -l pl.UTF-8
Pliki wspólne dla wszystkich X serwerów, w tym moduły, Xwrapper oraz
pliki konfiguracyjne PAM. Zainstaluj ten pakiet wraz z pakietem
zawierającym odpowiedni X serwer jeżeli masz starą kartę, która była
obsługiwana przez XFree 3.3.6, a nie jest obsługiwana przez XFree 4.x.
Jeżeli twoja karta jest dobrze obsługiwana przez XFree 4.x, lepiej
użyj X serwera wraz z odpowiednim driverem z XFree 4.x

Pełną listę X serwerów oraz kart które obsługują można znaleźć pod
adresem http://www.xfree86.org/.

%package -n XFree86-S3
Summary:	The XFree86 server for video cards based on older S3 chips
Summary(pl.UTF-8):	Serwer XFree86 dla kart na starych układach S3
Group:		X11/Servers
Provides:	Xserver
Requires:	%{name}-common = %{version}

%description -n XFree86-S3
XFree86-S3 is the X server for video cards based on S3 chips,
including most Number Nine cards, many Diamond Stealth cards, Orchid
Fahrenheits, the Miro Crystal 8S, most STB cards, and some
motherboards with built-in graphics accelerators (such as the IBM
ValuePoint line). Note that if you have an S3 ViRGE based video card,
you'll need XFree86-S3V instead of XFree86-S3.

%description -n XFree86-S3 -l pl.UTF-8
XFree86-S3 jest X serwerem dla kart graficznych na układach S3, czyli
części kart Number Nine, Diamond Stealth, Orchid Fahrenheit, Miro
Crystal, STB. Jeżeli masz kartę na układzie S3 ViRGE, zamiast tego
pakietu zainstaluj XFree86-S3V.

%package -n XFree86-I128
Summary:	The XFree86 server for Number Nine Imagine 128 video cards
Summary(pl.UTF-8):	Serwer XFree86 dla kart Number Nine Imagine 128
Group:		X11/Servers
Provides:	Xserver
Requires:	%{name}-common = %{version}

%description -n XFree86-I128
XFree86-I128 is the X server for the Number Nine Imagine 128 and
similar video cards.

%description -n XFree86-I128 -l pl.UTF-8
XFree86-I128 jest X serwerem dla kart graficznych Number Nine Imagine
128 i podobnych.

%package -n XFree86-S3V
Summary:	The XFree86 server for video cards based on the S3 Virge chip
Summary(pl.UTF-8):	Serwer XFree86 dla kart na układzie S3 Virge
Group:		X11/Servers
Provides:	Xserver
Requires:	%{name}-common = %{version}

%description -n XFree86-S3V
XFree86-S3V is the X server for video cards based on the S3 ViRGE
chipset.

%description -n XFree86-S3V -l pl.UTF-8
XFree86-S3V jest X serwerem dla kart graficznych opartych o układy S3
ViRGE.

%package -n XFree86-Mach64
Summary:	The XFree86 server for Mach64 based video cards
Summary(pl.UTF-8):	Serwer XFree86 dla kart na układzie Mach64
Group:		X11/Servers
Provides:	Xserver
Requires:	%{name}-common = %{version}

%description -n XFree86-Mach64
XFree86-Mach64 is the server package for cards based on ATI's Mach64
chip, such as the Graphics Xpression, GUP Turbo, and WinTurbo cards.
Note that this server is known to have problems with some Mach64
cards. Check http://www.xfree86.org/ for current information on
updating this server.

%description -n XFree86-Mach64 -l pl.UTF-8
XFree86-Mach64 to X serwer dla kart opartych o układ ATI Mach64,
takich jak Graphics Xpression, GUP Turbo, WinTurbo. Uwaga: ten serwer
miewa problemy z niektórymi kartami Mach64.

%package -n XFree86-8514
Summary:	The XFree86 server program for older IBM 8514 or compatible video cards
Summary(pl.UTF-8):	Serwer XFree86 dla kart na układzie IBM 8514
Group:		X11/Servers
Provides:	Xserver
Requires:	%{name}-common = %{version}

%description -n XFree86-8514
The XFree86-8514 package contains the X server for older IBM 8514
video cards, or compatibles from a company such as ATI.

%description -n XFree86-8514 -l pl.UTF-8
XFree86-8514 zawiera X serwer dla starszych kart graficznych IBM 8514
lub kompatybilnych.

%package -n XFree86-AGX
Summary:	The XFree86 server for AGX-based video cards
Summary(pl.UTF-8):	Serwer XFree86 dla kart na układzie AGX
Group:		X11/Servers
Provides:	Xserver
Requires:	%{name}-common = %{version}

%description -n XFree86-AGX
The XFree86-AGX package contains the X server for AGX-based cards,
such as the Boca Vortex, Orchid Celsius, Spider Black Widow and
Hercules Graphite.

%description -n XFree86-AGX -l pl.UTF-8
XFree86-AGX zawiera X serwer dla kart graficznych na układzie AGX,
takich jak Roca Vortex, Orchid Celsius, Spider Black Widow, Hercules
Graphite.

%package -n XFree86-Mach32
Summary:	The XFree86 server for Mach32 based video cards
Summary(pl.UTF-8):	Serwer XFree86 dla kart na układzie Mach32
Group:		X11/Servers
Provides:	Xserver
Requires:	%{name}-common = %{version}

%description -n XFree86-Mach32
XFree86-Mach32 is the X server package for video cards built around
ATI's Mach32 chip, including the ATI Graphics Ultra Pro and Ultra
Plus.

%description -n XFree86-Mach32 -l pl.UTF-8
XFree86-Mach32 jest X serwerem dla kart graficznych opartych na
układzie ATI Mach32, w tym kart ATI Graphics Ultra Pro i Ultra Plus.

%package -n XFree86-Mach8
Summary:	The XFree86 server for Mach8 video cards
Summary(pl.UTF-8):	Serwer XFree86 dla kart na układzie Mach8
Group:		X11/Servers
Provides:	Xserver
Requires:	%{name}-common = %{version}

%description -n XFree86-Mach8
XFree86-Mach8 is the X server for video cards built around ATI's Mach8
chip, including the ATI 8514 Ultra and Graphics Ultra.

%description -n XFree86-Mach8 -l pl.UTF-8
XFree86-Mach8 jest X serwerem dla kart graficznych opartych na
układzie ATI Mach8, w tym kart ATI 8514 Ultra i Graphics Ultra.

%package -n XFree86-Mono
Summary:	A generic XFree86 monochrome server for VGA cards
Summary(pl.UTF-8):	Serwer XFree86 dla kart VGA w trybie mono
Group:		X11/Servers
Provides:	Xserver
Requires:	%{name}-common = %{version}

%description -n XFree86-Mono
XFree86-Mono is a generic monochrome (two color) server for VGA cards.
XFree86-Mono will work for nearly all VGA compatible cards, but will
only support a monochrome display.

%description -n XFree86-Mono -l pl.UTF-8
XFree86-Mono jest standardowym monochromatycznym (2-kolorowym)
serwerem dla kart VGA. Działa na prawie wszystkich kartach zgodnych z
VGA.

%package -n XFree86-P9000
Summary:	The XFree86 server for P9000 cards
Summary(pl.UTF-8):	Serwer dla kart na układzie P9000
Group:		X11/Servers
Provides:	Xserver
Requires:	%{name}-common = %{version}

%description -n XFree86-P9000
XFree86-P9000 is the X server for video cards built around the Weitek
P9000 chip, such as most Diamond Viper cards and the Orchid P9000
card.

%description -n XFree86-P9000 -l pl.UTF-8
XFree86-P9000 jest X serwerem dla kart graficznych opartych na
układzie Weitek P9000, takich jak Diamon Viper i Orchid P9000.

%package -n XFree86-SVGA
Summary:	An XFree86 server for most simple framebuffer SVGA devices
Summary(pl.UTF-8):	Serwer dla większości prostych kart SVGA
Group:		X11/Servers
Provides:	Xserver
Requires:	%{name}-common = %{version}

%description -n XFree86-SVGA
An X server for most simple frame buffer SVGA devices, including cards
built from ET4000 chips, Cirrus Logic chips, Chips and Technologies
laptop chips, Trident 8900 and 9000 chips, and Matrox chips. It also
works for Diamond Speedstar, Orchid Kelvins, STB Nitros and Horizons,
Genoa 8500VL, most Actix boards, and the Spider VLB Plus. This X
server works for many other chips and cards, so try this server if you
are having problems.

%description -n XFree86-SVGA -l pl.UTF-8
X serwer dla większości prostych kart SVGA, w tym kart zbudowanych na
układach ET4000, Cirrus Logic, Chips and Technologies, Trident 8900 i
9000, Matrox. Działa także na kartach Diamond Speedstar, Orchid
Kelvin, STB Nitro i Horizon, Genoa 8500VL, Spider VLB Plus i
większości kart Actix.

%package -n XFree86-VGA16
Summary:	A generic XFree86 server for VGA16 boards
Summary(pl.UTF-8):	Serwer XFree86 dla kart VGA w trybie 4bpp
Group:		X11/Servers
Provides:	Xserver
Requires:	%{name}-common = %{version}

%description -n XFree86-VGA16
XFree86-VGA16 is a generic 16 color server for VGA boards.
XFree86-VGA16 will work on nearly all VGA style graphics boards, but
will only support a low resolution, 16 color display.

%description -n XFree86-VGA16 -l pl.UTF-8
XFree86-VGA16 jest standardowych 16-kolorowym serwerem dla kart VGA.
Działa na prawie wszystkich kartach zgodnych z VGA.

%package -n XFree86-W32
Summary:	The XFree86 server for video cards based on ET4000/W32 chips
Summary(pl.UTF-8):	Serwer XFree86 dla kart na układzie ET4000/W32
Group:		X11/Servers
Provides:	Xserver
Requires:	%{name}-common = %{version}

%description -n XFree86-W32
XFree86-W32 is the X server for cards built around ET4000/W32 chips,
including the Genoa 8900 Phantom 32i, the Hercules Dynamite, the
LeadTek WinFast S200, the Sigma Concorde, the STB LightSpeed, the
TechWorks Thunderbolt, and the ViewTop PCI.

%description -n XFree86-W32 -l pl.UTF-8
XFree86-W32 jest X serwerem dla kart opartych na układach ET4000/W32,
w tym kart Genoa 8900 Phantom 32i, Hercules Dynamite, LeadTek WinFast
S200, Sigma Concorde, STB LightSpeed, TechWorks Thunderbolt, ViewTop
PCI.

%package -n XFree86-3DLabs
Summary:	The XFree86 server for 3Dlabs video cards
Summary(pl.UTF-8):	Serwer XFree86 dla kart na układzie 3Dlabs
Group:		X11/Servers
Provides:	Xserver
Requires:	%{name}-common = %{version}

%description -n XFree86-3DLabs
XFree86-3DLabs is the X server for cards built around 3Dlabs Glint and
Permedia chipsets, including the Glint 500TX with IBM RGB526 RAMDAC,
the Glint MX with IBM RGB526 and IBM RGB640 RAMDAC, the Permedia with
IBM RGB526 RAMDAC, and the Permedia 2 (classic, 2a, 2v).

%description -n XFree86-3DLabs -l pl.UTF-8
XFree86-3DLabs jest X serwerem dla kart graficznych na układach 3Dlabs
Glint lub Permedia, w tym Glint 500TX z RAMDAC IBM RGB526, Glint MX z
RAMDAC IBM RGB526 lub IBM RGB640, Permedia z RAMDAC IBM RGB526 oraz
Permedia 2 (classic, 2a, 2v).

%package -n XFree86-TGA
Summary:	X server for systems with Digital TGA boards based on DC21040 chips
Summary(pl.UTF-8):	X serwer dla systemów z kartami Digital TGA na układach DC21040
Group:		X11/Servers
Provides:	Xserver
Requires:	%{name}-common = %{version}

%description -n XFree86-TGA
The XFree86-TGA package contains an 8-bit X server for Digital TGA
boards based on the DC21040 chip. These adapters are often used in
Alpha workstations and are included with Alpha UDB (Multia) machines.

%description -n XFree86-TGA -l pl.UTF-8
XFree86-TGA zawiea 8-bitowy X serwer dla kart Digital TGA opartych na
układzie DC21040. Te karty są często używane na w stacjach roboczych
Alpha oraz maszynach Alpha UDB (Multia).

%package -n XFree86-FBDev
Summary:	The X server for the generic frame buffer device on some machines
Summary(pl.UTF-8):	X serwer działający w oparciu o framebuffer
Group:		X11/Servers
Provides:	Xserver
Requires:	%{name}-common = %{version}

%description -n XFree86-FBDev
The XFree86-FBDev package contains an X server for the generic frame
buffer device. This X server is usually the only choice for SPARC
machines, but also has some special capabilities that make it useful
on Intel platforms, especially laptops.

First, this X server can be used as a generic driver for a chipset
that does not yet have an Open Source driver (note that it will be
un-accelerated). Secondly, this X server "speaks" VESA protocols, so
it will produce the exact timing needed by projection systems. This
feature is handy for using your laptop to display a presentation on a
projection system on the road. Your regular X server may or may not be
in sync with the projection system, but the FBDev X server will always
work. Thirdly, this X server can produce a larger display, at a higher
resolution, for consoles on laptops.

%description -n XFree86-FBDev -l pl.UTF-8
XFree86-FBDev zawiera X serwer oparty o framebuffer. Zazwyczaj jest
jedynym dla maszyn SPARC, ale ma też możliwości przydatne na
platformach intelowskich, zwłaszcza w laptopach.

Po pierwsze, ten X serwer może być używany dla kart, które nie mają
jeszcze dedykowanego drivera (uwaga: ten serwer działa bez
akceleracji). Po drugie, ten X serwer obsługuje protokoły VESA, więc
może dostosować parametry wyświetlania do urządzenia, co jest
przydatne przy projekcjach. Po trzecie, ten X serwer może wyświetlać
większy obraz, z większą rozdzielczością na laptopach.

%package -n XFree86-Sun
Summary:	X server for Suns with monochrome and 8-bit color SBUS framebuffers
Summary(pl.UTF-8):	X serwer dla Sunów z framebufferem SBUS mono lub kolorowym 8bpp
Group:		X11/Servers
Obsoletes:	X11R6.1-Sun
Provides:	Xserver
Requires:	%{name}-common = %{version}

%description -n XFree86-Sun
The XFree86-Sun package contains the X server for Sun computers with
monochrome and 8-bit color SBUS frame buffers (for example, the CG3
and CG6 frame buffers).

%description -n XFree86-Sun -l pl.UTF-8
XFree86-Sun zawiera X serwer dla komputerów Sun z framebufferem SBUS
monochromatycznym lub z 8-bitowym kolorem (np. CG3 lub CG6).

%package -n XFree86-SunMono
Summary:	X server for Sun computers with monochrome SBUS framebuffers only
Summary(pl.UTF-8):	X serwer dla Sunów z monochromatycznym framebufferem SBUS
Group:		X11/Servers
Obsoletes:	X11R6.1-SunMono
Provides:	Xserver
Requires:	%{name}-common = %{version}

%description -n XFree86-SunMono
The XFree86-SunMono package includes an X server for Sun computers
with monochrome SBUS frame buffers only.

%description -n XFree86-SunMono -l pl.UTF-8
XFree86-SunMono zawiera X serwer dla komputerów Sun z
monochromatycznym framebufferem SBUS.

%package -n XFree86-Sun24
Summary:	The X server for Suns with all supported SBUS framebuffers
Summary(pl.UTF-8):	X serwer dla Sunów z framebufferami SBUS
Group:		X11/Servers
Obsoletes:	X11R6.1-Sun24
Provides:	Xserver
Requires:	%{name}-common = %{version}

%description -n XFree86-Sun24
The XFree86-Sun24 package contains the X server for Sun computers with
all supported SBUS frame buffers.

%description -n XFree86-Sun24 -l pl.UTF-8
XFree86-Sun24 zawiera X serwer dla komputerów Sun z framebufferem
SBUS.

%prep
%setup -q -c -a1

# install xfsft
tar x -C xc/lib -f xfsft-1.1.6/libfont.tar
patch -p0 -s -d xc/lib < xfsft-1.1.6/libfont.patch

%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1
# Fix Xconfigurator setup of Diamond SpeedStar A50
%patch4 -p1
# new cyrix driver seems wonky
%patch5 -p1
# turn off accel for sis6326 cards
%patch6 -p1
%ifarch alpha
%patch7 -p1
%endif
%ifarch sparc
# Sparc jumbo patch
%patch8 -p1
%endif
# enable i810 driver in 3.3.6; switch agpgart to X 4.0-style
%patch9 -p1
# fix memory detection on Cirrus 5480 series chips
%patch10 -p1
# fix rage mobility chipset (IBM ThinkPads)
%patch11 -p1
# 2000, not 1999!
%patch12 -p1
# probe SVGA cards in different order to avoid lockups
%patch13 -p1
# more minor MediaGX tweaks
%patch14 -p1
# fix bug in security extension (listens on port 6000)
%patch15 -p1
# fix stack overrun in xkb startup code
%patch16 -p1
# fix S3 trio3d issues
%patch17 -p0
%patch18 -p0
# make things compile with glibc 2.2
%patch19 -p0
# make alpha build with gcc 2.96
%patch20 -p0
# Only build X servers
%patch21 -p0
# fix cfb linking
%patch22 -p1
%patch23 -p1
%patch24 -p1

# Fix the header file for makedepend.
cd xc/config/imake
mkdir X11
ln -sf ../../include/Xosdefs.h X11

%build
%ifarch alpha
%{__make} World -C xc BOOTSTRAPCFLAGS="%{rpmcflags} -Wa,-m21164a" \
	CDEBUGFLAGS="%{rpmcflags} -Wa,-m21164a"
%else
%{__make} World -C xc BOOTSTRAPCFLAGS="%{rpmcflags} -pipe" \
	CDEBUGFLAGS="%{rpmcflags} -pipe"
%endif

# XXX: applies to gcc "2.96" only??? needs testing with 2.95*... -- qboosh
# There are apparently bugs in -m486. Grrrrrrrrrrrrrrr.
#%ifarch %{ix86}
#%if %{?debug:0}%{!?debug:1}
#(
#  cd xc/programs/Xserver/hw/xfree86/accel/i128/
#  rm -f i128.o libi128.a
#  %{__make} i128.o CDEBUGFLAGS="-O2 -pipe"
#  cd ../../../..
#  %{__make} CDEBUGFLAGS="$RPM_OPT_FLAGS -pipe"
#)
#%endif
#%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/{pam.d,security/console.apps},%{_includedir}}

install %{SOURCE2} $RPM_BUILD_ROOT/etc/pam.d/xserver
touch $RPM_BUILD_ROOT/etc/security/console.apps/xserver
touch $RPM_BUILD_ROOT/etc/security/blacklist.xserver

%{__make} install install.man -C xc \
	DESTDIR=$RPM_BUILD_ROOT

# setup the default X server
rm -f $RPM_BUILD_ROOT%{_bindir}/X
ln -sf Xwrapper $RPM_BUILD_ROOT%{_bindir}/X

mv -f $RPM_BUILD_ROOT%{_mandir}/man5/XF86Config.5x \
	$RPM_BUILD_ROOT%{_mandir}/man5/XF86Config-3.5x

gzip -9nf $RPM_BUILD_ROOT%{_libdir}/X11/doc/*

%clean
rm -rf $RPM_BUILD_ROOT

%files common
%defattr(644,root,root,755)
%attr(4755,root,root) %{_bindir}/Xwrapper
%attr(755,root,root) %{_bindir}/X
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/xserver
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist.xserver
%config(missingok) /etc/security/console.apps/xserver
%{_mandir}/man5/XF86Config-3.5x*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/XF86Config.eg
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/AccelCards*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/Devices*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/Monitors*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/QuickStart.doc*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.gz
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.Config*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.DGA*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.Linux*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.mouse*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/RELNOTES*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/VideoModes.doc*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/xinput*
%ifarch %{ix86} alpha
%attr(755,root,root) %{_libdir}/modules/*
%endif

%ifarch %{ix86} alpha
%files -n XFree86-SVGA
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/XF86_SVGA
%{_mandir}/man1/XF86_SVGA.1x*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.MGA*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.NVIDIA*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.Oak*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.S3V*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.SiS*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.Video7*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.W32*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.WstDig*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.apm*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.ark*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.ati*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.chips*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.cirrus*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.cyrix*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.epson*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.i740*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.i810*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.neo*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.r128*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.rendition*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.trident*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.tseng*
%endif

%ifarch %{ix86} sparc
%files -n XFree86-VGA16
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/XF86_VGA16
%{_mandir}/man1/XF86_VGA16.1x*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.cyrix*
%endif

%ifarch %{ix86}
%files -n XFree86-W32
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/XF86_W32
%{_mandir}/man1/XF86_W32.1x*
%{_mandir}/man1/XF86_Accel.1x*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.W32*
%endif

%ifarch %{ix86} alpha
%files -n XFree86-Mono
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/XF86_Mono
%{_mandir}/man1/XF86_Mono.1x*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.cyrix*
%endif

%ifarch %{ix86} alpha
%files -n XFree86-S3
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/XF86_S3
%{_mandir}/man1/XF86_S3.1x*
%{_mandir}/man1/XF86_Accel.1x*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.S3.gz
%endif

%ifarch %{ix86} alpha
%files -n XFree86-S3V
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/XF86_S3V
%{_mandir}/man1/XF86_S3.1x*
%{_mandir}/man1/XF86_Accel.1x*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.S3V*
%endif

%ifarch %{ix86}
%files -n XFree86-8514
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/XF86_8514
%{_mandir}/man1/XF86_8514.1x*
%{_mandir}/man1/XF86_Accel.1x*
%endif

%ifarch %{ix86}
%files -n XFree86-Mach8
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/XF86_Mach8
%{_mandir}/man1/XF86_Mach8.1x*
%{_mandir}/man1/XF86_Accel.1x*
%endif

%ifarch %{ix86}
%files -n XFree86-Mach32
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/XF86_Mach32
%{_mandir}/man1/XF86_Mach32.1x*
%{_mandir}/man1/XF86_Accel.1x*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.Mach32*
%endif

%ifarch %{ix86} alpha sparc
%files -n XFree86-Mach64
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/XF86_Mach64
%{_mandir}/man1/XF86_Mach64.1x*
%{_mandir}/man1/XF86_Accel.1x*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.Mach64*
%endif

%ifarch %{ix86} alpha
%files -n XFree86-P9000
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/XF86_P9000
%{_mandir}/man1/XF86_P9000.1x*
%{_mandir}/man1/XF86_Accel.1x*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.P9000*
%endif

%ifarch %{ix86}
%files -n XFree86-AGX
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/XF86_AGX
%{_mandir}/man1/XF86_AGX.1x*
%{_mandir}/man1/XF86_Accel.1x*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.agx*
%endif

%ifarch %{ix86}
%files -n XFree86-I128
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/XF86_I128
%{_mandir}/man1/XF86_I128.1x*
%{_mandir}/man1/XF86_Accel.1x*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.I128*
%endif

%ifarch %{ix86} alpha sparc
%files -n XFree86-3DLabs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/XF86_3DLabs
%{_mandir}/man1/XF86_Accel.1x*
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.3DLabs*
%endif

%ifarch alpha
%files -n XFree86-TGA
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/XF86_TGA
%doc $RPM_BUILD_ROOT%{_libdir}/X11/doc/README.DECtga*
%endif

%ifarch m68k armv4l
%files -n XFree86-FBDev
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/XF68_FBDev
%{_mandir}/man1/XF68_FBDev.1x*
%endif

%ifarch %{ix86} alpha sparc
%files -n XFree86-FBDev
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/XF86_FBDev
%endif

%ifarch sparc
%files -n XFree86-Sun
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xsun
%endif

%ifarch sparc
%files -n XFree86-SunMono
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/XsunMono
%endif

%ifarch sparc
%files -n XFree86-Sun24
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xsun24
%endif
