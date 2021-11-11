andres
clara
mi rama
Cosas para hacer:
-- Backgraund imagen en static css no en html
-- opacity en dropdawn menu cantaro de piedra
--Definir si el modulo del busquieda va dentro de la main o dentro del index
-- Acerca de nosotros, contactos, libros
-- registro, login
-- paginas de error


Star-ratings:
    <template>
        <div>
            <b-form-rating v-model="value" readonly></b-form-rating>
            <p class="mt-2">Value: {{ value }}</p>
        </div>
    </template>
        
    <script>
    export default {
        data() {
        return {
            value: 2.567
        }
        }
    }
    </script>


    Auth 
     estilos de logion
     

index admin (idea suplente)
{% extends "main.html" %}

{% block title %}
    Admin
{% endblock %}

{% block content %}
    <div class="text-center font-monospace text-decoration-underline">
        <h2>Hola {{ current_user.name}} </h2>
    </div>
    <div class="row">
        <div class="col-5 usu">
            <a class="btn  col-11" data-bs-toggle="offcanvas" href="#offcanvasExample" role="button" aria-controls="offcanvasExample">
                Administrar la pagina
            </a>
        </div>
        <div class="col-5 usu">
            <a class="btn col-11" role="button" data-bs-toggle="offcanvas" data-bs-target="#estadistica" aria-controls="estadistiacas">
                Estadisticas
            </a>    
        </div>
    </div>
      
      <div class="offcanvas offcanvas-start gris" tabindex="-1" id="offcanvasExample" aria-labelledby="offcanvasExampleLabel">
        <div class="offcanvas-header">
          <h5 class="offcanvas-title" id="offcanvasExampleLabel">Administrar la pagina</h5>
          <button type="button" class="btn-close text-reset" data-bs-dismiss="offcanvas" aria-label="Close"></button>
        </div>
        <div class="offcanvas-body">
          <div class="m-3">
            Bienvenid@ de nuevo {{ current_user.name}} que deseas hacer?
          </div>
          <div class="list-group">
              <button type="button" class="gris btn button adm list-group-item list-group-item-action m-1 shadow" href="{{ url_for('admin.list_posts') }}">Agregar libros</a></button>
              <button type="button" class="gris btn button adm list-group-item list-group-item-action m-1 shadow" href="{{ url_for('admin.list_posts') }}">Agregar Autores</a></button>
              <button type="button" class="gris btn button adm list-group-item list-group-item-action m-1 shadow" href="{{ url_for('admin.list_posts') }}">Recomendaciones</a></button>
              <button type="button" class="gris btn button adm list-group-item list-group-item-action m-1 shadow" href="{{ url_for('admin.list_users') }}">Usuarios</a></button>  
          </div>
        </div>
      </div>
      <div class="offcanvas offcanvas-end gris" tabindex="-1" id="estadistica" aria-labelledby="estadisticas">
        <div class="offcanvas-header">
          <h5 class="offcanvas-title" id="estadisticas">Estadisticas de la pagina</h5>
          <button type="button" class="btn-close text-reset" data-bs-dismiss="offcanvas" aria-label="Close"></button>
        </div>
        <div class="offcanvas-body">
          <div class="m-3">
            Bienvenid@ de nuevo {{ current_user.name}} que deseas ver?
          </div>
          <div class="list-group">
              <button type="button" class="gris btn button adm list-group-item list-group-item-action m-1 shadow" href="{{ url_for('admin.list_posts') }}">Usuarios nuevos</a></button>
              <button type="button" class="gris btn button adm list-group-item list-group-item-action m-1 shadow" href="{{ url_for('admin.list_posts') }}">Ventas</a></button>
              <button type="button" class="gris btn button adm list-group-item list-group-item-action m-1 shadow" href="{{ url_for('admin.list_posts') }}">Minutos en pagina</a></button>
              <button type="button" class="gris btn button adm list-group-item list-group-item-action m-1 shadow" href="{{ url_for('admin.list_users') }}">Usuarios</a></button>  
          </div>
        </div>
      </div>
{% endblock %}

<!-- recomendaciones libros autores -->
 

preguntas 


1- El submit del form de libro-update no larga error cuadno no se sube el libro como hacer para que de un aviso de exito o de error.
2- Sigo sin poder hacer funcionar el Backgraund en algunas paginas 
3- Como mostrar un listado de todos los libros
4- No puedo subir un archivo epub
