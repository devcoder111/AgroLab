<template>
    <v-card
            class="mx-8 my-4"
    >
        <v-card-text>
            <v-container>
                <v-switch
                        v-model="fecha_vencimiento"
                        class="mx-2"
                        label="¿El producto tiene Fecha de Vencimiento?">
                </v-switch>
                <v-row>
                    <v-col
                            v-if="fecha_vencimiento"
                            cols="12" sm="12" md="10">
                        <v-date-picker
                                v-model="picker"
                                landscape
                                full-width
                        ></v-date-picker>
                        <span class="title">Fecha Seleccionada: {{picker}}</span>
                    </v-col>

                    <v-col cols="12" sm="6" md="2">
                        <v-text-field
                                v-model="existencia"
                                hint="Existencia"
                                solo
                                persistent-hint
                        ></v-text-field>
                    </v-col>
                </v-row>
            </v-container>
        </v-card-text>
        <v-card-actions>
            <v-btn
                    icon
                    @click="agregarSubLote"
            >
                <v-icon>mdi-plus</v-icon>
            </v-btn>
            <v-btn
                    icon
                    @click="eliminarSubLote"
            >
                <v-icon>mdi-delete</v-icon>
            </v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>
    export default {
        name: "SubLote",
        props: ['lote', 'index', 'index_presentacion'],
        data() {
            return {
                fecha_vencimiento: false,
                picker: new Date().toISOString().substr(0, 10)
            }
        },

        created() {
            var fecha = this.$store.state.producto.presentaciones[this.index_presentacion]
                .lotes[this.index].fecha_vencimiento
            if (fecha != null) {
                if (fecha.length > 0) {
                    this.fecha_vencimiento = true
                    this.picker = new Date(fecha).toISOString().substr(0, 10);
                }
            }

        },

        computed: {
            existencia: {
                get() {
                    return this.$store.state.producto.presentaciones[this.index_presentacion]
                        .lotes[this.index].existencia
                },
                set(value) {
                    this.$store.commit('setExistenciaLote',
                        {
                            index_presentacion: this.index_presentacion,
                            index: this.index,
                            existencia: value
                        })
                }
            },
        },

        watch: {
            fecha_vencimiento() {
                if (!this.fecha_vencimiento) {
                    this.$store.commit('deleteFechaFencimientoLote',
                        {
                            index_presentacion: this.index_presentacion,
                            index: this.index
                        })
                } else {
                    this.$store.commit('setFechaVencimientoLote',
                        {
                            index_presentacion: this.index_presentacion,
                            index: this.index,
                            fecha_vencimiento: this.picker
                        })

                }
            },
            picker() {
                if (this.fecha_vencimiento) {
                    this.$store.commit('setFechaVencimientoLote',
                        {
                            index_presentacion: this.index_presentacion,
                            index: this.index,
                            fecha_vencimiento: this.picker
                        })
                }
            }
        },

        methods: {
            agregarSubLote() {
                this.$store.commit('agregarLoteVacio', {index: this.index_presentacion})
            },

            eliminarSubLote() {
                if (this.$store.state.producto.presentaciones[this.index_presentacion].lotes.length > 1) {
                    this.$store.commit('eliminarSubLote',
                        {
                            index_presentacion: this.index_presentacion,
                            index: this.index
                        })
                }
            }
        }
    }
</script>

<style scoped>

</style>