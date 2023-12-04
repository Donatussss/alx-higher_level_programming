#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints info about a python list
 * @p: PyObject
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	long int list_size;
	PyListObject *list;
	PyObject *item;

	list_size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", list_size);
	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	for (int x = 0; x < list_size; x++)
	{
		item = PyList_GetItem(p, x);
		printf("Element %ld: %s\n", x, Py_TYPE(item)->tp_name);
	}
}
