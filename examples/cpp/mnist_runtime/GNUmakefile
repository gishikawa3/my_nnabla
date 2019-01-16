all: mnist_runtime.cpp
	$(CXX) -std=c++11 -D TIMING -O -o  mnist_runtime mnist_runtime.cpp -I/home/mukai/nnabla/src/nbla_utils -L/home/mukai/nnabla/buildC/lib -L/usr/lib/x86_64-linux-gnu/hdf5/serial -lhdf5 -llzma -lnnabla -lnnabla_utils

cuda: mnist_runtime.cpp
	$(CXX) -std=c++11 -D TIMING -D WITH_CUDA -O -o mnist_runtime_cuda mnist_runtime.cpp -lnnabla -lnnabla_utils -lnnabla_cuda

clean:
	rm -f mnist_runtime
