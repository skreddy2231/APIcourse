# {'artifacts': [{'scanner_count': 0}, {'scanner_match': 0}]}
import json

# o/p: action_results[data][artifacts][scanner_match value]
data = [
    {
        "asset_id": 49,
        "status": "success",
        "name": "de1",
        "app": "CCid",
        "action_results": [
            {
                "status": "success",
                "data": [
                    {
                        "report": {
                            "status": {
                                "origin": "sa",
                                "status": "Up.",
                                "sha1": "4a",
                                "sample_started_at": 159,
                                "running_on": "mt",
                                "ran": True,
                                "auto": True,
                                "vm": "w"
                            },
                            "artifacts": {
                                "1": {
                                    "size": 599518,
                                    "mime-type": "applic=binary",
                                    "antivirus": {
                                        "reversing_labs": {
                                            "status": "UNKNOWN",
                                            "scanner_count": 0,
                                            "scanner_match": 0,
                                            "threat_name": "",
                                            "query_hash": {
                                                "sha256": "029"
                                            },
                                            "last_seen": "0001-01-01T00:00:00Z"
                                        }
                                    },
                                    "entropy": 7.9870740440306
                                },
                                "10": {
                                    "size": 599518,
                                    "mime-type": "applic=binary",
                                    "antivirus": {
                                        "reversing_labs": {
                                            "status": "UNKNOWN",
                                            "scanner_count": 0,
                                            "scanner_match": 0,
                                            "threat_name": "",
                                            "query_hash": {
                                                "sha256": "d38"
                                            },
                                            "last_seen": "0001-01-01T00:00:00Z"
                                        }
                                    },
                                    "entropy": 1
                                }
                            }
                        }
                    }
                ],
                "app_id": 15
            }
        ]
    }
]

print(type(data[0]["action_results"]))
# data_str = json.dumps(data)    # string
# print(type(data_str))
# print(data_str["action_results"])
# mydict = json.loads(data_str)
# print(type(mydict))
print(data[0]["action_results"])
# for x in mydict["action_results"]:

def str_jsonObj():
    strData = '{"iss_position": {"longit3ude": "25.5810", "latitude": "50.1132"}, "message": "success", "timestamp": 1697355763}'
    print(type(strData))

    strJsonObj = json.loads(strData)  # way to Deserialize data into json obj
    print(type(strJsonObj))
    print(strJsonObj["iss_position"]["latitude"])

