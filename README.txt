Se busca realizar una aplicación gráfica CRUD, la cual se conectara con una base de datos basica, donde buscaremos insertar, leer, actualizar y borrar registros.

A aplicación debe poseer menus que se distribuyan en base de datos, borrar, CRUD y ayuda.
  El menu de base de datos, debe permitir conectarse (o crear) una base de datos y la opcion de salir para cerrar la aplicación.
    La base de datos debe poseer los siguientes campos: ID (INTEGER), NOMBRE_USUARIO (VARCHAR (50)), PASSWORD(VARCHAR (50)), APELLIDO(VARCHAR (20)), 
    DIRECCION (VARCHAR (50)) y COMENTARIO (VARCHAR (100)).
  El menu borrar, debe limpiar los formularios de datos por si se desea empezar devuelta con la carga de datos. Sin afectar a la base de datos.
  El menu CRUD, se lo puede diseñar como NO, dado que las opciones del mismo de crear, leer, actualizar y borrar seran ingresaros tambien como botones en la aplicación.
  El menu ayuda, puede contener datos como puede ser simplemente decorativo.

La aplicación debe tener varios formularios que reciban los datos para cada elemento de la base de datos, ejemplo: ID o PASSWORD.

Una vez cargado los datos en todos los campos del formulario, la opcion de create o crear, debe cargar dicho dato a la base de datos.

El boton leer y opcion leer, debe permitir traer por ID los datos y comentarios del campo de la base de datos al que este asignado.
El boton actualizar y opcion actualizar, debe permitir actualizar los datos del campo de la base de datos.
El boton borrar y opcion borrar, debe permitir borrar los datos de la ID ingresada.