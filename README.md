 ## Crear el proyecto.
    Crear la carpeta del proyecto mkdir.
    Crear el entorno virtual con venv o pyenv:
        - python3 -m venv venv
    Instalar django: pip install django
    Iniciar el repositorio de git: git init
    Iniciar el proyecto de django: django-admin startproject 'nomredelproyecto'
    Para evitar llevar al repositorio remoto archivos innecesarios es importante 
    crear el archivo: .gitignore (Donde se suele agregar la carpeta venv).

## Explorando los archivos que creó Django.
    init indica que es un paquete
    asgi y wsgi son archivos que sirven para el despliegue a producción del proyecto
    settings son configuraciones como BD, zona horaria, lenguaje, etc.
    urls es el archivo que tiene las rutas del proyecto.
    La subcarpeta es la que está afectada por django cambiar a este directorio.

## Servidor de desarrollo.
    - python manage.py runserver
    Detalle de mensaje:
    Watching for file … : A cada cambio que hagas en los archivo, Django lo notará y lo reflejará en el servidor.
    System check identified no issues … : No hay problemas y se silenciaron 0.
    You have 18 unapplied migration(s) … : No se ha creado una base de datos efectiva.
    Date, Version Django
    Using settings ‘premiosplatziapp.settings’ : Tomar el archivo settings-py, ver la variables de configuración y aplicarlas para tenerlas disponibles al crear el código.
    Starting development … : Servidor desplegado (iniciado) de manera local.

## Nuestro primer proyecto.
    Dentro de Django hay 2 cosas importantes para diferenciar:

    Proyecto : Un proyecto es una colección de configuraciones y aplicaciones para un sitio web en particular. Un proyecto puede contener varias aplicaciones. Una aplicación puede estar en varios proyectos.
    Apps : Una aplicación es una aplicación web que hace algo, por ejemplo, un sistema de blogs, una base de datos de registros públicos o una pequeña aplicación de encuestas.
    Cada aplicación que escribe en Django consta de un paquete de Python que sigue una determinada convención. Django viene con una utilidad que genera automáticamente la estructura básica de directorios de una aplicación, por lo que puede concentrarse en escribir código en lugar de crear directorios.

    -python manage.py startapp polls
    -Hacemos el hola mundo en un view.

## ORM
    Un ORM (Object-Relational Mapping) es una técnica que nos permite crear una Base de Datos Orientada a Objectos (virtual), que opera sobre la Base de Datos Relacional (real).

    Utilizando un ORM podemos operar sobre la base de datos aprovechando las características propias de la orientación a objetos, como herencia y polimorfismo.

    También podemos acceder a los atributos de una Entidad de la misma forma que accedemos a los atributos de una Clase, realizar operaciones para obtener, crear, modificar y eliminar datos, todo desde el código de programación sin tener que escribir SQL. Esto además nos permite escribir el código una sola vez y garantizarnos que va a seguir funcionando incluso si en el futuro se cambia el motor de Base de Datos (por ejemplo, de MySQL a Microsoft SQL Server).

    Modelo --->> clases(poo) ---> bbdd ---> tablas

    Atributos---->bbdd----> columnas

    cada columna debe tener un tipo de datos eje. primary key ---> int -> clases dentro de atributos.

    El nombre de los modelos siempre en singular.

    Migraciones para MOdelos:
    python manage.py makemigrations polls --> convertir en tablas
    python manage.py migrate  ---> ejecut las tablas sql en la base de datos.

## Consola interactiva
    python manage.py shell

    Queries:
    model.objects.all()  --> trae todos los registros.
    get() --> traer una condicion --> ejemplo (pk=1) trae un solo elemento.
    time zone:
    filter(pub_date__year=timezone.now().year) --> una query que puede traer todo el conjunto de objectos
    __gt = Mayor que
    __gte = Mayor o igual que
    __lt = Menor que
    __lte = Menos o igual que
    __startswith = Empieza con
    __endswith = Termina con

    tabla.choice_set.all() ---> establecer opciones
    .create() --> crear respuesta
    .count() --> acceder al conteo


## Administrador de Django.
    python manage.py createsuperuser  ---> tener cuidado con la creación de usuarios, se establecerá usuario y contraseña.
    Establecer los modelos en el archivo de admin de la app.

    Frontend ---> templates
    Backend ----> views  ---|-- funcion (function base views)o puede ser una clase. (generic views)

## El render es una función importada de Django. Necesita tres parámetros

    El request
    La ubicación de la template correlacionada. En la ruta se omite la carpeta /template/ ya que Django junta todas las carpetas templates de todas las aplicaciones de nuestro proyecto y las hace una sola
    Un objeto con la o las variables que le estaremos pasando a nuestra template


## Equivalencias de las views.
    generic views --> funciones

    class viewss ---> clases


## Generic views si se puede.
     Si podemos seguir el patrón:
     cargar datos de la base de datos
     Generar template
     Mostrar template
     Si no se pude:

## Functions based views.
    Escaparse del patrón anterior. Si es mas complejo, como mostrar 2 formularios en la misma página

   Comentarios en VSC:

   CTRL + K + C
   CTRL + K + U
