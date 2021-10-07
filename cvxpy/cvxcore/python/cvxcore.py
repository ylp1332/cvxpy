# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info

if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _cvxcore
else:
    import _cvxcore

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self) -> str:
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator:
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _cvxcore.delete_SwigPyIterator

    def value(self):
        return _cvxcore.SwigPyIterator_value(self)

    def incr(self, n: int = 1):
        return _cvxcore.SwigPyIterator_incr(self, n)

    def decr(self, n: int = 1):
        return _cvxcore.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _cvxcore.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _cvxcore.SwigPyIterator_equal(self, x)

    def copy(self):
        return _cvxcore.SwigPyIterator_copy(self)

    def next(self):
        return _cvxcore.SwigPyIterator_next(self)

    def __next__(self):
        return _cvxcore.SwigPyIterator___next__(self)

    def previous(self):
        return _cvxcore.SwigPyIterator_previous(self)

    def advance(self, n):
        return _cvxcore.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _cvxcore.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _cvxcore.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _cvxcore.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _cvxcore.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _cvxcore.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _cvxcore.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _cvxcore:
_cvxcore.SwigPyIterator_swigregister(SwigPyIterator)

VARIABLE = _cvxcore.VARIABLE
PARAM = _cvxcore.PARAM
PROMOTE = _cvxcore.PROMOTE
MUL = _cvxcore.MUL
RMUL = _cvxcore.RMUL
MUL_ELEM = _cvxcore.MUL_ELEM
DIV = _cvxcore.DIV
SUM = _cvxcore.SUM
NEG = _cvxcore.NEG
INDEX = _cvxcore.INDEX
TRANSPOSE = _cvxcore.TRANSPOSE
SUM_ENTRIES = _cvxcore.SUM_ENTRIES
TRACE = _cvxcore.TRACE
RESHAPE = _cvxcore.RESHAPE
DIAG_VEC = _cvxcore.DIAG_VEC
DIAG_MAT = _cvxcore.DIAG_MAT
UPPER_TRI = _cvxcore.UPPER_TRI
CONV = _cvxcore.CONV
HSTACK = _cvxcore.HSTACK
VSTACK = _cvxcore.VSTACK
SCALAR_CONST = _cvxcore.SCALAR_CONST
DENSE_CONST = _cvxcore.DENSE_CONST
SPARSE_CONST = _cvxcore.SPARSE_CONST
NO_OP = _cvxcore.NO_OP
KRON = _cvxcore.KRON
class LinOp:
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, type, shape, args) -> None:
        _cvxcore.LinOp_swiginit(self, _cvxcore.new_LinOp(type, shape, args))

    def get_type(self):
        return _cvxcore.LinOp_get_type(self)

    def is_constant(self) -> bool:
        return _cvxcore.LinOp_is_constant(self)

    def get_shape(self):
        return _cvxcore.LinOp_get_shape(self)

    def get_args(self):
        return _cvxcore.LinOp_get_args(self)

    def get_slice(self):
        return _cvxcore.LinOp_get_slice(self)

    def push_back_slice_vec(self, slice_vec):
        return _cvxcore.LinOp_push_back_slice_vec(self, slice_vec)

    def has_numerical_data(self):
        return _cvxcore.LinOp_has_numerical_data(self)

    def get_linOp_data(self):
        return _cvxcore.LinOp_get_linOp_data(self)

    def set_linOp_data(self, tree):
        return _cvxcore.LinOp_set_linOp_data(self, tree)

    def get_data_ndim(self):
        return _cvxcore.LinOp_get_data_ndim(self)

    def set_data_ndim(self, ndim):
        return _cvxcore.LinOp_set_data_ndim(self, ndim)

    def is_sparse(self) -> bool:
        return _cvxcore.LinOp_is_sparse(self)

    def get_sparse_data(self):
        return _cvxcore.LinOp_get_sparse_data(self)

    def get_dense_data(self):
        return _cvxcore.LinOp_get_dense_data(self)

    def set_dense_data(self, matrix):
        return _cvxcore.LinOp_set_dense_data(self, matrix)

    def set_sparse_data(self, data, row_idxs, col_idxs, rows, cols):
        return _cvxcore.LinOp_set_sparse_data(self, data, row_idxs, col_idxs, rows, cols)
    __swig_destroy__ = _cvxcore.delete_LinOp

