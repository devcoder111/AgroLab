<template>
    <v-card
            class="mx-8 my-4"
    >
        <v-card-title>
            {{index+1}}
        </v-card-title>
        <v-card-text>
            <v-container>
                <v-row>
                    <v-col cols="12" sm="12" md="8">
                        <v-text-field
                                v-model="nombre"
                                hint="Nombre Presentación"
                                solo
                                persistent-hint
                        ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="2">
                        <v-text-field
                                v-model="precio_compra"
                                hint="Precio Compra"
                                solo
                                persistent-hint
                        ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="2">
                        <v-text-field
                                v-model="precio_venta"
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
                        :index="index"
                ></mapp-sub-presentaciones>
            </v-container>
        </v-card-text>
        <v-card-actions>
            <v-btn
                    @click="agregarPresentacion"
                    icon
            >
                <v-icon>mdi-plus</v-icon>
            </v-btn>
            <v-btn
                    @click="eliminarPresentacion"
                    icon
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
        props: ['index'],
        data() {
            return {
                sub_presentaciones: false
            }
        },

        computed: {
            producto() {
                return this.$store.state.producto
            },

            nombre : {
                get(){
                    return this.$store.state.producto.presentaciones[this.index].nombre
                },
                set(value){
                    this.$store.commit('setNombrePresentacion',{index : this.index, nombre: value})
                }
            },

            precio_compra : {
                get(){
                    return this.$store.state.producto.presentaciones[this.index].precio_compra
                },
                set(value){
                    this.$store.commit(
                        'setPrecioCompraPresentacion',
                        {index : this.index, precio_compra : value})
                }
            },

            precio_venta : {
                get(){
                    return this.$store.state.producto.presentaciones[this.index].precio_venta
                },
                set(value){
                    this.$store.commit(
                        'setPrecioVentaPresentacion',
                        {index : this.index, precio_venta : value})
                }
            },
        },

        watch :{
          sub_presentaciones(){
              if (this.sub_presentaciones){
                  this.$store.commit('setMedidasPresentacion',{index : this.index, medidas : {}})
                  this.$store.commit('agregarSubPresentacion',
                      {index: this.index})
              }else{
                  this.$store.commit('eliminarMedidasPresentacion', {index : this.index})
                  this.$store.commit('eliminarSubPresentaciones',{index : this.index})
              }
          }
        },

        methods : {
            agregarPresentacion() {
                this.$store.commit('agregarPresentacionVacia')
            },
            eliminarPresentacion(){
                this.$store.commit('eliminarPresentacion', {index : this.index})
            }
        },

        components: {
            'mappSubPresentaciones': SubPresentaciones
        }
    }
</script>

<style scoped>

</style>