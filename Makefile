all:
	cd Hybrid && make
	cd OpenMP && make
	cd MPI && make

clean:
	cd Hybrid && make  clean
	cd OpenMP && make clean
	cd MPI && make clean


