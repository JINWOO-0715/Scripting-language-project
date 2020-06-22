#include "python.h" 
#include <stdio.h>

static PyObject * 
selectBG(PyObject *self, PyObject *args)
{
	int n;
	const char* image;

    if (!PyArg_ParseTuple(args, "i", &n)) // 매개변수 값을 분석하고 지역변수에 할당 시킵니다.
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
    {NULL, NULL, 0, NULL}    //배열의 끝을 나타낸다.
};


static struct PyModuleDef spammodule = {
    PyModuleDef_HEAD_INIT,
    "spam",            // 모듈 이름
    "It is test module.", // 모듈 설명을 적는 부분, 모듈의 __doc__에 저장됩니다.
    -1,SpamMethods
};

PyMODINIT_FUNC
PyInit_selectBG(void)
{
    return PyModule_Create(&spammodule);
}