# Register LinOp in _cvxcore:
_cvxcore.LinOp_swigregister(LinOp)


def vecprod(vec):
    return _cvxcore.vecprod(vec)

def vecprod_before(vec, end):
    return _cvxcore.vecprod_before(vec, end)

def tensor_mul(lh_ten, rh_ten):
    return _cvxcore.tensor_mul(lh_ten, rh_ten)

def acc_tensor(lh_ten, rh_ten):
    return _cvxcore.acc_tensor(lh_ten, rh_ten)

def diagonalize(mat):
    return _cvxcore.diagonalize(mat)
class ProblemData:
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    TensorV = property(_cvxcore.ProblemData_TensorV_get, _cvxcore.ProblemData_TensorV_set)
    TensorI = property(_cvxcore.ProblemData_TensorI_get, _cvxcore.ProblemData_TensorI_set)
    TensorJ = property(_cvxcore.ProblemData_TensorJ_get, _cvxcore.ProblemData_TensorJ_set)
    param_id = property(_cvxcore.ProblemData_param_id_get, _cvxcore.ProblemData_param_id_set)
    vec_idx = property(_cvxcore.ProblemData_vec_idx_get, _cvxcore.ProblemData_vec_idx_set)

    def init_id(self, new_param_id, param_size):
        return _cvxcore.ProblemData_init_id(self, new_param_id, param_size)

    def getLen(self):
        return _cvxcore.ProblemData_getLen(self)

    def getV(self, values):
        return _cvxcore.ProblemData_getV(self, values)

    def getI(self, values):
        return _cvxcore.ProblemData_getI(self, values)

    def getJ(self, values):
        return _cvxcore.ProblemData_getJ(self, values)

    def __init__(self) -> None:
        _cvxcore.ProblemData_swiginit(self, _cvxcore.new_ProblemData())
    __swig_destroy__ = _cvxcore.delete_ProblemData

# Register ProblemData in _cvxcore:
_cvxcore.ProblemData_swigregister(ProblemData)
cvar = _cvxcore.cvar
CONSTANT_ID = cvar.CONSTANT_ID

class IntVector:
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _cvxcore.IntVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _cvxcore.IntVector___nonzero__(self)

    def __bool__(self):
        return _cvxcore.IntVector___bool__(self)

    def __len__(self):
        return _cvxcore.IntVector___len__(self)

    def __getslice__(self, i, j):
        return _cvxcore.IntVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _cvxcore.IntVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _cvxcore.IntVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _cvxcore.IntVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _cvxcore.IntVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _cvxcore.IntVector___setitem__(self, *args)

    def pop(self):
        return _cvxcore.IntVector_pop(self)

    def append(self, x):
        return _cvxcore.IntVector_append(self, x)

    def empty(self):
        return _cvxcore.IntVector_empty(self)

    def size(self):
        return _cvxcore.IntVector_size(self)

    def swap(self, v):
        return _cvxcore.IntVector_swap(self, v)

    def begin(self):
        return _cvxcore.IntVector_begin(self)

    def end(self):
        return _cvxcore.IntVector_end(self)

    def rbegin(self):
        return _cvxcore.IntVector_rbegin(self)

    def rend(self):
        return _cvxcore.IntVector_rend(self)

    def clear(self):
        return _cvxcore.IntVector_clear(self)

    def get_allocator(self):
        return _cvxcore.IntVector_get_allocator(self)

    def pop_back(self):
        return _cvxcore.IntVector_pop_back(self)

    def erase(self, *args):
        return _cvxcore.IntVector_erase(self, *args)

    def __init__(self, *args) -> None:
        _cvxcore.IntVector_swiginit(self, _cvxcore.new_IntVector(*args))

    def push_back(self, x):
        return _cvxcore.IntVector_push_back(self, x)

    def front(self):
        return _cvxcore.IntVector_front(self)

    def back(self):
        return _cvxcore.IntVector_back(self)

    def assign(self, n, x):
        return _cvxcore.IntVector_assign(self, n, x)

    def resize(self, *args):
        return _cvxcore.IntVector_resize(self, *args)

    def insert(self, *args):
        return _cvxcore.IntVector_insert(self, *args)

    def reserve(self, n):
        return _cvxcore.IntVector_reserve(self, n)

    def capacity(self):
        return _cvxcore.IntVector_capacity(self)
    __swig_destroy__ = _cvxcore.delete_IntVector

