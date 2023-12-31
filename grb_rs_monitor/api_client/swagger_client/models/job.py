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


class Job(object):
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
        'id': 'str',
        'address': 'str',
        'status': 'JobStatus',
        'error_code': 'float',
        'error_msg': 'str',
        'started_at': 'float',
        'queued_at': 'float',
        'queue_index': 'float',
        'ended_at': 'float',
        'solve_status': 'JobSolveStatus',
        'properties': 'JobProperties',
        'model_info': 'JobModelInfo',
        'mip_info': 'JobMipInfo',
        'simplex_info': 'JobSimplexInfo',
        'barrier_info': 'JobBarrierInfo',
        'tuning_info': 'JobTuningInfo',
        'optimization_status': 'OptimizationComplete'
    }

    attribute_map = {
        'id': 'id',
        'address': 'address',
        'status': 'status',
        'error_code': 'errorCode',
        'error_msg': 'errorMsg',
        'started_at': 'startedAt',
        'queued_at': 'queuedAt',
        'queue_index': 'queueIndex',
        'ended_at': 'endedAt',
        'solve_status': 'solveStatus',
        'properties': 'properties',
        'model_info': 'modelInfo',
        'mip_info': 'mipInfo',
        'simplex_info': 'simplexInfo',
        'barrier_info': 'barrierInfo',
        'tuning_info': 'tuningInfo',
        'optimization_status': 'optimizationStatus'
    }

    def __init__(self, id=None, address=None, status=None, error_code=None, error_msg=None, started_at=None, queued_at=None, queue_index=None, ended_at=None, solve_status=None, properties=None, model_info=None, mip_info=None, simplex_info=None, barrier_info=None, tuning_info=None, optimization_status=None, _configuration=None):  # noqa: E501
        """Job - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._address = None
        self._status = None
        self._error_code = None
        self._error_msg = None
        self._started_at = None
        self._queued_at = None
        self._queue_index = None
        self._ended_at = None
        self._solve_status = None
        self._properties = None
        self._model_info = None
        self._mip_info = None
        self._simplex_info = None
        self._barrier_info = None
        self._tuning_info = None
        self._optimization_status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if address is not None:
            self.address = address
        if status is not None:
            self.status = status
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if started_at is not None:
            self.started_at = started_at
        if queued_at is not None:
            self.queued_at = queued_at
        if queue_index is not None:
            self.queue_index = queue_index
        if ended_at is not None:
            self.ended_at = ended_at
        if solve_status is not None:
            self.solve_status = solve_status
        if properties is not None:
            self.properties = properties
        if model_info is not None:
            self.model_info = model_info
        if mip_info is not None:
            self.mip_info = mip_info
        if simplex_info is not None:
            self.simplex_info = simplex_info
        if barrier_info is not None:
            self.barrier_info = barrier_info
        if tuning_info is not None:
            self.tuning_info = tuning_info
        if optimization_status is not None:
            self.optimization_status = optimization_status

    @property
    def id(self):
        """Gets the id of this Job.  # noqa: E501

        the unique job id  # noqa: E501

        :return: The id of this Job.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Job.

        the unique job id  # noqa: E501

        :param id: The id of this Job.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def address(self):
        """Gets the address of this Job.  # noqa: E501

        server address  # noqa: E501

        :return: The address of this Job.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Job.

        server address  # noqa: E501

        :param address: The address of this Job.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def status(self):
        """Gets the status of this Job.  # noqa: E501


        :return: The status of this Job.  # noqa: E501
        :rtype: JobStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Job.


        :param status: The status of this Job.  # noqa: E501
        :type: JobStatus
        """

        self._status = status

    @property
    def error_code(self):
        """Gets the error_code of this Job.  # noqa: E501

        Error code  # noqa: E501

        :return: The error_code of this Job.  # noqa: E501
        :rtype: float
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this Job.

        Error code  # noqa: E501

        :param error_code: The error_code of this Job.  # noqa: E501
        :type: float
        """

        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this Job.  # noqa: E501

        Error message  # noqa: E501

        :return: The error_msg of this Job.  # noqa: E501
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this Job.

        Error message  # noqa: E501

        :param error_msg: The error_msg of this Job.  # noqa: E501
        :type: str
        """

        self._error_msg = error_msg

    @property
    def started_at(self):
        """Gets the started_at of this Job.  # noqa: E501

        Job start timestamp  # noqa: E501

        :return: The started_at of this Job.  # noqa: E501
        :rtype: float
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this Job.

        Job start timestamp  # noqa: E501

        :param started_at: The started_at of this Job.  # noqa: E501
        :type: float
        """

        self._started_at = started_at

    @property
    def queued_at(self):
        """Gets the queued_at of this Job.  # noqa: E501

        Job queue timestamp  # noqa: E501

        :return: The queued_at of this Job.  # noqa: E501
        :rtype: float
        """
        return self._queued_at

    @queued_at.setter
    def queued_at(self, queued_at):
        """Sets the queued_at of this Job.

        Job queue timestamp  # noqa: E501

        :param queued_at: The queued_at of this Job.  # noqa: E501
        :type: float
        """

        self._queued_at = queued_at

    @property
    def queue_index(self):
        """Gets the queue_index of this Job.  # noqa: E501

        Job index in the queue  # noqa: E501

        :return: The queue_index of this Job.  # noqa: E501
        :rtype: float
        """
        return self._queue_index

    @queue_index.setter
    def queue_index(self, queue_index):
        """Sets the queue_index of this Job.

        Job index in the queue  # noqa: E501

        :param queue_index: The queue_index of this Job.  # noqa: E501
        :type: float
        """

        self._queue_index = queue_index

    @property
    def ended_at(self):
        """Gets the ended_at of this Job.  # noqa: E501

        Job end stimestamp  # noqa: E501

        :return: The ended_at of this Job.  # noqa: E501
        :rtype: float
        """
        return self._ended_at

    @ended_at.setter
    def ended_at(self, ended_at):
        """Sets the ended_at of this Job.

        Job end stimestamp  # noqa: E501

        :param ended_at: The ended_at of this Job.  # noqa: E501
        :type: float
        """

        self._ended_at = ended_at

    @property
    def solve_status(self):
        """Gets the solve_status of this Job.  # noqa: E501


        :return: The solve_status of this Job.  # noqa: E501
        :rtype: JobSolveStatus
        """
        return self._solve_status

    @solve_status.setter
    def solve_status(self, solve_status):
        """Sets the solve_status of this Job.


        :param solve_status: The solve_status of this Job.  # noqa: E501
        :type: JobSolveStatus
        """

        self._solve_status = solve_status

    @property
    def properties(self):
        """Gets the properties of this Job.  # noqa: E501


        :return: The properties of this Job.  # noqa: E501
        :rtype: JobProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Job.


        :param properties: The properties of this Job.  # noqa: E501
        :type: JobProperties
        """

        self._properties = properties

    @property
    def model_info(self):
        """Gets the model_info of this Job.  # noqa: E501


        :return: The model_info of this Job.  # noqa: E501
        :rtype: JobModelInfo
        """
        return self._model_info

    @model_info.setter
    def model_info(self, model_info):
        """Sets the model_info of this Job.


        :param model_info: The model_info of this Job.  # noqa: E501
        :type: JobModelInfo
        """

        self._model_info = model_info

    @property
    def mip_info(self):
        """Gets the mip_info of this Job.  # noqa: E501


        :return: The mip_info of this Job.  # noqa: E501
        :rtype: JobMipInfo
        """
        return self._mip_info

    @mip_info.setter
    def mip_info(self, mip_info):
        """Sets the mip_info of this Job.


        :param mip_info: The mip_info of this Job.  # noqa: E501
        :type: JobMipInfo
        """

        self._mip_info = mip_info

    @property
    def simplex_info(self):
        """Gets the simplex_info of this Job.  # noqa: E501


        :return: The simplex_info of this Job.  # noqa: E501
        :rtype: JobSimplexInfo
        """
        return self._simplex_info

    @simplex_info.setter
    def simplex_info(self, simplex_info):
        """Sets the simplex_info of this Job.


        :param simplex_info: The simplex_info of this Job.  # noqa: E501
        :type: JobSimplexInfo
        """

        self._simplex_info = simplex_info

    @property
    def barrier_info(self):
        """Gets the barrier_info of this Job.  # noqa: E501


        :return: The barrier_info of this Job.  # noqa: E501
        :rtype: JobBarrierInfo
        """
        return self._barrier_info

    @barrier_info.setter
    def barrier_info(self, barrier_info):
        """Sets the barrier_info of this Job.


        :param barrier_info: The barrier_info of this Job.  # noqa: E501
        :type: JobBarrierInfo
        """

        self._barrier_info = barrier_info

    @property
    def tuning_info(self):
        """Gets the tuning_info of this Job.  # noqa: E501


        :return: The tuning_info of this Job.  # noqa: E501
        :rtype: JobTuningInfo
        """
        return self._tuning_info

    @tuning_info.setter
    def tuning_info(self, tuning_info):
        """Sets the tuning_info of this Job.


        :param tuning_info: The tuning_info of this Job.  # noqa: E501
        :type: JobTuningInfo
        """

        self._tuning_info = tuning_info

    @property
    def optimization_status(self):
        """Gets the optimization_status of this Job.  # noqa: E501


        :return: The optimization_status of this Job.  # noqa: E501
        :rtype: OptimizationComplete
        """
        return self._optimization_status

    @optimization_status.setter
    def optimization_status(self, optimization_status):
        """Sets the optimization_status of this Job.


        :param optimization_status: The optimization_status of this Job.  # noqa: E501
        :type: OptimizationComplete
        """

        self._optimization_status = optimization_status

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
        if issubclass(Job, dict):
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
        if not isinstance(other, Job):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Job):
            return True

        return self.to_dict() != other.to_dict()
