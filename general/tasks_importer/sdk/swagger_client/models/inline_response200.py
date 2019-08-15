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


class InlineResponse200(object):
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
        'description': 'str',
        'name': 'str',
        'part_of': 'str',
        'platform': 'str'
    }

    attribute_map = {
        'description': 'description',
        'name': 'name',
        'part_of': 'part_of',
        'platform': 'platform'
    }

    def __init__(self, description=None, name=None, part_of=None, platform=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._name = None
        self._part_of = None
        self._platform = None
        self.discriminator = None

        self.description = description
        self.name = name
        self.part_of = part_of
        self.platform = platform

    @property
    def description(self):
        """Gets the description of this InlineResponse200.  # noqa: E501


        :return: The description of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineResponse200.


        :param description: The description of this InlineResponse200.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def name(self):
        """Gets the name of this InlineResponse200.  # noqa: E501


        :return: The name of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse200.


        :param name: The name of this InlineResponse200.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def part_of(self):
        """Gets the part_of of this InlineResponse200.  # noqa: E501

        The ID of the project that this activity is part of  # noqa: E501

        :return: The part_of of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._part_of

    @part_of.setter
    def part_of(self, part_of):
        """Sets the part_of of this InlineResponse200.

        The ID of the project that this activity is part of  # noqa: E501

        :param part_of: The part_of of this InlineResponse200.  # noqa: E501
        :type: str
        """
        if part_of is None:
            raise ValueError("Invalid value for `part_of`, must not be `None`")  # noqa: E501

        self._part_of = part_of

    @property
    def platform(self):
        """Gets the platform of this InlineResponse200.  # noqa: E501


        :return: The platform of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this InlineResponse200.


        :param platform: The platform of this InlineResponse200.  # noqa: E501
        :type: str
        """
        if platform is None:
            raise ValueError("Invalid value for `platform`, must not be `None`")  # noqa: E501
        allowed_values = ["Desktop", "Mobile", "Both"]  # noqa: E501
        if platform not in allowed_values:
            raise ValueError(
                "Invalid value for `platform` ({0}), must be one of {1}"  # noqa: E501
                .format(platform, allowed_values)
            )

        self._platform = platform

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
        if not isinstance(other, InlineResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other