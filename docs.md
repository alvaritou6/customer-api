# Documentation for customer managment API

This API helps to make a CRUD on an existing database by handling it with a fontend. It is designed for frontend programmers to make the corresponding connections and squeeze the API.

<br/>

-----
API Version: s1.0

## Endpoints

| URI                | Description              | HTTP Method | Parameters      |
|--------------------|--------------------------|-------------|-----------------|
| `/api/customers`   | Devuelve un JSON con todos los usuarios existentes en la base de  datos.                  | GET         |     -           |
| `/api/customers/id`| Devuelve el usuario con id especificado en el parametro.                   | GET         | ID del usuario  |
| `/api/customers`   | Guarda un usuario o crea uno. Es importante poner el JSON con la información en el body de la request.                  | POST        |       -         |
|`/api/customers/id` | Elimina el usuario especificado en el parametro id.                         | DELETE      | ID del usuario  |

## HTTP Codes

> This program does not contain alternative HTTP codes, the only ones it returns are the official and approved HTTP Codes. <br/> You can view the codes [here](https://developer.mozilla.org/es/docs/Web/HTTP/Status).


<br/><br/></br>

***

If you wish to contact the developer click [here](https://github.com/alvaritou6).