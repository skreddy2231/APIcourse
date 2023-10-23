import  json

jsondata = {
    "page": 2,
    "per_page": 6,
    "total": 12,
    "total_pages": 2,
    "data": [
        {
            "id": 7,
            "email": "michael.lawson@reqres.in",
            "first_name": "Michael",
            "last_name": "Lawson",
            "avatar": "https://reqres.in/img/faces/7-image.jpg"
        },
        {
            "id": 8,
            "email": "lindsay.ferguson@reqres.in",
            "first_name": "Lindsay",
            "last_name": "Ferguson",
            "avatar": "https://reqres.in/img/faces/8-image.jpg"
        },
        {
            "id": 9,
            "email": "tobias.funke@reqres.in",
            "first_name": "Tobias",
            "last_name": "Funke",
            "avatar": "https://reqres.in/img/faces/9-image.jpg"
        },
        {
            "id": 10,
            "email": "byron.fields@reqres.in",
            "first_name": "Byron",
            "last_name": "Fields",
            "avatar": "https://reqres.in/img/faces/10-image.jpg"
        },
        {
            "id": 11,
            "email": "george.edwards@reqres.in",
            "first_name": "George",
            "last_name": "Edwards",
            "avatar": "https://reqres.in/img/faces/11-image.jpg"
        },
        {
            "id": 12,
            "email": "rachel.howell@reqres.in",
            "first_name": "Rachel",
            "last_name": "Howell",
            "avatar": "https://reqres.in/img/faces/12-image.jpg"
        }
    ],
    "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
}

list1 = []
dict1 = {}
for i in jsondata["data"]:
    # print(i["id"])
    list1.append(i["id"])
    dict1.update({i["first_name"]: i["id"]})

print("Geneter list:", list1)
print("Generate dictionart", dict1)


data = {
    "type": "video",
    "videoID": "vid001",
    "links": [
        {"type": "video", "videoID": "vid002", "links": []},
        {"type": "video",
         "videoID": "vid003",
         "links": [
             {"type": "video", "videoID": "vid004"},
             {"type": "video", "videoID": "vid005"},
         ]
         },
        {"type": "video", "videoID": "vid006"},
        {"type": "video",
         "videoID": "vid007",
         "links": [
             {"type": "video", "videoID": "vid008", "links": [
                 {"type": "video",
                  "videoID": "vid009",
                  "links": [{"type": "video", "videoID": "vid010"}]
                  }
             ]}
         ]},
    ]
}

mydict2 = {}
mylist2 = []
# print(data.items())




def getjsonIds():
    data2 = {
        'ok': 1.0,
        'result': [
            {
                'total': 142250.0,
                '_id': 'BC'
            },
            {
                'total': 210.88999999999996,
                '_id': 'USD'
            },

            {
                'total': 1065600.0,
                '_id': 'TK'
            }
        ]
    }
    list3 = []
    for item in data2["result"]:
            # print(item)
            for ekey, eval in item.items():
                if ekey == "_id":
                    list3.append(item[ekey])

    print("getjsonIds::", list3)


# getjsonIds()

