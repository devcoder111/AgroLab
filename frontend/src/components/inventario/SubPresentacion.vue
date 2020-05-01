<template>
    <v-container fluid>
        <v-row>
            <v-col cols="12" sm="12" md="12" class="px-0">
                <v-card
                        style="background-color: #E8EAF6"
                >
                    <v-card-text>
                        <v-container>
                            <v-row>
                                <v-col cols="12" sm="12" md="6">
                                    <v-text-field
                                            v-model="datos.nombre"
                                            hint="Nombre Descriptivo"
                                            solo
                                            persistent-hint
                                    ></v-text-field>
                                </v-col>
                                <v-col cols="12" sm="6" md="6">
                                    <mapp-unidad-medida-producto></mapp-unidad-medida-producto>
                                </v-col>
                                <v-col cols="12" sm="6" md="6">
                                    <v-text-field
                                            hint="Cantidad"
                                            solo
                                            persistent-hint
                                    ></v-text-field>
                                </v-col>
                                <v-col cols="12" sm="6" md="6">
                                    <v-text-field
                                            hint="Precio Unitario"
                                            solo
                                            persistent-hint
                                    ></v-text-field>
                                </v-col>
                            </v-row>

                        </v-container>
                    </v-card-text>
                    <v-card-actions>
                        <v-btn icon @click="$emit('agregarSubPresentacion')">
                            <v-icon>mdi-plus</v-icon>
                        </v-btn>
                        <v-btn icon @click="$emit('eliminarSubPresentacion',index)">
                            <v-icon>mdi-delete</v-icon>
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
        props: ['datos', 'index'],
        components: {
            mappUnidadMedidaProducto: UnidadDeMedida
        }
    }
</script>

<style scoped>

</style>