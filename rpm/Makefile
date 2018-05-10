RPMBUILD_ROOT=~/rpmbuild
RPMBUILD_SOURCES=$(RPMBUILD_ROOT)/SOURCES
RPMBUILD_SPECS=$(RPMBUILD_ROOT)/SPECS
RPMBUILD_RPMS=$(RPMBUILD_ROOT)/RPMS
RPMBUILD_RPMS_i386=$(RPMBUILD_RPMS)/i386
RPMBUILD_RPMS_x86_64=$(RPMBUILD_RPMS)/x86_64

.PHONY: clean i386 x86_64 all

all: i386 x86_64

clean:
	rm -f $(RPMBUILD_SOURCES)/*
	rm -f $(RPMBUILD_SPECS)/*
	rm -f $(RPMBUILD_RPMS_i386)/*
	rm -f $(RPMBUILD_RPMS_x86_64)/*
	rm -f *.rpm

i386: $(RPMBUILD_RPMS_i386)/librawnet-1.0.0-1.i386.rpm \
      $(RPMBUILD_RPMS_i386)/librawnet-static-1.0.0-1.i386.rpm \
	  $(RPMBUILD_RPMS_i386)/librawnet-devel-1.0.0-1.i386.rpm \
	  librawnet-devel-1.0.0-3.rpm

$(RPMBUILD_SPECS)/%.spec: %.spec
	cp -f $< $@


$(RPMBUILD_SOURCES)/librawnet-1.0.0.tar.gz:
	ln -s librawnet/ ../../librawnet-1.0.0
	tar cvzh -C ../../ -f $@ librawnet-1.0.0/
	rm -f ../../librawnet-1.0.0

$(RPMBUILD_RPMS_i386)/librawnet-1.0.0-1.i386.rpm: $(RPMBUILD_SOURCES)/librawnet-1.0.0.tar.gz \
												  $(RPMBUILD_SPECS)/librawnet-1.0.0-1.spec
	setarch i386 rpmbuild -ba --target=i386 $(RPMBUILD_SPECS)/librawnet-1.0.0-1.spec


$(RPMBUILD_SOURCES)/librawnet-static-1.0.0.tar.gz:
	ln -s librawnet/ ../../librawnet-static-1.0.0
	tar cvzh -C ../../ -f $@ librawnet-static-1.0.0/
	rm -f ../../librawnet-static-1.0.0

$(RPMBUILD_RPMS_i386)/librawnet-static-1.0.0-1.i386.rpm: $(RPMBUILD_SOURCES)/librawnet-static-1.0.0.tar.gz \
														 $(RPMBUILD_SPECS)/librawnet-static-1.0.0-1.spec
	setarch i386 rpmbuild -ba --target=i386 $(RPMBUILD_SPECS)/librawnet-static-1.0.0-1.spec


$(RPMBUILD_SOURCES)/librawnet-devel-1.0.0.tar.gz:
	ln -s librawnet/ ../../librawnet-devel-1.0.0
	tar cvzh -C ../../ -f $@ librawnet-devel-1.0.0/
	rm -f ../../librawnet-devel-1.0.0

$(RPMBUILD_RPMS_i386)/librawnet-devel-1.0.0-1.i386.rpm: $(RPMBUILD_SOURCES)/librawnet-devel-1.0.0.tar.gz \
												        $(RPMBUILD_SPECS)/librawnet-devel-1.0.0-1.spec
	setarch i386 rpmbuild -ba --target=i386 $(RPMBUILD_SPECS)/librawnet-devel-1.0.0-1.spec

$(RPMBUILD_RPMS_i386)/librawnet-devel-1.0.0-3.i386.rpm: $(RPMBUILD_SOURCES)/librawnet-devel-1.0.0.tar.gz \
												        $(RPMBUILD_SPECS)/librawnet-devel-1.0.0-3.spec
	setarch i386 rpmbuild -ba --target=i386 $(RPMBUILD_SPECS)/librawnet-devel-1.0.0-3.spec

librawnet-devel-1.0.0-3.rpm: $(RPMBUILD_RPMS_i386)/librawnet-devel-1.0.0-3.i386.rpm
	cp $< $@



x86_64: $(RPMBUILD_RPMS_x86_64)/lib64rawnet-1.0.0-1.x86_64.rpm \
        $(RPMBUILD_RPMS_x86_64)/lib64rawnet-static-1.0.0-1.x86_64.rpm \
	    $(RPMBUILD_RPMS_x86_64)/lib64rawnet-devel-1.0.0-1.x86_64.rpm \
	    lib64rawnet-devel-1.0.0-3.rpm

$(RPMBUILD_SOURCES)/lib64rawnet-1.0.0.tar.gz:
	ln -s librawnet/ ../../lib64rawnet-1.0.0
	tar cvzh -C ../../ -f $@ lib64rawnet-1.0.0/
	rm -f ../../lib64rawnet-1.0.0

$(RPMBUILD_RPMS_x86_64)/lib64rawnet-1.0.0-1.x86_64.rpm: $(RPMBUILD_SOURCES)/lib64rawnet-1.0.0.tar.gz \
														$(RPMBUILD_SPECS)/lib64rawnet-1.0.0-1.spec
	rpmbuild -ba --target=x86_64 $(RPMBUILD_SPECS)/lib64rawnet-1.0.0-1.spec


$(RPMBUILD_SOURCES)/lib64rawnet-static-1.0.0.tar.gz:
	ln -s librawnet/ ../../lib64rawnet-static-1.0.0
	tar cvzh -C ../../ -f $@ lib64rawnet-static-1.0.0/
	rm -f ../../lib64rawnet-static-1.0.0

$(RPMBUILD_RPMS_x86_64)/lib64rawnet-static-1.0.0-1.x86_64.rpm: $(RPMBUILD_SOURCES)/lib64rawnet-static-1.0.0.tar.gz \
															   $(RPMBUILD_SPECS)/lib64rawnet-static-1.0.0-1.spec
	rpmbuild -ba --target=x86_64 $(RPMBUILD_SPECS)/lib64rawnet-static-1.0.0-1.spec

$(RPMBUILD_SOURCES)/lib64rawnet-devel-1.0.0.tar.gz:
	ln -s librawnet/ ../../lib64rawnet-devel-1.0.0
	tar cvzh -C ../../ -f $@ lib64rawnet-devel-1.0.0/
	rm -f ../../lib64rawnet-devel-1.0.0

$(RPMBUILD_RPMS_x86_64)/lib64rawnet-devel-1.0.0-1.x86_64.rpm: $(RPMBUILD_SOURCES)/lib64rawnet-devel-1.0.0.tar.gz \
														      $(RPMBUILD_SPECS)/lib64rawnet-devel-1.0.0-1.spec
	rpmbuild -ba --target=x86_64 $(RPMBUILD_SPECS)/lib64rawnet-devel-1.0.0-1.spec

$(RPMBUILD_RPMS_x86_64)/lib64rawnet-devel-1.0.0-3.x86_64.rpm: $(RPMBUILD_SOURCES)/lib64rawnet-devel-1.0.0.tar.gz \
							      						      $(RPMBUILD_SPECS)/lib64rawnet-devel-1.0.0-3.spec
	rpmbuild -ba --target=x86_64 $(RPMBUILD_SPECS)/lib64rawnet-devel-1.0.0-3.spec

lib64rawnet-devel-1.0.0-3.rpm: $(RPMBUILD_RPMS_x86_64)/lib64rawnet-devel-1.0.0-3.x86_64.rpm
	cp $< $@
