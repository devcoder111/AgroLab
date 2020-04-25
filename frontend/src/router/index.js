import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Proveedores from "../components/inventario/Proveedores";
import Productos from "../components/inventario/Productos";

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/proveedores',
    name: 'Proveedores',
    component: Proveedores
  },
  {
    path: '/proveedores/:proveedorId',
    name: 'Proveedores',
    component: Proveedores
  },
  {
    path: '/productos',
    name: 'Productos',
    component: Productos
  },
  {
    path: '/categorias-producto/:categoriaId',
    name: 'Categoria',
    component: Productos
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
