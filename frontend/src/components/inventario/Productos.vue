<template>
    <v-container fluid style="background-color: #E8EAF6">
        <v-row>
            <v-col cols="12">
                <h1 class="title">Productos</h1>
            </v-col>
        </v-row>
        <v-card
                class="mx-auto"
        >
            <v-data-table
                    :headers="headers"
                    :items="productos"
                    class="elevation-1"
                    :search="search"
            >
                <template v-slot:top>
                    <v-toolbar flat color="white">
                        <v-text-field
                                v-model="search"
                                append-icon="mdi-magnify"
                                label="Buscar"
                                single-line
                                hide-details
                        ></v-text-field>
                        <v-divider
                                class="mx-4"
                                inset
                                vertical
                        ></v-divider>
                        <v-spacer></v-spacer>
                        <v-dialog v-model="dialog" fullscreen hide-overlay transition="dialog-bottom-transition">
                            <template v-slot:activator="{ on }">
                                <v-btn color="primary" dark v-on="on">Nuevo Producto</v-btn>
                            </template>
                            <v-card>
                                <v-toolbar dark color="primary">
                                    <v-btn icon dark @click="dialog = false">
                                        <v-icon>mdi-close</v-icon>
                                    </v-btn>
                                    <v-toolbar-title>{{formTitle}}</v-toolbar-title>
                                    <v-spacer></v-spacer>
                                    <v-toolbar-items>
                                        <v-btn dark text @click="save">Guardar</v-btn>
                                    </v-toolbar-items>
                                    <v-tabs
                                            slot="extension"
                                            centered
                                            v-model="tabs"
                                            slider-color="white"
                                            color="white"
                                    >
                                        <v-tab
                                                v-for="n in nombresTabs"
                                                :key="n"
                                        >
                                            {{ n }}
                                        </v-tab>
                                    </v-tabs>
                                </v-toolbar>
                                <v-tabs-items v-model="tabs">
                                    <v-tab-item
                                            key="1"
                                    >
                                        <mapp-datos-producto></mapp-datos-producto>
                                    </v-tab-item>
                                    <v-tab-item
                                            key="2"
                                            style="background-color: #E8EAF6"
                                            class="py-4"
                                    >
                                        <mapp-presentaciones-producto
                                                v-for="(presentacion, index) in presentaciones"
                                                :key="index"
                                                :index="index"
                                        ></mapp-presentaciones-producto>
                                    </v-tab-item>
                                    <v-tab-item
                                            key="3"
                                    >
                                        <mapp-lotes></mapp-lotes>

                                    </v-tab-item>
                                </v-tabs-items>
                            </v-card>
                        </v-dialog>
                    </v-toolbar>
                </template>
                <template v-slot:item.actions="{ item }">
                    <v-icon
                            small
                            class="mr-2"
                            @click="editItem(item)"
                    >
                        mdi-pencil
                    </v-icon>
                    <v-icon
                            small
                            @click="confirmarEliminar(item)"
                    >
                        mdi-delete
                    </v-icon>
                </template>
                <template v-slot:no-data>
                    <v-btn color="primary">Resetear</v-btn>
                </template>
            </v-data-table>
        </v-card>
        <v-snackbar
                v-model="snackbar"
                color="error"
                :right=true
                :timeout=6000
        >
            ¿Desea eliminar este Item?
            <v-btn
                    color="white"
                    text
                    @click="deleteItem()"
            >
                Sí, Eliminar
            </v-btn>
            <v-btn
                    color="white"
                    text
                    @click="snackbar = false"
            >
                Cancelar
            </v-btn>
        </v-snackbar>
    </v-container>

</template>
<script>
    import DatosProducto from "./DatosProducto";
    import Presentaciones from "./Presentaciones";
    import Lotes from "./Lotes";
    import axios from 'axios';

    export default {
        data: () => ({
            id_producto : '',
            tab: null,
            nombresTabs: ['Básico', 'Presentaciones', 'Lotes'],
            tabs: 0,
            snackbar: false,
            search: '',
            search_producto: '',
            dialog: false,
            headers: [
                {text: 'ID', value: 'id'},
                {text: 'Nombre', value: 'nombre',},
                {text: 'Categoria', value: 'categoria'},
                {text: 'Proveedor', value: 'proveedor'},
                {text: 'Acciones', value: 'acciones'},
                {text: 'Aplicaciones', value: 'aplicaciones'},
                {text: 'Acciones', value: 'actions', sortable: false},
            ],
            productos: [],
            editedIndex: -1,
        }),

        computed: {
            formTitle() {
                return this.editedIndex === -1 ? 'Nuevo Producto' : 'Editar Producto'
            },

            presentaciones: {
                get() {
                    return this.$store.state.producto.presentaciones
                },
            }
        },

        created(){
          this.initialize();
        },

        watch: {
            dialog(val) {
                val || this.close()
            },

        },
        methods: {
            initialize() {
                const ruta = 'http://localhost:8000/api/v1.0/producto/'
                axios.get(ruta).then(response => {
                    this.productos = response.data
                })
                    .catch(error => {
                        console.log(error);
                    });
            },


            confirmarEliminar(item) {
                this.snackbar = true;
                this.id_producto = item.id
            },

            editItem(item) {
                this.editedIndex = this.productos.indexOf(item)
                this.id_producto = item.id
                this.$store.commit('setProducto',item)
                console.log(JSON.stringify(this.$store.state.producto))
                this.dialog = true
            },

            deleteItem() {
                const ruta = "http://localhost:8000/api/v1.0/producto/" + this.id_producto + "/";
                axios.delete(ruta).then((response) => {
                    console.log(response.data);
                }).catch((error) => {
                    console.log(error);
                });
                const index = this.productos.indexOf(this.productos.find(pro => pro.id === this.id_producto))
                this.productos.splice(index, 1)
                this.snackbar = false
            },

            close() {
                this.dialog = false
                setTimeout(() => {
                    this.editedIndex = -1
                }, 300)
            },

            save() {
                if (this.editedIndex > -1) {
                    const ruta = 'http://localhost:8000/api/v1.0/producto/' + this.id_producto + "/"
                    axios.put(ruta, this.$store.state.producto).then(response => {
                        Object.assign(this.productos[this.editedIndex], response.data)
                    })
                    .catch(error => {
                        console.log(error);
                    });
                } else {
                    const ruta = 'http://localhost:8000/api/v1.0/producto/'
                    console.log(JSON.stringify(this.$store.state.producto))
                    axios.post(ruta, this.$store.state.producto).then((response) => {
                        this.productos.push(response.data);
                    }).catch((error) => {
                        console.log(error);
                    });
                }
                this.close()
            },
        },

        components: {
            mappDatosProducto: DatosProducto,
            mappPresentacionesProducto: Presentaciones,
            mappLotes: Lotes
        }
    }
</script>