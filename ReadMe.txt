andres
clara
mi rama
Cosas para hacer:
-- Backgraund imagen en static css no en html
-- opacity en dropdawn menu cantaro de piedra
--Definir si el modulo del busquieda va dentro de la main o dentro del index
-- footer
-- Acerca de nosotros, contactos, libros
-- registro, login
-- paginas de error

Base de datos (PONER TODO EN EL MISMO IDIOMA)
- en tabla libro:
    1) Eduitar el titulo (dice libros).
    2) Agregar tabla ISBN
- En detalle factura no va anulado va solo en factura 
- En genero va codigo
- En idioma va codigo
- En Pais va codigo y continente


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