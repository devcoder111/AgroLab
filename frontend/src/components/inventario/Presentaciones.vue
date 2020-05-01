<template>
    <v-card
            class="mx-8 my-4"
    >
        <v-card-text>
            <v-container>
                <v-row>
                    <v-col cols="12" sm="12" md="8">
                        <v-text-field
                                v-model="datos.nombre"
                                hint="Nombre Presentación"
                                solo
                                persistent-hint
                        ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="2">
                        <v-text-field
                                v-model="datos.precio_compra"
                                hint="Precio Compra"
                                solo
                                persistent-hint
                        ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="2">
                        <v-text-field
                                v-model="datos.precio_venta"
                                hint="Precio Venta"
                                solo
                                persistent-hint
                        ></v-text-field>
                    </v-col>
                </v-row>
                <v-divider
                ></v-divider>
                <v-switch
                        v-model="sub_presentaciones"
                        class="mx-2"
                        label="Esta presentación se vende por partes">
                </v-switch>
                <mapp-sub-presentaciones
                        v-if="sub_presentaciones"
                ></mapp-sub-presentaciones>
            </v-container>
        </v-card-text>
        <v-card-actions>
             <v-btn
                     icon
                     @click="$emit('agregarPresentacion')"
             >
                    <v-icon>mdi-plus</v-icon>
                </v-btn>
                <v-btn
                        icon
                        @click="$emit('eliminarPresentacion',index)"
                >
                    <v-icon>mdi-delete</v-icon>
                </v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>
    import SubPresentaciones from "./SubPresentaciones";

    export default {
        name: "Presentaciones",
        props: ['datos', 'index'],
        data() {
            return {
                sub_presentaciones: false
            }
        },
        components: {
            'mappSubPresentaciones': SubPresentaciones
        }
    }
</script>

<style scoped>

</style>