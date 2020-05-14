<template>
    <v-card
            class="mx-8 my-4"
    >
        <v-card-text>
            {{presentaciones}}
            <v-container>
                <span class="title">Fecha de Vencimiento</span> {{picker}}
                <v-row>
                    <v-col cols="12" sm="12" md="10">
                        <v-date-picker
                                v-model="picker"
                                landscape
                                full-width
                        ></v-date-picker>
                    </v-col>
                    <v-col cols="12" sm="6" md="2">
                        <v-text-field
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
                    @click="$emit('agregarLote')"
            >
                <v-icon>mdi-plus</v-icon>
            </v-btn>
            <v-btn
                    icon
                    @click="$emit('eliminarLote',index)"
            >
                <v-icon>mdi-delete</v-icon>
            </v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>
    export default {
        name: "Lote",
        props: ['datos', 'index'],
        data() {
            return {
                picker: new Date().toISOString().substr(0, 10)
            }
        },

        computed : {
            presentaciones(){
                return this.$store.state.producto.presentaciones
            }
        }
    }
</script>

<style scoped>

</style>