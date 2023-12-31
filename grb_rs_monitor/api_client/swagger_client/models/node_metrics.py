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


class NodeMetrics(object):
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
        'nb_running_jobs': 'int',
        'nb_queued_jobs': 'int',
        'nb_recent_jobs': 'int',
        'processed_job_counter': 'int',
        'idle_time': 'int',
        'memory': 'float',
        'cpu': 'float'
    }

    attribute_map = {
        'nb_running_jobs': 'nbRunningJobs',
        'nb_queued_jobs': 'nbQueuedJobs',
        'nb_recent_jobs': 'nbRecentJobs',
        'processed_job_counter': 'processedJobCounter',
        'idle_time': 'idleTime',
        'memory': 'memory',
        'cpu': 'cpu'
    }

    def __init__(self, nb_running_jobs=None, nb_queued_jobs=None, nb_recent_jobs=None, processed_job_counter=None, idle_time=None, memory=None, cpu=None, _configuration=None):  # noqa: E501
        """NodeMetrics - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._nb_running_jobs = None
        self._nb_queued_jobs = None
        self._nb_recent_jobs = None
        self._processed_job_counter = None
        self._idle_time = None
        self._memory = None
        self._cpu = None
        self.discriminator = None

        if nb_running_jobs is not None:
            self.nb_running_jobs = nb_running_jobs
        if nb_queued_jobs is not None:
            self.nb_queued_jobs = nb_queued_jobs
        if nb_recent_jobs is not None:
            self.nb_recent_jobs = nb_recent_jobs
        if processed_job_counter is not None:
            self.processed_job_counter = processed_job_counter
        if idle_time is not None:
            self.idle_time = idle_time
        if memory is not None:
            self.memory = memory
        if cpu is not None:
            self.cpu = cpu

    @property
    def nb_running_jobs(self):
        """Gets the nb_running_jobs of this NodeMetrics.  # noqa: E501

        Number of jobs running  # noqa: E501

        :return: The nb_running_jobs of this NodeMetrics.  # noqa: E501
        :rtype: int
        """
        return self._nb_running_jobs

    @nb_running_jobs.setter
    def nb_running_jobs(self, nb_running_jobs):
        """Sets the nb_running_jobs of this NodeMetrics.

        Number of jobs running  # noqa: E501

        :param nb_running_jobs: The nb_running_jobs of this NodeMetrics.  # noqa: E501
        :type: int
        """

        self._nb_running_jobs = nb_running_jobs

    @property
    def nb_queued_jobs(self):
        """Gets the nb_queued_jobs of this NodeMetrics.  # noqa: E501

        Number of jobs in queue  # noqa: E501

        :return: The nb_queued_jobs of this NodeMetrics.  # noqa: E501
        :rtype: int
        """
        return self._nb_queued_jobs

    @nb_queued_jobs.setter
    def nb_queued_jobs(self, nb_queued_jobs):
        """Sets the nb_queued_jobs of this NodeMetrics.

        Number of jobs in queue  # noqa: E501

        :param nb_queued_jobs: The nb_queued_jobs of this NodeMetrics.  # noqa: E501
        :type: int
        """

        self._nb_queued_jobs = nb_queued_jobs

    @property
    def nb_recent_jobs(self):
        """Gets the nb_recent_jobs of this NodeMetrics.  # noqa: E501

        Number of recent jobs in the short term history  # noqa: E501

        :return: The nb_recent_jobs of this NodeMetrics.  # noqa: E501
        :rtype: int
        """
        return self._nb_recent_jobs

    @nb_recent_jobs.setter
    def nb_recent_jobs(self, nb_recent_jobs):
        """Sets the nb_recent_jobs of this NodeMetrics.

        Number of recent jobs in the short term history  # noqa: E501

        :param nb_recent_jobs: The nb_recent_jobs of this NodeMetrics.  # noqa: E501
        :type: int
        """

        self._nb_recent_jobs = nb_recent_jobs

    @property
    def processed_job_counter(self):
        """Gets the processed_job_counter of this NodeMetrics.  # noqa: E501

        Persistent counter of processed jobs [0,4294967295], will cycle  # noqa: E501

        :return: The processed_job_counter of this NodeMetrics.  # noqa: E501
        :rtype: int
        """
        return self._processed_job_counter

    @processed_job_counter.setter
    def processed_job_counter(self, processed_job_counter):
        """Sets the processed_job_counter of this NodeMetrics.

        Persistent counter of processed jobs [0,4294967295], will cycle  # noqa: E501

        :param processed_job_counter: The processed_job_counter of this NodeMetrics.  # noqa: E501
        :type: int
        """

        self._processed_job_counter = processed_job_counter

    @property
    def idle_time(self):
        """Gets the idle_time of this NodeMetrics.  # noqa: E501

        Idle time since the last job execution (in minutes)  # noqa: E501

        :return: The idle_time of this NodeMetrics.  # noqa: E501
        :rtype: int
        """
        return self._idle_time

    @idle_time.setter
    def idle_time(self, idle_time):
        """Sets the idle_time of this NodeMetrics.

        Idle time since the last job execution (in minutes)  # noqa: E501

        :param idle_time: The idle_time of this NodeMetrics.  # noqa: E501
        :type: int
        """

        self._idle_time = idle_time

    @property
    def memory(self):
        """Gets the memory of this NodeMetrics.  # noqa: E501

        Percentage of memory currently used on the machine  # noqa: E501

        :return: The memory of this NodeMetrics.  # noqa: E501
        :rtype: float
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this NodeMetrics.

        Percentage of memory currently used on the machine  # noqa: E501

        :param memory: The memory of this NodeMetrics.  # noqa: E501
        :type: float
        """

        self._memory = memory

    @property
    def cpu(self):
        """Gets the cpu of this NodeMetrics.  # noqa: E501

        Percentage of CPU currently used on the machine  # noqa: E501

        :return: The cpu of this NodeMetrics.  # noqa: E501
        :rtype: float
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this NodeMetrics.

        Percentage of CPU currently used on the machine  # noqa: E501

        :param cpu: The cpu of this NodeMetrics.  # noqa: E501
        :type: float
        """

        self._cpu = cpu

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
        if issubclass(NodeMetrics, dict):
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
        if not isinstance(other, NodeMetrics):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NodeMetrics):
            return True

        return self.to_dict() != other.to_dict()
