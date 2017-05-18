#
# Validator for "snmp" Test
#

from pscheduler import json_validate

def spec_is_valid(json):
# QUESTION: Separate schema for each version
    if json['version'] == '2c':
        schema = {
            "local": {
                "VersionNumber": {
                    "type": "string",
                    "enum": [ "1", "2c", "3"]
	            }
                "OptionType": {
                    "type": "string",
                    "enum": [ "get", "walk"]
                    }
	        },
            "type": "object",
            "properties": {
                "schema":       { "$ref": "#/pScheduler/Cardinal" },
                "host":         { "$ref": "#/pScheduler/Host" },
                "host-node":    { "$ref": "#/pScheduler/Host" },
                "dest":         { "$ref": "#/pScheduler/Host" },
                "version":      { "$ref": "#/local/VersionNumber"},
                "community":    { "$ref": "#/pScheduler/String"},
                "oid":          { "$ref": "#/pScheduler/String"},
                "op":           { "$ref": "#/local/OptionType"},
                "timeout":      { "$ref": "#/pScheduler/Duration" },
                },
            "required": [
                "version",
                "community",
                "dest",
                "op",
                ]
            }
            
    if json['version'] == '3':
        pass

    return json_validate(json, schema)


def result_is_valid(json):
    schema = {
        "type": "object",
        "properties": {
            "schema":     { "$ref": "#/pScheduler/Cardinal" },
            "succeeded":  { "$ref": "#/pScheduler/Boolean" },
            "time":   { "$ref": "#/pScheduler/Duration" },
            "data":       { "$ref": "#/pScheduler/String"},
            },
        "required": [
            "schema",
            "succeeded",
            "data",
            "time",
            ]
        }
    return json_validate(json, schema)

def limit_is_valid(json):
    schema = {
        "type": "object",
        "properties": {
            "schema": { "$ref": "#/pScheduler/Cardinal" },
            "dest":         { "$ref": "#/pScheduler/Limit/String" },
            "version":      { "$ref": "#/pScheduler/String"},
            "community":    { "$ref": "#/pScheduler/String"},
            "oid":          { "$ref": "#/pScheduler/String"},
            "op":           { "$ref": "#/pScheduler/String"},
        },
        "additionalProperties": False
        }

    return json_validate(json, schema)
