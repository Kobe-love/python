# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.32
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V1beta1BasicDevice(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'attributes': 'dict(str, V1beta1DeviceAttribute)',
        'capacity': 'dict(str, V1beta1DeviceCapacity)'
    }

    attribute_map = {
        'attributes': 'attributes',
        'capacity': 'capacity'
    }

    def __init__(self, attributes=None, capacity=None, local_vars_configuration=None):  # noqa: E501
        """V1beta1BasicDevice - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._attributes = None
        self._capacity = None
        self.discriminator = None

        if attributes is not None:
            self.attributes = attributes
        if capacity is not None:
            self.capacity = capacity

    @property
    def attributes(self):
        """Gets the attributes of this V1beta1BasicDevice.  # noqa: E501

        Attributes defines the set of attributes for this device. The name of each attribute must be unique in that set.  The maximum number of attributes and capacities combined is 32.  # noqa: E501

        :return: The attributes of this V1beta1BasicDevice.  # noqa: E501
        :rtype: dict(str, V1beta1DeviceAttribute)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this V1beta1BasicDevice.

        Attributes defines the set of attributes for this device. The name of each attribute must be unique in that set.  The maximum number of attributes and capacities combined is 32.  # noqa: E501

        :param attributes: The attributes of this V1beta1BasicDevice.  # noqa: E501
        :type: dict(str, V1beta1DeviceAttribute)
        """

        self._attributes = attributes

    @property
    def capacity(self):
        """Gets the capacity of this V1beta1BasicDevice.  # noqa: E501

        Capacity defines the set of capacities for this device. The name of each capacity must be unique in that set.  The maximum number of attributes and capacities combined is 32.  # noqa: E501

        :return: The capacity of this V1beta1BasicDevice.  # noqa: E501
        :rtype: dict(str, V1beta1DeviceCapacity)
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this V1beta1BasicDevice.

        Capacity defines the set of capacities for this device. The name of each capacity must be unique in that set.  The maximum number of attributes and capacities combined is 32.  # noqa: E501

        :param capacity: The capacity of this V1beta1BasicDevice.  # noqa: E501
        :type: dict(str, V1beta1DeviceCapacity)
        """

        self._capacity = capacity

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, V1beta1BasicDevice):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta1BasicDevice):
            return True

        return self.to_dict() != other.to_dict()
