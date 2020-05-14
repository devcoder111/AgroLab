<template>
    <v-card
            tile
            class="px-2"
    >
        <v-row>
            <v-col cols="12" sm="12" md="6" lg="6" class="py-0 text-center">
                <v-btn class="ma-2" fab small dark color="primary" @click="agregarTipoProducto()">
                    <v-icon dark>mdi-plus</v-icon>
                </v-btn>
                <v-btn class="ma-2" fab small dark color="warning" @click="editarTipoProducto()">
                    <v-icon dark>mdi-pencil</v-icon>
                </v-btn>
                <v-btn class="ma-2" fab small dark color="error" @click="eliminarTipoProducto()">
                    <v-icon dark>mdi-delete</v-icon>
                </v-btn>
            </v-col>
            <v-col cols="12" sm="12" md="6" lg="6" class="py-0">
                <v-autocomplete
                        v-model="select"
                        :items="tipos"
                        :search-input="search"
                        persistent-hint
                        return-object
                        item-text="nombre"
                        hint="Tipo de Producto"
                        clearable
                ></v-autocomplete>
            </v-col>
        </v-row>
        <v-dialog
                v-model="dialog"
                max-width="350"
        >
            <v-card>
                <v-card-title>
                    <span class="title">{{ tituloFormulario }}</span>
                </v-card-title>
                <v-card-text>
                    <span
                            v-if="editedIndex === 1"
                            class="subtitle-2">
                        ¿Está seguro que desea eliminar el tipo de producto {{editedItem.nombre}} ?
                    </span>
                    <v-text-field
                            v-if="editedIndex != 1"
                            v-model="editedItem.nombre"
                            hint="Tipo de Producto"
                            solo
                            persistent-hint
                    ></v-text-field>
                </v-card-text>

                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn
                            color="error"
                            text
                            @click="cerrar()"
                    >
                        Cancelar
                    </v-btn>

                    <v-btn
                            color="primary"
                            text
                            @click="guardar"
                    >
                        {{textoGuardar}}
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-card>
</template>
<script>
    import axios from "axios";

    export default {
        props : ['index'],
        data() {
            return {
                dialog: false,
                search: null,
                select: null,
                editedIndex: -1,
                editedItem: {
                    id: '',
                    nombre: ''
                },
                defaultItem: {
                    id: '',
                    nombre: ''
                },
                tipos: []
            }
        },

        created() {
            const ruta = 'http://localhost:8000/api/v1.0/tipo-producto/'
            axios.get(ruta).then(response => {
                //this.categorias = Object.values(response.data);
                // const objectArray = Object.values(response.data);
                // objectArray.forEach((item) => {
                //     this.categorias.push(item.nombre);
                // });
                console.log(response.data)
                this.tipos = response.data;
            })
                .catch(error => {
                    console.log(error);
                });
        },

        computed: {
            tituloFormulario() {
                return this.editedIndex === -1 ? 'Nueva Tipo de Producto' :
                    this.editedIndex === 0 ? 'Editar Tipo de Producto' :
                        'Eliminar Tipo de Producto'
            },

            textoGuardar() {
                return this.editedIndex === 1 ? "Sí, Eliminar" : "Guardar"
            }
        },

        watch: {
            search(val) {
                val && val !== this.select && this.querySelections(val)
            },

            select() {
                this.select != null ? this.editedItem = this.select : this.editedItem = this.defaultItem
                if (this.select != null){
                    this.$store.commit(
                        'setTipoProductoPresentacion',
                        {index : this.index, tipo_producto : this.select.nombre})
                }else{
                    this.$store.commit(
                        'setTipoProductoPresentacion',
                        {index : this.index, tipo_producto : ''})
                }
            }
        },

        methods: {

            setTipoProducto(value){
                this.$store.commit('setTipoProductoPresentacion', value)
            },

            agregarTipoProducto() {
                this.editedItem = this.defaultItem
                this.dialog = true
            },

            editarTipoProducto() {
                this.editedIndex = 0
                if (this.select != null) {
                    this.editedItem = this.select
                    this.dialog = true
                }
            },

            eliminarTipoProducto() {
                // el número 1 en editedItem indica que se a a eliminar el elemento
                if (this.select != null) {
                    this.editedIndex = 1
                    this.editedItem = this.select
                    this.dialog = true
                }
            },

            cerrar() {
                this.editedIndex = -1
                this.editedItem = this.defaultItem
                this.dialog = false
            },

            guardar() {
                if (this.editedIndex === -1) {
                    const ruta = 'http://localhost:8000/api/v1.0/tipo-producto/'
                    axios.post(ruta, this.editedItem).then((response) => {
                        this.tipos.push(response.data);
                    }).catch((error) => {
                        console.log(error);
                    });

                } else if (this.editedIndex === 0) {
                    const ruta = "http://127.0.0.1:8000/api/v1.0/tipo-producto/" + this.editedItem.id + "/"
                    axios.put(ruta, this.editedItem).then(response => {
                        Object.assign(this.tipos[this.tipos.indexOf(this.editedItem)], response.data)
                    })
                        .catch(error => {
                            console.log(error);
                        });

                } else {
                    const ruta = "http://localhost:8000/api/v1.0/tipo-producto/" + this.editedItem.id + "/";
                    axios.delete(ruta).then((response) => {
                        console.log(response.data);
                    }).catch((error) => {
                        console.log(error);
                    });
                    const index = this.tipos.indexOf(this.editedItem)
                    this.tipos.splice(index, 1)
                }
                this.select = this.defaultItem
                this.editedIndex = -1
                this.editedItem = this.defaultItem
                this.dialog = false
            }
        }
    }
</script>