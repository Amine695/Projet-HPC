CC = mpicc
CFLAGS = -std=c99 -g -Wall -Wextra -Werror -O3 -march=native -mavx2 -I .
LDFLAGS =


all: lanczos_modp checker_modp
lanczos_modp: mmio.o lanczos_modp.o
lanczos_modp.o: lanczos_modp.c mmio.h
checker_modp:   mmio.o checker_modp.o
checker_modp.o: checker_modp.c mmio.h

clean:
	rm -f *.o
	rm -f lanczos_modp checker_modp
