# Decathon Calculator

This projects calculates Decathon competition scores https://en.wikipedia.org/wiki/Decathlon

The task is to output an JSON file with all athletes in ascending order of their places, containing all the input data plus total score and the place in the competition (in case of equal scores, athletes must share the places, e.g. 3-4 and 3-4 instead of 3 and 4). Draw an algorythm 
diagram using a tool you prefer.


## Endpoint
The endpoint `/score` accepts payload of the following structure.
``` http
POST api/score/
```
|Parameter |  Type         |  Description           |
|----------|:-------------:|-----------------------:|
| `url` |  `string`  | The url of the csv document|


## Responses
sucesss response
``` javascript
{
  "status_message": "Okay",
  "data": [
            {
            "name": "Edan Daniele",
            "100m": 12.61,
            "long_jump": 5,
            "shot_put": 9.22,
            "high_jump": 1.5,
            "400m": 60.39,
            "110m_hurdles": 16.43,
            "discus_throw": 21.6,
            "pole_vault": 2.6,
            "javelin_throw": 35.81,
            "1500m": "5.25.72",
            "score": 3873,
            "placement": 1
            },
        ]
}
```

The `status_message` The message corresponding to the `status code`.

The `data` the result of the payload that holds columns `['name', '100m', 'long_jump', 'shot_put', 'high_jump', '400m',                                '110m_hurdles', 'discus_throw', 'pole_vault', 'javelin_throw', '1500m', 'score','placement']`.

## Example Payload
Calling the endpoint `/api/score/`  
``` javascript
{
    "url":"https://docs.google.com/spreadsheets/d/1gaNCWqV6I6I_Hp5Er40-uDS8jiOI8RT4nsDmFj1r8zA/export?format=csv&gid=1656318840"
    
}
```