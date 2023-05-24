CFLAGS:=-Wall 

.PHONY: all
all: fnv.o 

fnv.o: fnv.c fnv.h
	$(CC) -c $(CFLAGS) $<

.PHONY: clean
clean:
	rm -f *.o *.so _fnv*
