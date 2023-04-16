const database = 'PorfolioEB';

use(database);

// db.Porfolio.insertOne(
//     {
//         email: "exebarco280320@gmail.com",
//         username: "exebarco",
//         password: "asdf1234",

//         first_name: "Exequiel",
//         last_name: "Barco",
//         title: {
//             es: "Desarrollador Web Junior",
//             en: "Jr. Web Developer"
//         },
//         phone: "+5493856276491",
//         description: {
//             es: "¡Hola! Mi nombre es Exequiel Barco, y soy un desarrollador web con la pasión de hacer realidad ideas innovadoras a través de la tecnología. He estado usando computadoras desde que tenía siete años y desde siempre he estado fascinado por el continue avance técnologico y digital de este mundo. Como desarrollador, estoy constantemente buscando nuevas técnicas y herramientas para mejorar mis habilidades y brindar las mejores soluciones posibles a mis clientes. Siempre estoy atento a las últimas tendencias y avances en tecnología, y me encanta investigar y aprender sobre nuevos lenguajes de programación y frameworks. Además de mis habilidades técnicas, me gusta trabajar en equipo y soy de los que disfruta colaborar con otros para lograr objetivos comunes. Considero tener excelentes habilidades de comunicación y puedo trabajar eficazmente con interesados tanto técnicos como no técnicos.",
//             en: "Hi there! My name is Exequiel Barco, and I am a web developer with a passion for bringing innovative ideas to life through technology. I have been using computers since I was seven years old and have been fascinated by the ever-evolving digital landscape ever since. As a developer, I am constantly seeking new techniques and tools to improve my skills and deliver the best possible solutions for my clients. I am always on the lookout for the latest trends and advancements in technology, and I love to research and learn about new programming languages and frameworks. In addition to my technical skills, I am a team player who enjoys collaborating with others to achieve common goals. I have excellent communication skills and can work effectively with both technical and non-technical stakeholders."
//         },
//         country: "Argentina",
//         province: "Santiago del Estero",

//         skills: [
//             {
//                 name: "Javascript",
//                 proficiency: "Intermediate",
//             },
//             {
//                 name: "Python",
//                 proficiency: "Intermediate",
//             },
//             {
//                 name: "React",
//                 proficiency: "Intermediate",
//             },
//             {
//                 name: "NextJS",
//                 proficiency: "Beginner",
//             },
//             {
//                 name: "ExpressJS",
//                 proficiency: "Intermediate",
//             },
//             {
//                 name: "MySQL",
//                 proficiency: "Intermediate",
//             },
//             {
//                 name: "MongoDB",
//                 proficiency: "Intermediate",
//             },
//             {
//                 name: "Sequelize",
//                 proficiency: "Intermediate",
//             },
//         ],

//         projects: [
//             {
//                 company: "Vitrinia",
//                 name: {
//                     es: "Vitrinia",
//                     en: "Vitrinia"
//                 },
//                 description: {
//                     es: "Aplicación de delivery de bienes y mercancías, y e-commerce. Trabajé como Desarrollador Full-stack: Diseño y Implementación Front-End con React Class Component con Bootstrap 3, desarrollo de rutas API y modejale de Base de Datos con ExpressJS - Sequelize - MySQL, Deploys en EC2 de AWS (no automatizados). Uso de Jira Software para manejo de Incidencias y Bitbucket para repositorio. Realizé tareas como automatización de la gestión administrativa, contable y financiera, y mejorar diseño Front-End.",
//                     en: "Delivery and E-commerce application. I worked as a Full-stack Developer: designing and implementing the front-end using React Class Component with Bootstrap 3, developing API routes, modeling the database with ExpressJS - Sequelize - MySQL, performing deployments on AWS EC2 (not automated), using Jira Software for incident management and Bitbucket for source control. I also automated administrative, accounting, and financial management tasks and improved the front-end design."
//                 },
//                 technologies_used: [
//                     "NodeJs", "Typescript", "ExpressJs", "Sequelize", "React", "Bootstrap 3", "MySQL", "Ubuntu Server", "AWS"
//                 ],
//                 repo_link: null,
//                 image_link: [
//                     "https://imgur.com/DwTSeBi",
//                     "https://imgur.com/ppW4bER"
//                 ],
//                 date_start: "2022-12-11T00:00:00.000Z",
//                 date_finish: null,
//             },
//             {
//                 company: "ISPP",
//                 name: {
//                     es: "Sistema de Gestión Academica",
//                     en: "Academic Management System"
//                 },
//                 description: {
//                     es: "Sistema de Gestión Academica: Administración de Usuarios (Estudiantes, Docentes, entre otros). Trabajé como Desarrollador Full-Stack: Realizé tareas como configuración del servidor, configuración de Django para deployment, configuración del Django-Admin, cargado de Base de Datos de Excel a MySQL, realizé el Deploy en servidores de Ubuntu, Diseño Front-end, Diseño de Base de Datos, Modejale en Django, implementacion de rutas API, manejo de lenguaje Jinja de Django",
//                     en: "Academic Management System: User Administration (Students, Teachers, among others). I worked as a Full-Stack Developer: I performed tasks such as server configuration, Django configuration for deployment, Django-Admin configuration, loading Excel database to MySQL, deployment on Ubuntu servers, Front-end design, Database design, Model creation in Django, implementation of API routes, and management of Django's Jinja language."
//                 },
//                 technologies_used: [
//                     "Python", "Django", "Jinja", "Bootstrap 5", "Ubuntu Server", "NGINX"
//                 ],
//                 repo_link: null,
//                 image_link: [
//                     "https://imgur.com/nLUewdB",
//                     "https://imgur.com/xO0DnYf"
//                 ],
//                 date_start: "2022-12-20T00:00:00.000Z",
//                 date_finish: null,
//             },
//             {
//                 company: "RAASE",
//                 name: {
//                     es: "Sistema de Derivación de Pacientes",
//                     en: "Patient Referral System"
//                 },
//                 description: {
//                     en: "Este sistema de referencia de pacientes facilita la transferencia del cuidado de un paciente de un proveedor de atención médica a otro. Trabajé como Desarrollador Full-stack: Desarrollo de controladores back-end creando implementaciones de las rutas API protegidas con JWT, desarrollo de diseño front-end utilizando PrimeReact con el Dashboard administrativo de Sakai, Diseño de base de Datos, Deploy a servidor en Ubuntu Server, configuración del servidor, configuración para Deployment.",
//                     es: "This patient referral system facilitates the transfer of a patient's care from one healthcare provider to another. I worked as a Full-stack Developer: I developed backend controllers by creating implementations of JWT-protected API routes, developed front-end design using PrimeReact with Sakai's administrative dashboard, designed the database, deployed to an Ubuntu Server, performed server configuration, and configured the system for deployment."
//                 },
//                 technologies_used: [
//                     "NodeJs", "Typescript", "ExpressJs", "Sequelize", "NextJs", "React", "PrimeReact", "MySQL", "Ubuntu Server", "NGINX"
//                 ],
//                 repo_link: null,
//                 image_link: [
//                     "https://imgur.com/uQWbDAU",
//                     "https://imgur.com/Jme2e50"
//                 ],
//                 date_start: "2022-12-20T00:00:00.000Z",
//                 date_finish: null,
//             },
//             {
//                 company: null,
//                 name: {
//                     es: "Porfolio Personal",
//                     en: "Personal Porfolio"
//                 },
//                 description: {
//                     es: "Un portafolio de programador muestra sus habilidades, experiencia y proyectos en los que ha trabajado, demostrando su expertise y potencial a los empleadores.",
//                     en: "A programmer's portfolio showcases their skills, experience, and projects they have worked on, demonstrating their expertise and potential to employers."
//                 },
//                 technologies_used: [
//                     "Python", "FastAPI", "Mongo"
//                 ],
//                 repo_link: "",
//                 image_link: [],
//                 date_start: "2022-12-20T00:00:00.000Z",
//                 date_finish: null,
//             }
//         ],
//         date_created: new Date(),
//         date_modified: new Date()
//     }
// )