# Register IntVector in _cvxcore:
_cvxcore.IntVector_swigregister(IntVector)

class DoubleVector:
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _cvxcore.DoubleVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _cvxcore.DoubleVector___nonzero__(self)

    def __bool__(self):
        return _cvxcore.DoubleVector___bool__(self)

    def __len__(self):
        return _cvxcore.DoubleVector___len__(self)

    def __getslice__(self, i, j):
        return _cvxcore.DoubleVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _cvxcore.DoubleVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _cvxcore.DoubleVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _cvxcore.DoubleVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _cvxcore.DoubleVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _cvxcore.DoubleVector___setitem__(self, *args)

    def pop(self):
        return _cvxcore.DoubleVector_pop(self)

    def append(self, x):
        return _cvxcore.DoubleVector_append(self, x)

    def empty(self):
        return _cvxcore.DoubleVector_empty(self)

    def size(self):
        return _cvxcore.DoubleVector_size(self)

    def swap(self, v):
        return _cvxcore.DoubleVector_swap(self, v)

    def begin(self):
        return _cvxcore.DoubleVector_begin(self)

    def end(self):
        return _cvxcore.DoubleVector_end(self)

    def rbegin(self):
        return _cvxcore.DoubleVector_rbegin(self)

    def rend(self):
        return _cvxcore.DoubleVector_rend(self)

    def clear(self):
        return _cvxcore.DoubleVector_clear(self)

    def get_allocator(self):
        return _cvxcore.DoubleVector_get_allocator(self)

    def pop_back(self):
        return _cvxcore.DoubleVector_pop_back(self)

    def erase(self, *args):
        return _cvxcore.DoubleVector_erase(self, *args)

    def __init__(self, *args) -> None:
        _cvxcore.DoubleVector_swiginit(self, _cvxcore.new_DoubleVector(*args))

    def push_back(self, x):
        return _cvxcore.DoubleVector_push_back(self, x)

    def front(self):
        return _cvxcore.DoubleVector_front(self)

    def back(self):
        return _cvxcore.DoubleVector_back(self)

    def assign(self, n, x):
        return _cvxcore.DoubleVector_assign(self, n, x)

    def resize(self, *args):
        return _cvxcore.DoubleVector_resize(self, *args)

    def insert(self, *args):
        return _cvxcore.DoubleVector_insert(self, *args)

    def reserve(self, n):
        return _cvxcore.DoubleVector_reserve(self, n)

    def capacity(self):
        return _cvxcore.DoubleVector_capacity(self)
    __swig_destroy__ = _cvxcore.delete_DoubleVector

# Register DoubleVector in _cvxcore:
_cvxcore.DoubleVector_swigregister(DoubleVector)

class IntVector2D:
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _cvxcore.IntVector2D_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _cvxcore.IntVector2D___nonzero__(self)

    def __bool__(self):
        return _cvxcore.IntVector2D___bool__(self)

    def __len__(self):
        return _cvxcore.IntVector2D___len__(self)

    def __getslice__(self, i, j):
        return _cvxcore.IntVector2D___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _cvxcore.IntVector2D___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _cvxcore.IntVector2D___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _cvxcore.IntVector2D___delitem__(self, *args)

    def __getitem__(self, *args):
        return _cvxcore.IntVector2D___getitem__(self, *args)

    def __setitem__(self, *args):
        return _cvxcore.IntVector2D___setitem__(self, *args)

    def pop(self):
        return _cvxcore.IntVector2D_pop(self)

    def append(self, x):
        return _cvxcore.IntVector2D_append(self, x)

    def empty(self):
        return _cvxcore.IntVector2D_empty(self)

    def size(self):
        return _cvxcore.IntVector2D_size(self)

    def swap(self, v):
        return _cvxcore.IntVector2D_swap(self, v)

    def begin(self):
        return _cvxcore.IntVector2D_begin(self)

    def end(self):
        return _cvxcore.IntVector2D_end(self)

    def rbegin(self):
        return _cvxcore.IntVector2D_rbegin(self)

    def rend(self):
        return _cvxcore.IntVector2D_rend(self)

    def clear(self):
        return _cvxcore.IntVector2D_clear(self)

    def get_allocator(self):
        return _cvxcore.IntVector2D_get_allocator(self)

    def pop_back(self):
        return _cvxcore.IntVector2D_pop_back(self)

    def erase(self, *args):
        return _cvxcore.IntVector2D_erase(self, *args)

    def __init__(self, *args) -> None:
        _cvxcore.IntVector2D_swiginit(self, _cvxcore.new_IntVector2D(*args))

    def push_back(self, x):
        return _cvxcore.IntVector2D_push_back(self, x)

    def front(self):
        return _cvxcore.IntVector2D_front(self)

    def back(self):
        return _cvxcore.IntVector2D_back(self)

    def assign(self, n, x):
        return _cvxcore.IntVector2D_assign(self, n, x)

    def resize(self, *args):
        return _cvxcore.IntVector2D_resize(self, *args)

    def insert(self, *args):
        return _cvxcore.IntVector2D_insert(self, *args)

    def reserve(self, n):
        return _cvxcore.IntVector2D_reserve(self, n)

    def capacity(self):
        return _cvxcore.IntVector2D_capacity(self)
    __swig_destroy__ = _cvxcore.delete_IntVector2D

