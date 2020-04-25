<template>
    <v-container fluid style="background-color: #E8EAF6">
        <v-row>
            <v-col cols="12">
                <h1 class="title">Proveedores</h1>
            </v-col>
        </v-row>
        <v-card
                class="mx-auto"
        >
            <v-data-table
                    :headers="headers"
                    :items="proveedores"
                    sort-by="calories"
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
                        <v-dialog v-model="dialog" max-width="600px">
                            <template v-slot:activator="{ on }">
                                <v-btn color="primary" dark class="mb-2" v-on="on">Nuevo Proveedor</v-btn>
                            </template>
                            <v-card>
                                <v-card-title>
                                    <span class="title">{{ formTitle }}</span>
                                </v-card-title>
                                <v-divider></v-divider>
                                <v-card-text>
                                    <v-container>
                                        <v-row>
                                            <v-col cols="12" sm="6" md="6">
                                                <v-text-field v-model="editedItem.id"
                                                              hint="ID"
                                                              solo
                                                              readonly
                                                              persistent-hint
                                                ></v-text-field>
                                            </v-col>
                                            <v-col cols="12" sm="6" md="6">
                                                <v-text-field v-model="editedItem.nombre"
                                                              hint="Nombre"
                                                              solo
                                                              persistent-hint
                                                ></v-text-field>
                                            </v-col>
                                            <v-col cols="12" sm="6" md="6">
                                                <v-text-field v-model="editedItem.direccion"
                                                              hint="Direccion"
                                                              solo
                                                              persistent-hint
                                                ></v-text-field>
                                            </v-col>
                                            <v-col cols="12" sm="6" md="6">
                                                <v-text-field v-model="editedItem.telefono"
                                                              hint="Teléfono"
                                                              solo
                                                              persistent-hint
                                                ></v-text-field>
                                            </v-col>
                                            <v-col cols="12" sm="6" md="6">
                                                <v-text-field v-model="editedItem.nombre_banco"
                                                              hint="Banco"
                                                              solo
                                                              persistent-hint
                                                ></v-text-field>
                                            </v-col>
                                            <v-col cols="12" sm="6" md="6">
                                                <v-text-field v-model="editedItem.no_cuenta"
                                                              hint="Cuenta"
                                                              solo
                                                              persistent-hint
                                                ></v-text-field>
                                            </v-col>
                                            <v-col cols="12" sm="6" md="6">
                                                <v-text-field v-model="editedItem.nombre_vendedor"
                                                              hint="Vendedor"
                                                              solo
                                                              persistent-hint

                                                ></v-text-field>
                                            </v-col>
                                            <v-col cols="12" sm="6" md="6">
                                                <v-text-field v-model="editedItem.telefono_vendedor"
                                                              hint="Teléfono Vendedor"
                                                              solo
                                                              persistent-hint
                                                ></v-text-field>
                                            </v-col>
                                        </v-row>
                                    </v-container>
                                </v-card-text>

                                <v-card-actions>
                                    <v-spacer></v-spacer>
                                    <v-btn color="blue darken-1" text @click="close">Cancelar</v-btn>
                                    <v-btn color="blue darken-1" text @click="save">Guardar</v-btn>
                                </v-card-actions>
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
                :right = true
                :timeout = 6000
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
    import axios from 'axios';
    export default {
        data: () => ({
            //proveedorId : 0,
            snackbar : false,
            search: '',
            dialog: false,
            headers: [
                {text : 'ID', value :'id'},
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
                id : '',
                nombre: '',
                direccion: '',
                telefono: '',
                nombre_banco: '',
                no_cuenta: '',
                nombre_vendedor: '',
                telefono_vendedor: ''
            },
            defaultItem: {
                id : '',
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
                return this.editedIndex === -1 ? 'Nuevo Proveedor' : 'Editar Proveedor'
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

            confirmarEliminar(item){
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
    }
</script>