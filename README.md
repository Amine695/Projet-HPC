# HPC Project (High Performance Computing)

The goal of the project is to parallelize a sequential program, the **Block-Lanczos** algorithm which performs the resolution of linear systems of the type xM = 0 mod p, where M is a sparse matrix of size N × (N - k). The parallelization of this program has been made using several librairies such as **MPI** and **OpenMP**. We had a special access to Grid 5000 to benchmark our code. 

Grid'5000 is a large-scale and flexible testbed for experiment-driven research in all areas of computer science, with a focus on parallel and distributed computing including Cloud, HPC and Big Data and AI.

## Work done
- [x] Exploration of sequential code performance (hotspots, etc.).
- [x] Parallelization with MPI only on a cluster
- [x] Parallelization with OpenMP only on a multi-core machine
- [x] Parallelization with MPI + OpenMP: we launch a single MPI process per node and we do multi-threaded inside.
