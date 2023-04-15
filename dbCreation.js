const database = 'PorfolioEB';

use(database);

db.Porfolio.insertOne(
    {
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
            es: "Soy un desarrollador web con 2 años de experiencia",
            en: "I am a web developer with 2 years of experience"
        },
        country: "Argentina",
        province: "Santiago del Estero",

        skills: [
            {
                    
                _id: ObjectId(),
                name: "Javascript",
                proficiency: "Intermediate",
            },
            {   
                _id: ObjectId(),
                name: "Python",
                proficiency: "Intermediate",
            },
            {   
                _id: ObjectId(),
                name: "React",
                proficiency: "Intermediate",
            },
            {   
                _id: ObjectId(),
                name: "NextJS",
                proficiency: "Beginner",
            },
            {   
                _id: ObjectId(),
                name: "ExpressJS",
                proficiency: "Intermediate",
            },
            {   
                _id: ObjectId(),
                name: "MySQL",
                proficiency: "Intermediate",
            },
            {   
                _id: ObjectId(),
                name: "MongoDB",
                proficiency: "Intermediate",
            },
            {   
                _id: ObjectId(),
                name: "Sequelize",
                proficiency: "Intermediate",
            },
        ],

        projects: [
            {   
                _id: ObjectId(),
                company: "Vitrinia",
                name: {
                    en: "Vitrinia",
                    es: "Vitrinia"
                },
                description: {
                    es: "Aplicación de delivery de bienes y mercancías, y e-commerce.",
                    en: "Delivery App of Goods && Merchandise and E-commerce."
                },
                technologies_used: [
                    "NodeJs", "Typescript", "ExpressJs", "Sequelize", "React", "Bootstrap 3", "MySQL", "Ubuntu", "AWS"
                ],
                date_start: "2022-12-11T00:00:00.000Z",
                date_finish: null,
            },
            {   
                _id: ObjectId(),
                company: "ISPP",
                name: {
                    es: "Sistema de Gestión Academica",
                    en: "Academic Management System"
                },
                description: {
                    es: "Academic Management System to administrate studentes, teachers, etc.",
                    en: "Sistema para gestión academica para administración de alumnos, docentes, etc."
                },
                technologies_used: [
                    "Python", "Django", "Jinja", "Bootstrap 5", "Ubuntu", "NGINX"
                ],
                date_start: "2022-12-20T00:00:00.000Z",
                date_finish: null,
            },
            {   
                _id: ObjectId(),
                company: "RAASE",
                name: {
                    es: "Sistema de Derivación de Pacientes",
                    en: "Patient Referral System"
                },
                description: {
                    en: "Este sistema de referencia de pacientes facilita la transferencia del cuidado de un paciente de un proveedor de atención médica a otro.",
                    es: "This patient referral system facilitates the transfer of a patient's care from one healthcare provider to another."
                },
                technologies_used: [
                    "NodeJs", "Typescript", "ExpressJs", "Sequelize", "NextJs", "React", "PrimeReact", "MySQL", "Ubuntu", "NGINX"
                ],
                date_start: "2022-12-20T00:00:00.000Z",
                date_finish: null,
            },
            {   
                _id: ObjectId(),
                company: null,
                name: {
                    es: "Porfolio Personal",
                    en: "Personal Porfolio"
                },
                description: {
                    es: "Un portafolio de programador muestra sus habilidades, experiencia y proyectos en los que ha trabajado, demostrando su expertise y potencial a los empleadores.",
                    en: "A programmer's portfolio showcases their skills, experience, and projects they have worked on, demonstrating their expertise and potential to employers."
                },
                technologies_used: [
                    "Python", "FastAPI", "Mongo"
                ],
                date_start: "2022-12-20T00:00:00.000Z",
                date_finish: null,
            }
        ],
        date_created: new Date(),
        date_modified: new Date()
    }
)