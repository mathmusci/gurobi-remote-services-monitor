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


class OptimizationComplete(object):
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
        'status': 'int',
        'error': 'int',
        'errormsg': 'str'
    }

    attribute_map = {
        'status': 'status',
        'error': 'error',
        'errormsg': 'errormsg'
    }

    def __init__(self, status=None, error=None, errormsg=None, _configuration=None):  # noqa: E501
        """OptimizationComplete - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._status = None
        self._error = None
        self._errormsg = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if error is not None:
            self.error = error
        if errormsg is not None:
            self.errormsg = errormsg

    @property
    def status(self):
        """Gets the status of this OptimizationComplete.  # noqa: E501

        Optimization status code  # noqa: E501

        :return: The status of this OptimizationComplete.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OptimizationComplete.

        Optimization status code  # noqa: E501

        :param status: The status of this OptimizationComplete.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def error(self):
        """Gets the error of this OptimizationComplete.  # noqa: E501

        Error code  # noqa: E501

        :return: The error of this OptimizationComplete.  # noqa: E501
        :rtype: int
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this OptimizationComplete.

        Error code  # noqa: E501

        :param error: The error of this OptimizationComplete.  # noqa: E501
        :type: int
        """

        self._error = error

    @property
    def errormsg(self):
        """Gets the errormsg of this OptimizationComplete.  # noqa: E501

        Error message  # noqa: E501

        :return: The errormsg of this OptimizationComplete.  # noqa: E501
        :rtype: str
        """
        return self._errormsg

    @errormsg.setter
    def errormsg(self, errormsg):
        """Sets the errormsg of this OptimizationComplete.

        Error message  # noqa: E501

        :param errormsg: The errormsg of this OptimizationComplete.  # noqa: E501
        :type: str
        """

        self._errormsg = errormsg

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
        if issubclass(OptimizationComplete, dict):
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
        if not isinstance(other, OptimizationComplete):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OptimizationComplete):
            return True

        return self.to_dict() != other.to_dict()
