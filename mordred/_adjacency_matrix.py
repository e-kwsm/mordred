import numpy as np

from ._base import Descriptor
from ._common import AdjacencyMatrix as A
from ._matrix_attributes import get_method, methods


class AdjacencyMatrix(Descriptor):
    r"""adjacency matrix descriptor.

    :type type: :py:class:`str`
    :param type: :ref:`matrix_aggregating_methods`
    """

    explicit_hydrogens = False

    @classmethod
    def preset(cls):
        return map(cls, methods)

    def __str__(self):
        return '{}_A'.format(self._type.__name__)

    __slots__ = ('_type',)

    def __reduce_ex__(self, version):
        return self.__class__, (self._type,)

    def __init__(self, type='SpMax'):
        self._type = get_method(type)

    def dependencies(self):
        return dict(
            result=self._type(
                A(self.explicit_hydrogens),
                self.explicit_hydrogens,
                self.gasteiger_charges,
                self.kekulize,
            )
        )

    def calculate(self, mol, result):
        return result

    rtype = float