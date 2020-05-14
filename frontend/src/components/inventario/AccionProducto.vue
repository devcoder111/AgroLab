<template>
    <v-card
            tile
            class="px-2"
    >
        <v-row>
            <v-col cols="12" sm="12" md="6" lg="4" class="py-0 text-center">
                <v-btn class="ma-2" fab small dark color="primary" @click="agregarAccion">
                    <v-icon dark>mdi-plus</v-icon>
                </v-btn>
                <v-btn class="ma-2" fab small dark color="warning" @click="editarAccion">
                    <v-icon dark>mdi-pencil</v-icon>
                </v-btn>
                <v-btn class="ma-2" fab small dark color="error" @click="eliminarAccion">
                    <v-icon dark>mdi-delete</v-icon>
                </v-btn>
            </v-col>
            <v-col cols="12" sm="12" md="6" lg="8" class="py-0">
                <v-autocomplete
                        v-model="values"
                        :items="items"
                        chips
                        small-chips
                        multiple
                        persistent-hint
                        hint="Acciones"
                        return-object
                        item-text="nombre"
                        @change="setAcciones(values)"
                ></v-autocomplete>
            </v-col>
        </v-row>
        <v-dialog
                v-model="dialog"
                max-width="350"
        >
            <v-card>
                <v-card-title>
                    <span class="title">{{tituloFormulario}}</span>
                </v-card-title>
                <v-card-text>
                    <span
                            v-if="editedIndex === 1"
                            class="subtitle-2">
                        ¿Está seguro que desea eliminar la acción ?
                    </span>
                    <v-text-field
                            v-if="editedIndex != 1"
                            v-model="editedItem.nombre"
                            hint="Acción"
                            solo
                            persistent-hint
                    ></v-text-field>
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn
                            color="error"
                            text
                            @click="cerrar"
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
        name: "AccionProducto",
        data: () => ({
            items: [],
            value: null,
            values : [],
            dialog: false,
            defaultItem: {
                id: '',
                nombre: ''
            },
            editedItem: {
                id: '',
                nombre: ''
            },
            editedIndex: null
        }),

        created() {
            const ruta = 'http://localhost:8000/api/v1.0/accion-producto/'
            axios.get(ruta).then(response => {
                //this.categorias = Object.values(response.data);
                // const objectArray = Object.values(response.data);
                // objectArray.forEach((item) => {
                //     this.categorias.push(item.nombre);
                // });
                this.items = response.data;
            })
                .catch(error => {
                    console.log(error);
                });
        },

        computed: {
            tituloFormulario() {
                return this.editedIndex === -1 ? 'Agregar Acción' :
                    this.editedIndex === 0 ? 'Editar Acción' :
                        'Eliminar Acción'
            },

            textoGuardar() {
                return this.editedIndex === 1 ? 'Sí, Eliminar' : "Guardar"
            },

            // acciones : {
            //     get(){
            //         return this.$store.state.producto.acciones
            //     },
            //     set(value){
            //         this.$store.commit('setAccionesProducto',value)
            //     }
            // },
        },

        methods: {
            setAcciones(acciones){
              this.$store.commit('setAccionesProducto',acciones)
            },

            agregarAccion() {
                this.editedIndex = -1
                this.editedItem = this.defaultItem
                this.dialog = true
            },
            editarAccion() {
                this.editedIndex = 0
                if (this.values.length === 1) {
                    this.editedItem = this.values[0]
                    this.dialog = true
                }

            },
            eliminarAccion() {
                this.editedIndex = 1
                if (this.values.length === 1){
                    this.editedItem = this.values[0]
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
                    const ruta = 'http://localhost:8000/api/v1.0/accion-producto/'
                    axios.post(ruta, this.editedItem).then((response) => {
                        this.items.push(response.data)
                    }).catch((error) => {
                        console.log(error);
                    });
                } else if (this.editedIndex === 0) {
                    const ruta = "http://127.0.0.1:8000/api/v1.0/accion-producto/" + this.editedItem.id + "/"
                    axios.put(ruta, this.editedItem).then(response => {
                        Object.assign(this.items[this.items.indexOf(this.editedItem)], response.data)
                    })
                        .catch(error => {
                            console.log(error);
                        });
                    this.values = []
                    this.setAcciones([])
                } else {
                    const ruta = "http://localhost:8000/api/v1.0/accion-producto/" + this.editedItem.id + "/";
                    axios.delete(ruta).then((response) => {
                        console.log(response)
                    }).catch((error) => {
                        console.log(error);
                    });
                    const index = this.items.indexOf(this.editedItem)
                    this.items.splice(index, 1)
                    this.values = []
                    this.setAcciones([])
                }
                this.editedIndex = -1
                this.editedItem = this.defaultItem
                this.dialog = false
            }
        }
    }
</script>

<style scoped>

</style>