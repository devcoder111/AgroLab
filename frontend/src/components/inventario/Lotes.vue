<template>
    <v-card
    >
        <v-card-text>
            <mapp-lote
                    v-for="(presentacion, index) in presentaciones"
                    :key="index"
                    :presentacion="presentacion"
                    :index="index"
            ></mapp-lote>
        </v-card-text>
    </v-card>
</template>

<script>
    import Lote from "./Lote";

    export default {
        name: "Lotes",
        computed: {
            presentaciones() {
                return this.$store.state.producto.presentaciones
            }
        },
        components: {
            mappLote: Lote
        }
    }
</script>

<style scoped>

</style>