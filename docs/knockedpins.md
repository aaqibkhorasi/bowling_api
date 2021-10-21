# Create User's Account

Create an Account for the authenticated User if an Account for that User does
not already exist. Each User can only have one Account.

**URL** : `/knocked_pins`

**Method** : `POST`

**Auth required** : No

**Permissions required** : None

**Data constraints**

Provide knocked-pin for particular throw.

```json
{
    "knocked_pins": "[Integer]"
}
```

**Data example** All fields must be sent.

```json
{
    "knocked_pins": "5"
}
```

## Success Response

**Condition** : If everything is OK and valid pin in entered, it will successfully update the score .

**Code** : `200 CREATED`

**Content example**

```json
{
    "info": "Scores updated.",
    "current_frame": 0,
    "current_frame_score": -1
}
```

## Error Responses

**Condition** : If pins value is above 10 

**Code** : `400 Bad Request`


**Content** : 
```json
{
    "error": "Pins knocked should be positive number and less than 11."
}
```

### Or

**Condition** : If pin value of current frame is more than 10.

**Code** : `400 BAD REQUEST`

**Content example**

```json
{
    "error": "Total knocked pins of first and second throw cannot be more than 10, 5 pins were knocked down in first throw."
}
```