db.User.insertOne({
    email: "exebarco280320@gmail.com",
    username: "exebarco",
    password: "asdf1234",

    first_name: "Exequiel",
    last_name: "Barco",
    title: {
        es: "Desarrollador Web Junior",
        en: "Jr. Web Developer"
    },
    phone: "+5493856276491",
    description: {
        es: "¡Hola! Mi nombre es Exequiel Barco, y soy un desarrollador web con la pasión de hacer realidad ideas innovadoras a través de la tecnología. He estado usando computadoras desde que tenía siete años y desde siempre he estado fascinado por el continue avance técnologico y digital de este mundo. Como desarrollador, estoy constantemente buscando nuevas técnicas y herramientas para mejorar mis habilidades y brindar las mejores soluciones posibles a mis clientes. Siempre estoy atento a las últimas tendencias y avances en tecnología, y me encanta investigar y aprender sobre nuevos lenguajes de programación y frameworks. Además de mis habilidades técnicas, me gusta trabajar en equipo y soy de los que disfruta colaborar con otros para lograr objetivos comunes. Considero tener excelentes habilidades de comunicación y puedo trabajar eficazmente con interesados tanto técnicos como no técnicos.",
        en: "Hi there! My name is Exequiel Barco, and I am a web developer with a passion for bringing innovative ideas to life through technology. I have been using computers since I was seven years old and have been fascinated by the ever-evolving digital landscape ever since. As a developer, I am constantly seeking new techniques and tools to improve my skills and deliver the best possible solutions for my clients. I am always on the lookout for the latest trends and advancements in technology, and I love to research and learn about new programming languages and frameworks. In addition to my technical skills, I am a team player who enjoys collaborating with others to achieve common goals. I have excellent communication skills and can work effectively with both technical and non-technical stakeholders."
    },
    country: "Argentina",
    province: "Santiago del Estero",
    date_created: new Date(),
    date_modified: new Date()
})

db.User.insertMany([
    {
        name: "Javascript",
        proficiency: "Intermediate",
        date_created: new Date(),
        date_modified: new Date()
    },
    {
        name: "Python",
        proficiency: "Intermediate",
        date_created: new Date(),
        date_modified: new Date()
    },
    {
        name: "React",
        proficiency: "Intermediate",
        date_created: new Date(),
        date_modified: new Date()
    },
    {
        name: "NextJS",
        proficiency: "Beginner",
        date_created: new Date(),
        date_modified: new Date()
    },
    {
        name: "ExpressJS",
        proficiency: "Intermediate",
        date_created: new Date(),
        date_modified: new Date()
    },
    {
        name: "MySQL",
        proficiency: "Intermediate",
        date_created: new Date(),
        date_modified: new Date()
    },
    {
        name: "MongoDB",
        proficiency: "Intermediate",
        date_created: new Date(),
        date_modified: new Date()
    },
    {
        name: "Sequelize",
        proficiency: "Intermediate",
        date_created: new Date(),
        date_modified: new Date()
    },
])