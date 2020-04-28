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
                    :items="proveedores"
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
                                        <v-btn dark text @click="dialog = false">Guardar</v-btn>
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
                                        <v-card
                                                class="mx-8"
                                        >
                                            <v-card-text>
                                                <v-container>
                                                    <v-row>
                                                        <v-col cols="12" sm="3" md="2">
                                                            <v-text-field v-model="editedItem.id"
                                                                          hint="ID"
                                                                          solo
                                                                          readonly
                                                                          persistent-hint
                                                            ></v-text-field>
                                                        </v-col>
                                                        <v-col cols="12" sm="9" md="10">
                                                            <v-text-field v-model="editedItem.nombre"
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
                                                            <v-btn class="ma-2" fab small dark color="primary"
                                                                   @click="">
                                                                <v-icon dark>mdi-plus</v-icon>
                                                            </v-btn>
                                                            <v-autocomplete
                                                                    v-model="proveedor_seleccionado"
                                                                    :items="proveedores"
                                                                    :search-input="search_proveedor"
                                                                    persistent-hint
                                                                    return-object
                                                                    item-text="nombre"
                                                                    hint="Proveedor"
                                                                    clearable
                                                            ></v-autocomplete>
                                                        </v-col>
                                                    </v-row>
                                                </v-container>
                                            </v-card-text>
                                        </v-card>
                                    </v-tab-item>
                                    <v-tab-item
                                            key="2"
                                    >
                                        <v-card
                                                class="mx-8"
                                        >
                                            <v-card-text>
                                                2
                                            </v-card-text>
                                        </v-card>
                                    </v-tab-item>
                                    <v-tab-item
                                            key="3"
                                    >
                                        <v-card
                                                class="mx-8"
                                        >
                                            <v-card-text>
                                                3
                                            </v-card-text>
                                        </v-card>
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
                    <v-btn color="primary" @click="initialize">Resetear</v-btn>
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
    import Categorias from "./Categorias";
    import AccionProducto from "./AccionProducto";
    import AplicacionProducto from "./AplicacionProducto";
    import axios from 'axios';

    export default {
        data: () => ({
            //proveedorId : 0,
            proveedor_seleccionado: null,
            tab: null,
            nombresTabs: ['Básico', 'Presentaciones', 'Lotes'],
            tabs: 0,
            snackbar: false,
            search: '',
            search_proveedor: '',
            dialog: false,
            headers: [
                {text: 'ID', value: 'id'},
                {text: 'Nombre', value: 'nombre',},
                {text: 'Dirección', value: 'direccion'},
                {text: 'Teléfono', value: 'telefono'},
                {text: 'Banco', value: 'nombre_banco'},
                {text: 'Cuenta', value: 'no_cuenta'},
                {text: 'Vendedor', value: 'nombre_vendedor'},
                {text: 'Tel Vendedor', value: 'telefono_vendedor'},
                {text: 'Acciones', value: 'actions', sortable: false},
            ],
            proveedores: [],
            editedIndex: -1,
            editedItem: {
                id: '',
                nombre: '',
                direccion: '',
                telefono: '',
                nombre_banco: '',
                no_cuenta: '',
                nombre_vendedor: '',
                telefono_vendedor: ''
            },
            defaultItem: {
                id: '',
                nombre: '',
                direccion: '',
                telefono: '',
                nombre_banco: '',
                no_cuenta: '',
                nombre_vendedor: '',
                telefono_vendedor: ''
            },
        }),

        computed: {
            formTitle() {
                return this.editedIndex === -1 ? 'Nuevo Producto' : 'Editar Producto'
            },
        },

        watch: {
            dialog(val) {
                val || this.close()
            },
        },

        created() {
            this.initialize()
            //this.getProveedor()
            //this.proveedorId = this.$route.params.proveedorId;
        },

        methods: {
            initialize() {
                const ruta = 'http://localhost:8000/api/v1.0/proveedores/'
                axios.get(ruta).then(response => {
                    this.proveedores = response.data
                })
                    .catch(error => {
                        console.log(error);
                    });
            },

            // getProveedor(){
            //   const ruta = "http://127.0.0.1:8000/api/v1.0/proveedores/${this.proveedorId}"
            //     axios.get(ruta).then(response => {
            //        console.log(response.data.nombre);
            //
            //     }).catch(error => {
            //        console.log(error);
            //     });
            // },

            confirmarEliminar(item) {
                this.snackbar = true;
                this.editedItem = Object.assign({}, item)
            },

            editItem(item) {
                this.editedIndex = this.proveedores.indexOf(item)
                this.editedItem = Object.assign({}, item)
                this.dialog = true
            },

            deleteItem() {
                const ruta = "http://localhost:8000/api/v1.0/proveedores/" + this.editedItem.id + "/";
                axios.delete(ruta).then((response) => {
                    console.log(response.data);
                }).catch((error) => {
                    console.log(error);
                });
                const index = this.proveedores.indexOf(this.editedItem)
                this.proveedores.splice(index, 1)
                this.snackbar = false
            },

            close() {
                this.dialog = false
                setTimeout(() => {
                    this.editedItem = Object.assign({}, this.defaultItem)
                    this.editedIndex = -1
                }, 300)
            },

            save() {
                if (this.editedIndex > -1) {
                    const ruta = 'http://localhost:8000/api/v1.0/proveedores/' + this.editedItem.id + "/"
                    axios.put(ruta, this.editedItem).then(response => {
                        Object.assign(this.proveedores[this.editedIndex], response.data)
                    })
                        .catch(error => {
                            console.log(error);
                        });
                } else {
                    const ruta = 'http://localhost:8000/api/v1.0/proveedores/'
                    axios.post(ruta, this.editedItem).then((response) => {
                        this.proveedores.push(response.data);
                    }).catch((error) => {
                        console.log(error);
                    });
                }
                this.close()
            },
        },

        components: {
            mappCategorias: Categorias,
            mappAccionProducto: AccionProducto,
            mappAplicacionProducto: AplicacionProducto
        }
    }
</script>