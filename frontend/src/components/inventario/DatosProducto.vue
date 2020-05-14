<template>
    <v-card
            class="mx-8"
    >
        <v-card-text>
            <v-container>
                <v-row>
                    <v-col cols="12" sm="3" md="2">
                        <v-text-field
                                hint="ID"
                                solo
                                readonly
                                persistent-hint
                        ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="9" md="10">
                        <v-text-field
                                v-model="nombre"
                                hint="Nombre"
                                solo
                                persistent-hint
                        ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="6">
                        <mapp-categorias></mapp-categorias>
                    </v-col>
                    <v-col cols="12" sm="6" md="6">
                        <mapp-accion-producto></mapp-accion-producto>
                    </v-col>
                    <v-col cols="12" sm="6" md="6">
                        <mapp-aplicacion-producto></mapp-aplicacion-producto>
                    </v-col>
                    <v-col cols="12" sm="6" md="6">
                        <v-autocomplete
                                v-model="proveedor"
                                :items="proveedores"
                                persistent-hint
                                return-object
                                item-text="nombre"
                                hint="Proveedor"
                                class="mx-4"
                                clearable
                        ></v-autocomplete>
                    </v-col>
                </v-row>
            </v-container>
        </v-card-text>
    </v-card>
</template>

<script>
    import axios from "axios";
    import Categorias from "./Categorias";
    import AccionProducto from "./AccionProducto";
    import AplicacionProducto from "./AplicacionProducto";

    export default {
        name: "DatosProducto",
        data() {
            return {
                proveedor: {nombre : ''},
                proveedores: [],
            }
        },

        created() {
            const ruta = 'http://localhost:8000/api/v1.0/proveedores/'
            axios.get(ruta).then(response => {
                this.proveedores = response.data
            })
                .catch(error => {
                    console.log(error);
                });
        },

        computed: {
            nombre: {
                get(){
                    return this.$store.state.producto.nombre
                },
                set(value){
                    this.$store.commit('setNombreProducto',value)
                }
            },
        },

        watch : {
          proveedor(){
              if (this.proveedor != null)
                    this.setProveedor(this.proveedor)
              else {
                  this.setProveedor({nombre : ''})
              }
          }
        },

        methods : {
            setProveedor(proveedor){
                this.$store.commit('setProveedorProducto', proveedor)
            }
        },

        components: {
            mappCategorias: Categorias,
            mappAccionProducto: AccionProducto,
            mappAplicacionProducto: AplicacionProducto,
        }
    }
</script>

<style scoped>

</style>