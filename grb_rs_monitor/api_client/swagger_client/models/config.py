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


class Config(object):
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
        'version': 'str',
        'job_limit': 'int',
        'distributed_limit': 'int',
        'cs_enabled': 'bool'
    }

    attribute_map = {
        'version': 'version',
        'job_limit': 'jobLimit',
        'distributed_limit': 'distributed Limit',
        'cs_enabled': 'csEnabled'
    }

    def __init__(self, version=None, job_limit=None, distributed_limit=None, cs_enabled=None, _configuration=None):  # noqa: E501
        """Config - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._version = None
        self._job_limit = None
        self._distributed_limit = None
        self._cs_enabled = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if job_limit is not None:
            self.job_limit = job_limit
        if distributed_limit is not None:
            self.distributed_limit = distributed_limit
        if cs_enabled is not None:
            self.cs_enabled = cs_enabled

    @property
    def version(self):
        """Gets the version of this Config.  # noqa: E501

        Remote Services version  # noqa: E501

        :return: The version of this Config.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Config.

        Remote Services version  # noqa: E501

        :param version: The version of this Config.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def job_limit(self):
        """Gets the job_limit of this Config.  # noqa: E501

        Job limit  # noqa: E501

        :return: The job_limit of this Config.  # noqa: E501
        :rtype: int
        """
        return self._job_limit

    @job_limit.setter
    def job_limit(self, job_limit):
        """Sets the job_limit of this Config.

        Job limit  # noqa: E501

        :param job_limit: The job_limit of this Config.  # noqa: E501
        :type: int
        """

        self._job_limit = job_limit

    @property
    def distributed_limit(self):
        """Gets the distributed_limit of this Config.  # noqa: E501

        Distributed limit  # noqa: E501

        :return: The distributed_limit of this Config.  # noqa: E501
        :rtype: int
        """
        return self._distributed_limit

    @distributed_limit.setter
    def distributed_limit(self, distributed_limit):
        """Sets the distributed_limit of this Config.

        Distributed limit  # noqa: E501

        :param distributed_limit: The distributed_limit of this Config.  # noqa: E501
        :type: int
        """

        self._distributed_limit = distributed_limit

    @property
    def cs_enabled(self):
        """Gets the cs_enabled of this Config.  # noqa: E501

        Indicates if Compute Server is enabled  # noqa: E501

        :return: The cs_enabled of this Config.  # noqa: E501
        :rtype: bool
        """
        return self._cs_enabled

    @cs_enabled.setter
    def cs_enabled(self, cs_enabled):
        """Sets the cs_enabled of this Config.

        Indicates if Compute Server is enabled  # noqa: E501

        :param cs_enabled: The cs_enabled of this Config.  # noqa: E501
        :type: bool
        """

        self._cs_enabled = cs_enabled

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
        if issubclass(Config, dict):
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
        if not isinstance(other, Config):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Config):
            return True

        return self.to_dict() != other.to_dict()
