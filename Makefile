CC = gcc
CFLAGS = -std=c99 -g -Wall -Wextra -Werror -pg -O3 -march=native -fopenmp -mavx2 -I .
LDFLAGS =-fopenmp

# Uncomment these for OpenMP
CFLAGS += -fopenmp
LDFLAGS += -fopenmp

all: lanczos_modp checker_modp
lanczos_modp: mmio.o lanczos_modp.o
lanczos_modp.o: lanczos_modp.c mmio.h
checker_modp:   mmio.o checker_modp.o
checker_modp.o: checker_modp.c mmio.h

clean:
	rm -f *.o
	rm -f lanczos_modp checker_modp