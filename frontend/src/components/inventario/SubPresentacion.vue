<template>
    <v-container fluid>
        <v-row>
            <v-col cols="12" sm="12" md="12" class="px-0">
                <v-card
                        v-bind:style="{backgroundColor : colorFondo}"
                >
                    <v-card-title>
                        {{index+1}}
                    </v-card-title>
                    <v-card-text>
                        <v-container>
                            <v-row>
                                <v-col cols="12" sm="12" md="6">
                                    <v-text-field
                                            v-model="nombreSubPresentacion"
                                            hint="Nombre Descriptivo"
                                            solo
                                            persistent-hint
                                    ></v-text-field>
                                </v-col>
                                <v-col cols="12" sm="6" md="6">
                                    <mapp-unidad-medida-producto
                                        @getDato="setUnidadMedidaSubPresentacion"
                                    ></mapp-unidad-medida-producto>
                                </v-col>
                                <v-col cols="12" sm="6" md="6">
                                    <v-text-field
                                            v-model="cantidad_unitaria"
                                            hint="Cantidad"
                                            solo
                                            persistent-hint
                                    ></v-text-field>
                                </v-col>
                                <v-col cols="12" sm="6" md="6">
                                    <v-text-field
                                            v-model="precio_unidad"
                                            hint="Precio Unitario"
                                            solo
                                            persistent-hint
                                    ></v-text-field>
                                </v-col>
                            </v-row>

                        </v-container>
                    </v-card-text>
                    <v-card-actions>
                        <v-btn icon
                               @click="agregarSubPresentacion()">
                            <v-icon>mdi-plus</v-icon>
                        </v-btn>
                        <v-btn icon>
                            <v-icon
                                    @click="eliminarSubPresentacion()"
                            >mdi-delete
                            </v-icon>
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-col>
        </v-row>
    </v-container>

</template>

<script>
    import UnidadDeMedida from "./UnidadDeMedida";

    export default {
        name: "SubPresentacion",
        props: ['item', 'index', 'index_presentacion'],
        methods: {
            agregarSubPresentacion() {
                this.$store.commit('agregarSubPresentacion', {index: this.index_presentacion})
            },

            eliminarSubPresentacion() {
                this.$store.commit('eliminarSubPresentacion',
                    {index_presentacion: this.index_presentacion, index: this.index})
            },

            setUnidadMedidaSubPresentacion(e){
                this.$store.commit('setUnidadMedidaSubPresentacion',
                    {index_presentacion : this.index_presentacion,
                            index : this.index,
                            unidad_medida : e})
            }
        },
        computed: {
            colorFondo() {
                if (this.index_presentacion % 2 == 0) {
                    return '#BDE4A7'
                } else {
                    return '#9FBBCC'
                }
            },
            nombreSubPresentacion: {
                get() {
                    return this.$store.state.producto
                        .presentaciones[this.index_presentacion]
                        .detalle_unitario[this.index].nombre_sub_presentacion
                },
                set(value) {
                    this.$store.commit('setNombreSubPresentacion',
                        {index_presentacion: this.index_presentacion,
                                index: this.index,
                                nombre_sub_presentacion : value})
                }
            },

            cantidad_unitaria: {
                get() {
                    return this.$store.state.producto
                        .presentaciones[this.index_presentacion]
                        .detalle_unitario[this.index].cantidad_unitaria
                },
                set(value) {
                    this.$store.commit('setCantidadUnitariaSubPresentacion',
                        {index_presentacion: this.index_presentacion,
                                index: this.index,
                                cantidad_unitaria : value})
                }
            },

            precio_unidad: {
                get() {
                    return this.$store.state.producto
                        .presentaciones[this.index_presentacion]
                        .detalle_unitario[this.index].precio_unidad
                },
                set(value) {
                    this.$store.commit('setPrecioUnidadSubPresentacion',
                        {index_presentacion: this.index_presentacion,
                                index: this.index,
                                precio_unidad : value})
                }
            },
        },
        components: {
            mappUnidadMedidaProducto: UnidadDeMedida
        }
    }
</script>
<style scoped>

</style>