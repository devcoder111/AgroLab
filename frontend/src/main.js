import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify';
import Vuex from 'vuex'

Vue.config.productionTip = false
Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
        producto: {
            nombre: '',
            categoria: '',
            proveedor: '',
            acciones: [],
            aplicaciones: [],
            presentaciones: [
                {
                    nombre: '',
                    precio_compra: 0,
                    precio_venta: 0,
                    lotes: [],
                    medidas: {
                        tipo_producto: '',
                        unidad_medida: '',
                        cantidad_medida: 0
                    },
                    detalle_unitario: []
                }
            ],
        },

        default_producto: {
            nombre: '',
            categoria: '',
            proveedor: '',
            acciones: [],
            aplicaciones: [],
            presentaciones: [
                {
                    nombre: '',
                    precio_compra: 0,
                    precio_venta: 0,
                    lotes: [
                        {
                            vencimiento: '',
                            existencia: ''
                        }
                    ],
                    medidas: {
                        tipo_producto: '',
                        unidad_medida: '',
                        cantidad_medida: 0
                    },
                    detalle_unitario: [
                        {
                            cantidad_unitaria: 0,
                            nombre_sub_presentacion: '',
                            unidad_medida: '',
                            precio_unidad: 0
                        }
                    ]
                }
            ],
        }
    },
    mutations: {
        setProducto(state, producto){
          state.producto = producto
        },

        setNombreProducto(state, nombre) {
            state.producto.nombre = nombre
        },

        setCategoriaProducto(state, categoria) {
            state.producto.categoria = categoria.nombre
        },

        setProveedorProducto(state, proveedor) {
            state.producto.proveedor = proveedor.nombre
        },

        setAccionesProducto(state, acciones) {
            var x = acciones.map(a => a.nombre)
            state.producto.acciones = x
        },

        setAplicacionesProducto(state, aplicaciones) {
            var x = aplicaciones.map(a => a.nombre)
            state.producto.aplicaciones = x
        },

        setPresentacionInicial(state) {
            state.producto.presentaciones = []
            state.producto.presentaciones.push({
                nombre: '',
                precio_compra: 0,
                precio_venta: 0,
                detalle_unitario: [],
                lotes : [],
                medidas : {
                    cantidad_medida : 0
                }
            })
        },

        agregarPresentacionVacia(state) {
            state.producto.presentaciones.push({
                nombre: '',
                precio_compra: 0,
                precio_venta: 0,
                detalle_unitario: [],
                lotes : [],
                medidas : {
                    cantidad_medida: 0
                }
            })
        },

        eliminarPresentacion(state, value){
            state.producto.presentaciones.splice(value.index, 1)
        },

        eliminarSubPresentacion(state, value){
            state.producto.presentaciones[value.index_presentacion].detalle_unitario.splice(value.index,1)
        },

        setNombrePresentacion(state, value) {
            state.producto.presentaciones[value.index].nombre = value.nombre
        },

        setPrecioCompraPresentacion(state, value) {
            var p_compra = parseFloat(value.precio_compra)
            state.producto.presentaciones[value.index].precio_compra = p_compra
        },

        setPrecioVentaPresentacion(state, value) {
            var p_venta = parseFloat(value.precio_venta)
            state.producto.presentaciones[value.index].precio_venta = p_venta
        },

        setMedidasPresentacion(state, value) {
            state.producto.presentaciones[value.index].medidas = value.medidas
        },

        eliminarMedidasPresentacion(state, value) {
            delete state.producto.presentaciones[value.index].medidas
        },

        setTipoProductoPresentacion(state, value) {
            state.producto.presentaciones[value.index].medidas.tipo_producto = value.tipo_producto
        },

        setUnidadMedidaPresentacion(state, value) {
            state.producto.presentaciones[value.index].medidas.unidad_medida = value.unidad_medida
        },

        setCantidadMedidaPresentacion(state, value) {
            var c_medida = parseFloat(value.cantidad_medida)
            state.producto.presentaciones[value.index].medidas.cantidad_medida =  c_medida
        },

        agregarSubPresentacion(state, value) {
            state.producto.presentaciones[value.index].detalle_unitario.push(
                {
                    cantidad_unitaria: 0,
                    nombre_sub_presentacion: '',
                    unidad_medida: '',
                    precio_unidad: 0
                }
            )
        },

        eliminarSubPresentaciones(state, value) {
            state.producto.presentaciones[value.index].detalle_unitario.length = 0
        },

        setNombreSubPresentacion(state, value){
            state.producto.presentaciones[value.index_presentacion].detalle_unitario[value.index]
                .nombre_sub_presentacion = value.nombre_sub_presentacion
        },

        setUnidadMedidaSubPresentacion(state, value){
            state.producto.presentaciones[value.index_presentacion].detalle_unitario[value.index]
                .unidad_medida = value.unidad_medida
        },

        setCantidadUnitariaSubPresentacion(state, value){
            state.producto.presentaciones[value.index_presentacion].detalle_unitario[value.index]
                .cantidad_unitaria = parseInt(value.cantidad_unitaria)
        },

        setPrecioUnidadSubPresentacion(state, value){
            state.producto.presentaciones[value.index_presentacion].detalle_unitario[value.index]
                .precio_unidad = parseInt(value.precio_unidad)
        },

        agregarLoteVacio(state, value){
            state.producto.presentaciones[value.index].lotes.push({
                existencia : '',
            })
        },

        eliminarSubLote(state, value){
            state.producto.presentaciones[value.index_presentacion].lotes.splice(value.index,1);
        },

        setFechaVencimientoLote(state, value){
            state.producto.presentaciones[value.index_presentacion]
                .lotes[value.index].fecha_vencimiento = value.fecha_vencimiento
        },

        deleteFechaFencimientoLote(state, value){
            delete state.producto.presentaciones[value.index_presentacion]
                .lotes[value.index].fecha_vencimiento
        },

        setExistenciaLote(state, value){
            state.producto.presentaciones[value.index_presentacion]
                .lotes[value.index].existencia = parseInt(value.existencia)
        }
    }
})

new Vue({
    router,
    vuetify,
    store,
    render: h => h(App)
}).$mount('#app')