# Register IntVector2D in _cvxcore:
_cvxcore.IntVector2D_swigregister(IntVector2D)

class DoubleVector2D:
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _cvxcore.DoubleVector2D_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _cvxcore.DoubleVector2D___nonzero__(self)

    def __bool__(self):
        return _cvxcore.DoubleVector2D___bool__(self)

    def __len__(self):
        return _cvxcore.DoubleVector2D___len__(self)

    def __getslice__(self, i, j):
        return _cvxcore.DoubleVector2D___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _cvxcore.DoubleVector2D___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _cvxcore.DoubleVector2D___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _cvxcore.DoubleVector2D___delitem__(self, *args)

    def __getitem__(self, *args):
        return _cvxcore.DoubleVector2D___getitem__(self, *args)

    def __setitem__(self, *args):
        return _cvxcore.DoubleVector2D___setitem__(self, *args)

    def pop(self):
        return _cvxcore.DoubleVector2D_pop(self)

    def append(self, x):
        return _cvxcore.DoubleVector2D_append(self, x)

    def empty(self):
        return _cvxcore.DoubleVector2D_empty(self)

    def size(self):
        return _cvxcore.DoubleVector2D_size(self)

    def swap(self, v):
        return _cvxcore.DoubleVector2D_swap(self, v)

    def begin(self):
        return _cvxcore.DoubleVector2D_begin(self)

    def end(self):
        return _cvxcore.DoubleVector2D_end(self)

    def rbegin(self):
        return _cvxcore.DoubleVector2D_rbegin(self)

    def rend(self):
        return _cvxcore.DoubleVector2D_rend(self)

    def clear(self):
        return _cvxcore.DoubleVector2D_clear(self)

    def get_allocator(self):
        return _cvxcore.DoubleVector2D_get_allocator(self)

    def pop_back(self):
        return _cvxcore.DoubleVector2D_pop_back(self)

    def erase(self, *args):
        return _cvxcore.DoubleVector2D_erase(self, *args)

    def __init__(self, *args) -> None:
        _cvxcore.DoubleVector2D_swiginit(self, _cvxcore.new_DoubleVector2D(*args))

    def push_back(self, x):
        return _cvxcore.DoubleVector2D_push_back(self, x)

    def front(self):
        return _cvxcore.DoubleVector2D_front(self)

    def back(self):
        return _cvxcore.DoubleVector2D_back(self)

    def assign(self, n, x):
        return _cvxcore.DoubleVector2D_assign(self, n, x)

    def resize(self, *args):
        return _cvxcore.DoubleVector2D_resize(self, *args)

    def insert(self, *args):
        return _cvxcore.DoubleVector2D_insert(self, *args)

    def reserve(self, n):
        return _cvxcore.DoubleVector2D_reserve(self, n)

    def capacity(self):
        return _cvxcore.DoubleVector2D_capacity(self)
    __swig_destroy__ = _cvxcore.delete_DoubleVector2D

# Register DoubleVector2D in _cvxcore:
_cvxcore.DoubleVector2D_swigregister(DoubleVector2D)

