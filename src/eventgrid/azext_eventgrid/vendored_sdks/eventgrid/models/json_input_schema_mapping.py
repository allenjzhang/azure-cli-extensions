# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .input_schema_mapping import InputSchemaMapping


class JsonInputSchemaMapping(InputSchemaMapping):
    """This enables publishing to Event Grid using a custom input schema. This can
    be used to map properties from a custom input JSON schema to the Event Grid
    event schema.

    All required parameters must be populated in order to send to Azure.

    :param input_schema_mapping_type: Required. Constant filled by server.
    :type input_schema_mapping_type: str
    :param id: The mapping information for the Id property of the Event Grid
     Event.
    :type id: ~microsoft.azure.management.eventgrid.models.JsonField
    :param topic: The mapping information for the Topic property of the Event
     Grid Event.
    :type topic: ~microsoft.azure.management.eventgrid.models.JsonField
    :param event_time: The mapping information for the EventTime property of
     the Event Grid Event.
    :type event_time: ~microsoft.azure.management.eventgrid.models.JsonField
    :param event_type: The mapping information for the EventType property of
     the Event Grid Event.
    :type event_type:
     ~microsoft.azure.management.eventgrid.models.JsonFieldWithDefault
    :param subject: The mapping information for the Subject property of the
     Event Grid Event.
    :type subject:
     ~microsoft.azure.management.eventgrid.models.JsonFieldWithDefault
    :param data_version: The mapping information for the DataVersion property
     of the Event Grid Event.
    :type data_version:
     ~microsoft.azure.management.eventgrid.models.JsonFieldWithDefault
    """

    _validation = {
        'input_schema_mapping_type': {'required': True},
    }

    _attribute_map = {
        'input_schema_mapping_type': {'key': 'inputSchemaMappingType', 'type': 'str'},
        'id': {'key': 'properties.id', 'type': 'JsonField'},
        'topic': {'key': 'properties.topic', 'type': 'JsonField'},
        'event_time': {'key': 'properties.eventTime', 'type': 'JsonField'},
        'event_type': {'key': 'properties.eventType', 'type': 'JsonFieldWithDefault'},
        'subject': {'key': 'properties.subject', 'type': 'JsonFieldWithDefault'},
        'data_version': {'key': 'properties.dataVersion', 'type': 'JsonFieldWithDefault'},
    }

    def __init__(self, **kwargs):
        super(JsonInputSchemaMapping, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.topic = kwargs.get('topic', None)
        self.event_time = kwargs.get('event_time', None)
        self.event_type = kwargs.get('event_type', None)
        self.subject = kwargs.get('subject', None)
        self.data_version = kwargs.get('data_version', None)
        self.input_schema_mapping_type = 'Json'
