# OpenCV_Optimization_using_Cython

Some examples of OpenCV Python code optimization using the very powerful tool Cython

Brief Description of the Method:

1/ Write a valid Python .py file and test it
2/ You can evaluate how much time it consumes using IPython or simply the time library. In case you are also using OpenCV there are other techniques like the getTickFrequency() and getTickCount() functions.
3/ First execute the cmmand to detect where you can optimize using cython. An HTML file containing information about possible optimizations will be generated.
	$ cython -a myFileName.py
3/ Now you have to traslate .py file to .pyx file and perform your optimizations by:
	- Replacing "def" by "cdef" or "cpdef"
	- The major optimization will be performed if you add variables declarations such as (cdef int x, y for scalar variables or  cdef unsigned char [:, :] image for arrays ... etc.)
4/ Now let's generate .C files using the command you will notice that .C are generated.
	$ cython myFileName.pyx  		#if no main function
or	$ cython --embed  myFileName.pyx 	#if you have a main function
5/ Now we need to compile the generated files using the command:
	$ gcc $CFLAGS -I/usr/include/python2.7 -o EXECUTABLE_FILE_NAME SOURCE_FILE_NAME.c -lpython2.7 -lpthread -lm -lutil -ldl
6/ An executable will be generated and can be ran using the command:
	$ ./EXECUTABLE_FILE_NAME


REFERENCES:
http://www.pyimagesearch.com/2017/08/28/fast-optimized-for-pixel-loops-with-opencv-and-python/
https://python.g-node.org/python-summerschool-2012/_media/cython/kiel2012_cython.pdf


