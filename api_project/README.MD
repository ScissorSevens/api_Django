# 📌  API

Este proyecto es una API REST usando  para la gestión de tareas por personas desarrollada en **Django** y **Django REST Framework (DRF)**.  
Permite crear, actualizar, eliminar y consultar tanto tareas como usuarios y además de filtrar las tareas  por fechas y usuarios.


## 🚀 Características principales

- Crear nuevas personas con su nombre, documento y email
- Actualizar las perosas existentes.  
- Eliminar personas por su documento.  
- Consultar personas 
- Respuestas en formato **JSON** estandarizado. 

- Crear nuevas tareas con título, descripción, fecha límite y persona asignada.  
- Actualizar tareas existentes.  
- Eliminar tareas por su ID.  
- Consultar tareas por:
  - Fecha específica.  
  - Rango de fechas.  
  - Persona asignada.  
- Respuestas en formato **JSON** estandarizado.  

⚡ Instalación y configuración
Clonar el repositorio:


git clone https://github.com/ScissorSevens/api_Django.git
Crear y activar entorno virtual:

python -m venv venv

.\venv\Scripts\activate    # Windows
Instalar dependencias:

pip install -r requirements.txt
Ejecutar migraciones:

python manage.py migrate
Iniciar el servidor:

python manage.py runserver
📬 Endpoints disponibles
La colección completa de endpoints y ejemplos de uso está documentada en Postman:

👉 Ver documentación en Postman : https://documenter.getpostman.com/view/43635397/2sB3HjNMXu

🛠️ Tecnologías utilizadas
Python 3.x

Django 5.x

Django REST Framework

PostgreSQL 

👨‍💻 Autor
Desarrollado por Ikhthys Felipe Bernal Pachón