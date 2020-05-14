<template>
    <v-card
            class="mx-8 my-4"
    >
        <v-card-text>
            <v-container>
                <v-row>
                    <v-text-field
                            v-model="presentacion.nombre"
                            hint="Nombre Presentacion"
                            solo
                            readonly
                            persistent-hint
                    ></v-text-field>
                </v-row>
                <mapp-sub-lote
                        v-for="(sub,index) in subLotes"
                        :key="index"
                        :lote="sub"
                        :index="index"
                        :index_presentacion="index_presentacion"
                    ></mapp-sub-lote>

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
    import SubLote from './SubLote'

    export default {
        name: "Lote",
        props: ['presentacion', 'index'],
        data() {
            return {}
        },

        computed: {
            subLotes() {
              return this.$store.state.producto.presentaciones[this.index].lotes
            },
            index_presentacion(){
                return this.$store.state.producto.presentaciones.indexOf(this.presentacion)
            }
        },

        created() {
            this.$store.commit('agregarLoteVacio', {index: this.index})
        },
        components: {
            mappSubLote: SubLote
        }
    }
</script>

<style scoped>

</style>