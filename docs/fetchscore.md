# Show Current User

Get the details of the currently Authenticated User along with basic
subscription information.

**URL** : `/score`

**Method** : `GET`

**Auth required** : No

**Permissions required** : None

## Success Response

**Code** : `200 OK`

**Content examples**

Fetch score of current game

```json
{
    "frame_scores": {
        "0": {
            "throw": {
                "0": 5,
                "1": 2,
                "2": -1
            },
            "score": 7
        },
        "1": {
            "throw": {
                "0": 2,
                "1": 2,
                "2": -1
            },
            "score": 4
        },
        "2": {
            "throw": {
                "0": 2,
                "1": 2,
                "2": -1
            },
            "score": 4
        },
        "3": {
            "throw": {
                "0": -1,
                "1": -1,
                "2": -1
            },
            "score": -1
        },
        "4": {
            "throw": {
                "0": -1,
                "1": -1,
                "2": -1
            },
            "score": -1
        },
        "5": {
            "throw": {
                "0": -1,
                "1": -1,
                "2": -1
            },
            "score": -1
        },
        "6": {
            "throw": {
                "0": -1,
                "1": -1,
                "2": -1
            },
            "score": -1
        },
        "7": {
            "throw": {
                "0": -1,
                "1": -1,
                "2": -1
            },
            "score": -1
        },
        "8": {
            "throw": {
                "0": -1,
                "1": -1,
                "2": -1
            },
            "score": -1
        },
        "9": {
            "throw": {
                "0": -1,
                "1": -1,
                "2": -1
            },
            "score": -1
        }
    },
    "running_score": 15
}
```

## Assumption

*  -1 indicates, throw has not been used for particular frame
* -1 in score indicates score hasn't initialized, or the last frame had strike or spare and waiting on current frame to add new score. 


## Error Responses

**Condition** : If game has not started, and GET /score api is being called

**Code** : `400 Bad Request`


**Content** : 
```json
{
    "info": "Please start game before fetching score."
}
```