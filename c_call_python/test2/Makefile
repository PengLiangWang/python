all: test
test: test.o
	gcc -L/usr/lib/python2.6/ -lpython2.6 -ldl test.o -o test
test.o: test.c
	gcc -Wall -c test.c -I/usr/include/python2.6/
clean:
	@rm -rf *.o *.pyc test