class IntIntMap:
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _cvxcore.IntIntMap_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _cvxcore.IntIntMap___nonzero__(self)

    def __bool__(self):
        return _cvxcore.IntIntMap___bool__(self)

    def __len__(self):
        return _cvxcore.IntIntMap___len__(self)
    def __iter__(self):
        return self.key_iterator()
    def iterkeys(self):
        return self.key_iterator()
    def itervalues(self):
        return self.value_iterator()
    def iteritems(self):
        return self.iterator()

    def __getitem__(self, key):
        return _cvxcore.IntIntMap___getitem__(self, key)

    def __delitem__(self, key):
        return _cvxcore.IntIntMap___delitem__(self, key)

    def has_key(self, key):
        return _cvxcore.IntIntMap_has_key(self, key)

    def keys(self):
        return _cvxcore.IntIntMap_keys(self)

    def values(self):
        return _cvxcore.IntIntMap_values(self)

    def items(self):
        return _cvxcore.IntIntMap_items(self)

    def __contains__(self, key):
        return _cvxcore.IntIntMap___contains__(self, key)

    def key_iterator(self):
        return _cvxcore.IntIntMap_key_iterator(self)

    def value_iterator(self):
        return _cvxcore.IntIntMap_value_iterator(self)

    def __setitem__(self, *args):
        return _cvxcore.IntIntMap___setitem__(self, *args)

    def asdict(self):
        return _cvxcore.IntIntMap_asdict(self)

    def __init__(self, *args) -> None:
        _cvxcore.IntIntMap_swiginit(self, _cvxcore.new_IntIntMap(*args))

    def empty(self):
        return _cvxcore.IntIntMap_empty(self)

    def size(self):
        return _cvxcore.IntIntMap_size(self)

    def swap(self, v):
        return _cvxcore.IntIntMap_swap(self, v)

    def begin(self):
        return _cvxcore.IntIntMap_begin(self)

    def end(self):
        return _cvxcore.IntIntMap_end(self)

    def rbegin(self):
        return _cvxcore.IntIntMap_rbegin(self)

    def rend(self):
        return _cvxcore.IntIntMap_rend(self)

    def clear(self):
        return _cvxcore.IntIntMap_clear(self)

    def get_allocator(self):
        return _cvxcore.IntIntMap_get_allocator(self)

    def count(self, x):
        return _cvxcore.IntIntMap_count(self, x)

    def erase(self, *args):
        return _cvxcore.IntIntMap_erase(self, *args)

    def find(self, x):
        return _cvxcore.IntIntMap_find(self, x)

    def lower_bound(self, x):
        return _cvxcore.IntIntMap_lower_bound(self, x)

    def upper_bound(self, x):
        return _cvxcore.IntIntMap_upper_bound(self, x)
    __swig_destroy__ = _cvxcore.delete_IntIntMap

# Register IntIntMap in _cvxcore:
_cvxcore.IntIntMap_swigregister(IntIntMap)

class LinOpVector:
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _cvxcore.LinOpVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _cvxcore.LinOpVector___nonzero__(self)

    def __bool__(self):
        return _cvxcore.LinOpVector___bool__(self)

    def __len__(self):
        return _cvxcore.LinOpVector___len__(self)

    def __getslice__(self, i, j):
        return _cvxcore.LinOpVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _cvxcore.LinOpVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _cvxcore.LinOpVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _cvxcore.LinOpVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _cvxcore.LinOpVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _cvxcore.LinOpVector___setitem__(self, *args)

    def pop(self):
        return _cvxcore.LinOpVector_pop(self)

    def append(self, x):
        return _cvxcore.LinOpVector_append(self, x)

    def empty(self):
        return _cvxcore.LinOpVector_empty(self)

    def size(self):
        return _cvxcore.LinOpVector_size(self)

    def swap(self, v):
        return _cvxcore.LinOpVector_swap(self, v)

    def begin(self):
        return _cvxcore.LinOpVector_begin(self)

    def end(self):
        return _cvxcore.LinOpVector_end(self)

    def rbegin(self):
        return _cvxcore.LinOpVector_rbegin(self)

    def rend(self):
        return _cvxcore.LinOpVector_rend(self)

    def clear(self):
        return _cvxcore.LinOpVector_clear(self)

    def get_allocator(self):
        return _cvxcore.LinOpVector_get_allocator(self)

    def pop_back(self):
        return _cvxcore.LinOpVector_pop_back(self)

    def erase(self, *args):
        return _cvxcore.LinOpVector_erase(self, *args)

    def __init__(self, *args) -> None:
        _cvxcore.LinOpVector_swiginit(self, _cvxcore.new_LinOpVector(*args))

    def push_back(self, x):
        return _cvxcore.LinOpVector_push_back(self, x)

    def front(self):
        return _cvxcore.LinOpVector_front(self)

    def back(self):
        return _cvxcore.LinOpVector_back(self)

    def assign(self, n, x):
        return _cvxcore.LinOpVector_assign(self, n, x)

    def resize(self, *args):
        return _cvxcore.LinOpVector_resize(self, *args)

    def insert(self, *args):
        return _cvxcore.LinOpVector_insert(self, *args)

    def reserve(self, n):
        return _cvxcore.LinOpVector_reserve(self, n)

    def capacity(self):
        return _cvxcore.LinOpVector_capacity(self)
    __swig_destroy__ = _cvxcore.delete_LinOpVector

