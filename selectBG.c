#include "python.h" 
#include <stdio.h>

static PyObject * 
selectBG(PyObject *self, PyObject *args)
{
	int n;
	const char* image;

    if (!PyArg_ParseTuple(args, "i", &n)) // �Ű����� ���� �м��ϰ� ���������� �Ҵ� ��ŵ�ϴ�.
         return NULL; 

	switch (n) {
	case 1:
		image = "#F79F81";
		break;
	case 2:
		image = "#F6D8CE";
		break;
	}

    return Py_BuildValue("s", image);
}


static PyMethodDef SpamMethods[] = {
    {"selectbg", selectBG, METH_VARARGS,
    "count a string length."},
    {NULL, NULL, 0, NULL}    //�迭�� ���� ��Ÿ����.
};


static struct PyModuleDef spammodule = {
    PyModuleDef_HEAD_INIT,
    "spam",            // ��� �̸�
    "It is test module.", // ��� ������ ���� �κ�, ����� __doc__�� ����˴ϴ�.
    -1,SpamMethods
};

PyMODINIT_FUNC
PyInit_selectBG(void)
{
    return PyModule_Create(&spammodule);
}
