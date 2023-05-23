CFLAGS:=-Wall 

.PHONY: all
all: fnv0.o 

fnv0.o: fnv0.c fnv0.h
	$(CC) -c $(CFLAGS) $<

.PHONY: clean
clean:
	rm -f *.o *.so _fnv0*