# Register LinOpVector in _cvxcore:
_cvxcore.LinOpVector_swigregister(LinOpVector)

class ConstLinOpVector:
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _cvxcore.ConstLinOpVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _cvxcore.ConstLinOpVector___nonzero__(self)

    def __bool__(self):
        return _cvxcore.ConstLinOpVector___bool__(self)

    def __len__(self):
        return _cvxcore.ConstLinOpVector___len__(self)

    def __getslice__(self, i, j):
        return _cvxcore.ConstLinOpVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _cvxcore.ConstLinOpVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _cvxcore.ConstLinOpVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _cvxcore.ConstLinOpVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _cvxcore.ConstLinOpVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _cvxcore.ConstLinOpVector___setitem__(self, *args)

    def pop(self):
        return _cvxcore.ConstLinOpVector_pop(self)

    def append(self, x):
        return _cvxcore.ConstLinOpVector_append(self, x)

    def empty(self):
        return _cvxcore.ConstLinOpVector_empty(self)

    def size(self):
        return _cvxcore.ConstLinOpVector_size(self)

    def swap(self, v):
        return _cvxcore.ConstLinOpVector_swap(self, v)

    def begin(self):
        return _cvxcore.ConstLinOpVector_begin(self)

    def end(self):
        return _cvxcore.ConstLinOpVector_end(self)

    def rbegin(self):
        return _cvxcore.ConstLinOpVector_rbegin(self)

    def rend(self):
        return _cvxcore.ConstLinOpVector_rend(self)

    def clear(self):
        return _cvxcore.ConstLinOpVector_clear(self)

    def get_allocator(self):
        return _cvxcore.ConstLinOpVector_get_allocator(self)

    def pop_back(self):
        return _cvxcore.ConstLinOpVector_pop_back(self)

    def erase(self, *args):
        return _cvxcore.ConstLinOpVector_erase(self, *args)

    def __init__(self, *args) -> None:
        _cvxcore.ConstLinOpVector_swiginit(self, _cvxcore.new_ConstLinOpVector(*args))

    def push_back(self, x):
        return _cvxcore.ConstLinOpVector_push_back(self, x)

    def front(self):
        return _cvxcore.ConstLinOpVector_front(self)

    def back(self):
        return _cvxcore.ConstLinOpVector_back(self)

    def assign(self, n, x):
        return _cvxcore.ConstLinOpVector_assign(self, n, x)

    def resize(self, *args):
        return _cvxcore.ConstLinOpVector_resize(self, *args)

    def insert(self, *args):
        return _cvxcore.ConstLinOpVector_insert(self, *args)

    def reserve(self, n):
        return _cvxcore.ConstLinOpVector_reserve(self, n)

    def capacity(self):
        return _cvxcore.ConstLinOpVector_capacity(self)
    __swig_destroy__ = _cvxcore.delete_ConstLinOpVector

# Register ConstLinOpVector in _cvxcore:
_cvxcore.ConstLinOpVector_swigregister(ConstLinOpVector)


def build_matrix(*args):
    return _cvxcore.build_matrix(*args)
