# Porfolio Backend de Exequiel Barco
Python - Framework Fast API

## API
Crear porfolio

POST
/api/v1/porfolio/create
{
  "email": "exebarco280320@gmail.com",
  "username": "exebarco",
  "password": "passwordtesting",
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
  "province": "Santiago del Estero"
}