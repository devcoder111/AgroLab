<template>
    <v-card>
        <v-card-title>Medidas del Producto</v-card-title>
        <v-card-text>
            <v-container fluid>
                <v-row>
                    <v-col cols="12" sm="12" md="5">
                        <mapp-tipo-producto
                                :index="index"
                        ></mapp-tipo-producto>
                    </v-col>
                    <v-col cols="12" sm="12" md="5">
                        <mapp-Unidad-Medida-Presentacion
                            :index="index"
                        >
                        </mapp-Unidad-Medida-Presentacion>
                    </v-col>
                    <v-col cols="12" sm="12" md="2">
                        <v-text-field
                                v-model="cantidad_medida"
                                hint="Cantidad"
                                solo
                                persistent-hint
                        ></v-text-field>
                    </v-col>
                    <v-card>
                        <v-card-title>
                            Sub Presentaciones
                        </v-card-title>
                        <v-card-text>
                            <mapp-sub-presentacion
                                    v-for="(sub, i) in sub_presentaciones"
                                    :key="i"
                                    :index_presentacion="index"
                                    :index="i"
                                    :item="sub"
                            ></mapp-sub-presentacion>
                        </v-card-text>
                    </v-card>
                </v-row>
            </v-container>
        </v-card-text>
    </v-card>
</template>

<script>
    import TipoProducto from "./TipoProducto";
    import UnidadMedidaPresentacion from "./UnidadDeMedidaPresentacion";
    import SubPresentacion from "./SubPresentacion";

    export default {
        props: ['index'],
        name: "SubPresentaciones",
        created() {
            //this.$store.commit('setDetalleUnitarioPresentacion', {index : this.index})
        },
        computed: {
            sub_presentaciones: {
                get() {
                    return this.$store.state.producto.presentaciones[this.index].detalle_unitario
                }
            },
            cantidad_medida: {
                get() {
                    return this.$store.state.producto.presentaciones[this.index].medidas.cantidad_medida
                },
                set(value) {
                    this.$store.commit('setCantidadMedidaPresentacion',
                        {index: this.index, cantidad_medida: value})
                }
            }
        },

        methods: {
            agregarSubPresentacion() {
                this.subPresentaciones.push({
                    nombre: '',
                    unidadMedida: '',
                    cantidad: 0,
                    precioUnitario: 0
                })
            },
            eliminarSubPresentacion(index) {
                if (this.subPresentaciones.length > 1)
                    this.subPresentaciones.splice(index, 1)
            },

        },
        components: {
            mappTipoProducto: TipoProducto,
            mappUnidadMedidaPresentacion: UnidadMedidaPresentacion,
            mappSubPresentacion: SubPresentacion
        }
    }
</script>

<style scoped>

</style>