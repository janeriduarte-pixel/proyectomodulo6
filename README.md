Este proyecto como indica la entrega de este módulo es un sistema web para la gestión eficiente de proyectos y tareas individuales, desarrollado con el framework Django y estilizado mediante Bootstrap 5. El sistema permite registrar usuarios, gestionar cuentas de acceso seguras y mantener la privacidad total de la información, asegurando que cada usuario acceda únicamente a sus propios proyectos y tareas.

Características Principales:
Autenticación y Seguridad: Registro de nuevos usuarios (SignUpView), inicio de sesión (LoginView), cierre de sesión y protección de vistas mediante LoginRequiredMixin.
Gestión de Proyectos (CRUD): Crear, listar, editar y eliminar proyectos asociados directamente al usuario autenticado.
Gestión de Tareas (CRUD): Crear tareas dentro de cada proyecto, alternar su estado entre Pendiente y Completada mediante acciones rápidas (toggle), y eliminarlas directamente.
Panel de Administración: Configuración personalizada del administrador de Django (admin.py) con filtros por usuario, estado y campos de búsqueda.
Interfaz Moderna: Diseño adaptativo utilizando Bootstrap 5 con tarjetas, insignias y botones interactivos.

Para poder acceder a mi proyecto sigue estos pasos ordenados para desplegarlo localmente:
1. Clonar el repositorio e ingresar al proyecto:
git clone: https://github.com/janeriduarte-pixel/proyectomodulo6.git
cd proyectomodulo6
2. Crear y activar el entorno virtual:
python -m venv venv
venv\Scripts\activate
3. Instalar las dependencias:
pip install django
4. Aplicar las migraciones a la base de datos:
Ejecuta las migraciones para preparar la base de datos SQLite predeterminada:
python manage.py migrate
5. Crear un superusuario para el sitio administrativo
Para acceder al panel de control de Django en /admin/, crea una cuenta de administrador:
python manage.py createsuperuser
6. Iniciar el servidor de desarrollo:
python manage.py runserver
Abre tu navegador e ingresa a http://127.0.0.1:8000/ para comenzar a usar la aplicación.

Estructura del Proyecto
- core/models.py: Define los modelos Proyecto que vienen siendo los del usuario y las tareas.
- core/views.py: Vistas basadas en clases (CBV) para la lógica de negocio y seguridad.
- core/forms.py: Formularios personalizados con clases de Bootstrap (ProyectoForm, tarifaron, RegistroForm).
- core/admin.py: Configuración personalizada del panel administrativo con visualización de columnas y filtros.
- core/templates/:Plantillas HTML estructuradas en la carpeta core/ y registration/ extendiendo de base.html.
- mi_app/settings.py: Configuración global, idioma (es), zona horaria y URLs de redirección de autenticación.

Seguridad e Internacionalización
- Control de Accesos: Todas las vistas privadas heredan de LoginRequiredMixin, esto funciona para cuando un usuario no autenticado intenta acceder a una URL directa, es redirigido automáticamente a /accounts/login/.
- Aislamiento de Datos: El método get_queryset() en las vistas filtra los registros usando usuario=self.request.user, garantizando que un usuario no pueda consultar o alterar proyectos de otros.
- Idioma: Configurado en español (LANGUAGE_CODE = 'es') para la traducción automática de validaciones y formularios.
- Zona horaria (`TIME_ZONE`): Ajustado a `'America/Santiago'`, lo que garantiza que las fechas y horas de creación o modificación de los proyectos y tareas se registren y muestren con precisión según el huso horario local de Chile.

