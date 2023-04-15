# Porfolio Backend de Exequiel Barco

Python - Framework Fast API

## Objetivo a Llegar

Objetivo a Llegar:

```json
{
  # Login
  "email": "exebarco280320@gmail.com",
  "username": "exebarco",
  "password": "asdf1234",

  # Normal Data
  "first_name": "Exequiel",
  "last_name": "Barco",
  "title": {
    "en": "Jr. Web Developer",
    "es": "Desarrollador Web Junior",
  },
  "phone": "+5493856276491",
  "description": {
    "en": "I am a web developer with 2 years of experience",
    "es": "Soy un desarrollador web con 2 años de experiencia"
  },
  "country": "Argentina",
  "province": "Santiago del Estero",

  # Porfolio
  "skills": [
    {
      "name": "Javascript",
      "proficiency": "Intermediate"
    },
    {
      "name": "Python",
      "proficiency": "Intermediate"
    },
    {
      "name": "React",
      "proficiency": "Intermediate"
    },
    {
      "name": "NextJS",
      "proficiency": "Beginner"
    },
    {
      "name": "ExpressJS",
      "proficiency": "Intermediate"
    },
    {
      "name": "MySQL",
      "proficiency": "Intermediate"
    },
    {
      "name": "MongoDB",
      "proficiency": "Intermediate"
    },
    {
      "name": "Sequelize",
      "proficiency": "Intermediate"
    },
  ],
  "projects": [
    {
      "company": "Vitrinia",
      "name": {
        "en": "Vitrinia",
        "es": "Vitrinia"
      },
      "description": {
        "en": "Delivery App of Goods && Merchandise and E-commerce.",
        "es": "Aplicación de delivery de bienes y mercancías, y e-commerce."
      },
      "technologies_used": [
        "NodeJs", "Typescript", "ExpressJs", "Sequelize", "React", "MySQL", "Ubuntu", "AWS"
      ],
      "date_start": "",
      "date_finish": "",
    },
    {
      "company": "ISPP",
      "name": {
        "en": "Sistema de Gestión Academica",
        "es": "Academic Management System"
      },
      "description": {
        "en": "Sistema para gestión academica para administración de alumnos, docentes, etc.",
        "es": "Academic Management System to administrate studentes, teachers, etc."
      },
      "technologies_used": [
        "Python", "Django", "Ubuntu", "NGINX"
      ],
      "date_start": "",
      "date_finish": "",
    }
  ]
}
```

## API

POST
/api/v1/porfolio/create

```json
{
  "email": "exebarco280320@gmail.com",
  "username": "exebarco",
  "password": "asdf1234",
  "first_name": "Exequiel",
  "last_name": "Barco",
  "title": {
    "en": "Jr. Web Developer",
    "es": "Desarrollador Web Junior"
  },
  "phone": "+5493856276491",
  "description": {
    "en": "I am a web developer with 2 years of experience",
    "es": "Soy un desarrollador web con 2 años de experiencia"
  },
  "country": "Argentina",
  "province": "Santiago del Estero"
}
```

POST
/api/v1/auth/login

```
"email": "exebarco280320@gmail.com",
"password": "asdf1234"
```
