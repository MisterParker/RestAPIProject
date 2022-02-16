# Refreshing the API 

In this repo, we will explore basics of RESTful APIs, for jogging the memory & then create an API application using flask.

## REST 
Representational State Transfer

## Method
1. GET — Get a resource from a server. (read only)
2. POST — Create a new resource on the server.
3. PUT — Update a request on the server.
4. PATCH — Partially update a request on the server.
5. DELETE — Delete a resource from the server.

## Status Codes
- 1xx: Informational: Communicates transfer protocol-level information.
- 2xx: Success: Client’s request was accepted successfully.
- 3xx: Redirection: Client must take some additional action in order to complete their request.
- 4xx: Client Error: Client side error.
- 5xx: Server Error: Server side error.

> Source: https://realpython.com/api-integration-in-python/
## Identify Resources

The first step is to identify resources that you want to be managed through the API.
Eg: customers, transactions, events, etc. Use nouns to define your resources.
Also consider the nested resources.
Eg: customers - sales, balance, accounts, etc.

Estabilishing the heirarchies will help us create proper Endpoints.

## Define Endpoints

Eg:
Refer below examples for how endpoints can be defined as per your requirements.

| Http Method | API Endpoint | Description |
| ----------- | ------------ | ----------- |
| GET         | /transactions | Get a list of transactions |
| GET         | /transactions/<transaction_id> | Get a particular transaction |
| POST        | /transactions | Create a new transaction |
| PUT         | /transactions/<transaction_id> | Update a transaction |
| PATCH       | /transactions/<transaction_id> | Partially update a transaction |
| DELETE      | /transactions/<transaction_id> | Delete a transaction |

avoid using unnecessary verbs like 'GET /getTransactions' 

Eg: (nested resources)

Method 1
| Http Method | API Endpoint | Description |
| ----------- | ------------ | ----------- |
| GET         | /events/<event_id>/guests | Get a list of guests |
| GET         | /events/<event_id>/guests/<guest_id> | Get a single guest |
& so on...

Method 2
some people prefer to use query strings to access a nested resource.

'''
query - a query allows us to pass on additional parameters along with our HTTP Request.

GET /guests?event_iq=12
'''

## API Versioning
> Source: https://docs.microsoft.com/en-us/azure/architecture/best-practices/api-design#uri-versioning

Its common that over time the APIs will develop further & undergo changes. But in that case as well you would want the older applications to work properly, while letting the new users/applications take advantage of new features & resource.

# Types

# 1. No Versioning
Simple Approach, but outdated, may be accepted for internal only.
Eg: 
'''
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{"id":3,"name":"Contoso LLC","address":"1 Microsoft Way Redmond WA 98053"}
'''

# 2. URI Versioning 


# 3. Query String Versioning
Eg:
'''
https://adventure-works.com/customers/3?version=2.
'''

# 4. Header Versioning
'''
GET https://adventure-works.com/customers/3 HTTP/1.1
Custom-Header: api-version=1
'''

'''
GET https://adventure-works.com/customers/3 HTTP/1.1
Custom-Header: api-version=2
'''

# 5. Media Type Versioning
'''
GET https://adventure-works.com/customers/3 HTTP/1.1
Accept: application/vnd.adventure-works.v1+json
'''

## Data Interchange Format

# 1. XML
Eg:
'''
<?xml version="1.0" encoding="UTF-8">
<car>
    <company>Mahindra</company>
    <name>Marazzo</name>
    <models>
        <model>
            <model-name>M6</model-name>
            <capacity>7 - Seater</capacity>
        </model>
        <model>
            <model-name>M8</model-name>
            <capacity>8 - Seater</capacity>
        </model>
    </models>
    <type>SUV</type>
    <year>2018</year>
'''

# 2. JSON
Eg:
'''
{
    "company": "Mahindra",
    "name": "Marazzo",
    "models" : [
        {
            "model-name": "M6",
            "capacity": "7 - Seater"
        },
        {
            "model-name": "M8",
            "capacity": "8 - Seater"
        }
    ],
    "type": "SUV",
    "year": "2018",
}
'''
