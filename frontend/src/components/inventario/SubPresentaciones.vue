<template>
    <v-card>
        <v-card-title>Medidas del Producto</v-card-title>
        <v-card-text>
            <v-container fluid>
                <v-row>
                    <v-col cols="12" sm="12" md="5">
                        <mapp-tipo-producto></mapp-tipo-producto>
                    </v-col>
                    <v-col cols="12" sm="12" md="5">
                        <mapp-unidad-medida></mapp-unidad-medida>
                    </v-col>
                    <v-col cols="12" sm="12" md="2">
                        <v-text-field
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
                                    v-for="(sub, index) in subPresentaciones"
                                    :key="index"
                                    :index="index"
                                    :datos="sub"
                                    @agregarSubPresentacion="agregarSubPresentacion"
                                    @eliminarSubPresentacion="eliminarSubPresentacion(index)"
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
    import UnidadDeMedida from "./UnidadDeMedida";
    import SubPresentacion from "./SubPresentacion";

    export default {
        name: "SubPresentaciones",
        data() {
            return {
                subPresentaciones: [],
            }
        },

        created() {
            this.subPresentaciones.push({
                    nombre: '',
                    unidadMedida: '',
                    cantidad: 0,
                    precioUnitario: 0
                })
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
                if(this.subPresentaciones.length > 1)
                    this.subPresentaciones.splice(index,1)
            }
        },
        components: {
            mappTipoProducto: TipoProducto,
            mappUnidadMedida: UnidadDeMedida,
            mappSubPresentacion: SubPresentacion
        }
    }
</script>

<style scoped>

</style>