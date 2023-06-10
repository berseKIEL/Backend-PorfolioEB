# Creador de Porfolios de Exequiel Barco

El objetivo de este repositorio es posibilitar a los usuarios crear, a traves de una REST API, porfolios.

- Se podrá crear un usuario, en las cuales a partir de eso. Se le devolverá un token que le permitirá crear sus propios porfolios
- Los porfolios contienen tres tipos de informaciones validas: Datos, Habilidades y Proyectos
- El Datos son los datos principales del usuario que lo identifican
- Las Habilidades son las dichosas que lo hacen reconocer como programador
- Los Proyectos es el curriculum que desmuestra dichas habilidades

Layout del Porfolio:
- Usuario (Usuario, Email, Contraseña, Nombre, Apellido, Titulo, Telefono, Descripción, Pais, Provincia)
- Habilidades (Titulo, Nivel)
- Lenguaje (Titulo, Nivel)
- Projecto (Titulo, Descripción, TecnologiasUsadas, RepoLink, ImagenLink, FechaInicio, FechaFin)
- Educacion (Titulo, Escuela, FechaInicio, FechaFin)

# API

## Users
- POST /api/v1/user/create || Crea un Nuevo Usuario

**Datos que debe recibir**
```JSON
{
  "email": "usuario@ejemplo.com",
  "username": "Usuario",
  "password": "Contrasenia"
}
```
- PUT /api/v1/user/update || Actualiza la información y los datos de un usuario

**Datos que puede debe recibir** (Opctional)
```JSON

{
  "email": "user@example.com",
  "username": "username",
  "first_name": "First",
  "last_name": "Last",
  "title": {
    "en": "Full-Stack Web Developer",
    "es": "Desarrollador Web Full-Stack",
  },
  "phone": "string",
  "description": {
    "en": "Hi there! I'm First Last",
    "es": "¡Hola! Soy First Last"
  },
  "country": "Argentina",
  "province": "Buenos Aires"
}
```

## Skills
- GET /api/v1/skill || Obtiene las habilidades de un Usuario

**Dato que debe recibir**
```JSON
[
  {
    "name": "string",
    "profiency": "string"
  }
]
```
- POST /api/v1/skill/create || Crea una habilidad para un usuario

**Datos que debe recibir**
```JSON
{
  "name": "string",
  "profiency": "Beginner"
}
```

- GET /api/v1/skill/{skill_id} || Obtiene una habilidad por su id

**Dato que debe recibir**
```
skill_id
```

- PUT /api/v1/skill/{skill_id} || Edita la skills de un usuario según su ID

**Datos puede debe recibir** (Opctional)
```JSON
{
  "name": "string",
  "profiency": "Beginner"
}
```

- DELETE /api/v1/skill/{skill_id}

Borra una skills de un usuario según su ID

**Dato que debe recibir**
```
skill_id
```

## Projects
- GET /api/v1/project/ || Obtiene las habilidades de un usuario

**Respuesta**
```JSON
[
  {
    "name": {
      "en": "string",
      "es": "string"
    },
    "description": {
      "en": "string",
      "es": "string"
    },
    "technologies_used": [
      "string"
    ],
    "repo_link": "string",
    "image_link": [
      "string"
    ],
    "date_start": "2023-04-16T23:39:18.257Z",
    "date_finish": "2023-04-16T23:39:18.257Z",
    "created_at": "2023-04-16T23:39:18.257Z",
    "updated_at": "2023-04-16T23:39:18.257Z"
  }
]
```
- POST /api/v1/project/create || Crea habilidades para un usuario

**Datos que debe recibir**
```JSON
{
  "name": {
    "en": "string",
    "es": "string"
  },
  "description": {
    "en": "string",
    "es": "string"
  },
  "technologies_used": [
    "string"
  ],
  "repo_link": "string",
  "image_link": [
    "string"
  ],
  "date_start": "2023-04-16T23:39:36.145Z",
  "date_finish": "2023-04-16T23:39:36.145Z"
}
```

- GET /api/v1/project/{project_id} || Obtiene una habilidad por su id

**Dato que debe recibir**
```
project_id
```

- PUT /api/v1/project/{project_id} || Edita la habilidad de un usuario según su ID

**Datos puede debe recibir** (Opctional)
```JSON
{
  "name": {
    "en": "string",
    "es": "string"
  },
  "description": {
    "en": "string",
    "es": "string"
  },
  "technologies_used": [
    "string"
  ],
  "repo_link": "string",
  "image_link": [
    "string"
  ],
  "date_start": "2023-04-16T23:46:06.032Z",
  "date_finish": "2023-04-16T23:46:06.032Z"
}
```

- DELETE /api/v1/project/{project_id} || Borra una habilidad de un usuario según su ID

**Dato que debe recibir**
```
project_id
```