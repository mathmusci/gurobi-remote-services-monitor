# coding: utf-8

"""
    Gurobi Remote Services API

    The Gurobi Remote Services is used to control a compute  node  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from grb_rs_monitor.api_client.swagger_client.configuration import Configuration


class JobBarrierInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'primobj': 'float',
        'dualobj': 'float',
        'priminf': 'float',
        'dualinf': 'float',
        'compl': 'float'
    }

    attribute_map = {
        'primobj': 'primobj',
        'dualobj': 'dualobj',
        'priminf': 'priminf',
        'dualinf': 'dualinf',
        'compl': 'compl'
    }

    def __init__(self, primobj=None, dualobj=None, priminf=None, dualinf=None, compl=None, _configuration=None):  # noqa: E501
        """JobBarrierInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._primobj = None
        self._dualobj = None
        self._priminf = None
        self._dualinf = None
        self._compl = None
        self.discriminator = None

        if primobj is not None:
            self.primobj = primobj
        if dualobj is not None:
            self.dualobj = dualobj
        if priminf is not None:
            self.priminf = priminf
        if dualinf is not None:
            self.dualinf = dualinf
        if compl is not None:
            self.compl = compl

    @property
    def primobj(self):
        """Gets the primobj of this JobBarrierInfo.  # noqa: E501

        Primal objective value  # noqa: E501

        :return: The primobj of this JobBarrierInfo.  # noqa: E501
        :rtype: float
        """
        return self._primobj

    @primobj.setter
    def primobj(self, primobj):
        """Sets the primobj of this JobBarrierInfo.

        Primal objective value  # noqa: E501

        :param primobj: The primobj of this JobBarrierInfo.  # noqa: E501
        :type: float
        """

        self._primobj = primobj

    @property
    def dualobj(self):
        """Gets the dualobj of this JobBarrierInfo.  # noqa: E501

        Dual objective value   # noqa: E501

        :return: The dualobj of this JobBarrierInfo.  # noqa: E501
        :rtype: float
        """
        return self._dualobj

    @dualobj.setter
    def dualobj(self, dualobj):
        """Sets the dualobj of this JobBarrierInfo.

        Dual objective value   # noqa: E501

        :param dualobj: The dualobj of this JobBarrierInfo.  # noqa: E501
        :type: float
        """

        self._dualobj = dualobj

    @property
    def priminf(self):
        """Gets the priminf of this JobBarrierInfo.  # noqa: E501

        Primal infeasibility  # noqa: E501

        :return: The priminf of this JobBarrierInfo.  # noqa: E501
        :rtype: float
        """
        return self._priminf

    @priminf.setter
    def priminf(self, priminf):
        """Sets the priminf of this JobBarrierInfo.

        Primal infeasibility  # noqa: E501

        :param priminf: The priminf of this JobBarrierInfo.  # noqa: E501
        :type: float
        """

        self._priminf = priminf

    @property
    def dualinf(self):
        """Gets the dualinf of this JobBarrierInfo.  # noqa: E501

        Dual infeasibility  # noqa: E501

        :return: The dualinf of this JobBarrierInfo.  # noqa: E501
        :rtype: float
        """
        return self._dualinf

    @dualinf.setter
    def dualinf(self, dualinf):
        """Sets the dualinf of this JobBarrierInfo.

        Dual infeasibility  # noqa: E501

        :param dualinf: The dualinf of this JobBarrierInfo.  # noqa: E501
        :type: float
        """

        self._dualinf = dualinf

    @property
    def compl(self):
        """Gets the compl of this JobBarrierInfo.  # noqa: E501

        Complementarity violation  # noqa: E501

        :return: The compl of this JobBarrierInfo.  # noqa: E501
        :rtype: float
        """
        return self._compl

    @compl.setter
    def compl(self, compl):
        """Sets the compl of this JobBarrierInfo.

        Complementarity violation  # noqa: E501

        :param compl: The compl of this JobBarrierInfo.  # noqa: E501
        :type: float
        """

        self._compl = compl

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(JobBarrierInfo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, JobBarrierInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JobBarrierInfo):
            return True

        return self.to_dict() != other.to_dict()