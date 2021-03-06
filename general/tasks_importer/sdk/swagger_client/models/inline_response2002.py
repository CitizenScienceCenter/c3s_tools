# coding: utf-8

"""
    CCCS

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InlineResponse2002(object):
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
        'filetype': 'str',
        'name': 'str',
        'path': 'str',
        'source_id': 'str'
    }

    attribute_map = {
        'filetype': 'filetype',
        'name': 'name',
        'path': 'path',
        'source_id': 'source_id'
    }

    def __init__(self, filetype=None, name=None, path=None, source_id=None):  # noqa: E501
        """InlineResponse2002 - a model defined in Swagger"""  # noqa: E501

        self._filetype = None
        self._name = None
        self._path = None
        self._source_id = None
        self.discriminator = None

        if filetype is not None:
            self.filetype = filetype
        self.name = name
        self.path = path
        self.source_id = source_id

    @property
    def filetype(self):
        """Gets the filetype of this InlineResponse2002.  # noqa: E501


        :return: The filetype of this InlineResponse2002.  # noqa: E501
        :rtype: str
        """
        return self._filetype

    @filetype.setter
    def filetype(self, filetype):
        """Sets the filetype of this InlineResponse2002.


        :param filetype: The filetype of this InlineResponse2002.  # noqa: E501
        :type: str
        """

        self._filetype = filetype

    @property
    def name(self):
        """Gets the name of this InlineResponse2002.  # noqa: E501

        Name of file  # noqa: E501

        :return: The name of this InlineResponse2002.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse2002.

        Name of file  # noqa: E501

        :param name: The name of this InlineResponse2002.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def path(self):
        """Gets the path of this InlineResponse2002.  # noqa: E501

        Local or remote path  # noqa: E501

        :return: The path of this InlineResponse2002.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this InlineResponse2002.

        Local or remote path  # noqa: E501

        :param path: The path of this InlineResponse2002.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def source_id(self):
        """Gets the source_id of this InlineResponse2002.  # noqa: E501

        The task or project or user it is related to  # noqa: E501

        :return: The source_id of this InlineResponse2002.  # noqa: E501
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this InlineResponse2002.

        The task or project or user it is related to  # noqa: E501

        :param source_id: The source_id of this InlineResponse2002.  # noqa: E501
        :type: str
        """
        if source_id is None:
            raise ValueError("Invalid value for `source_id`, must not be `None`")  # noqa: E501

        self._source_id = source_id

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse2002):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
