import Vue from "vue";
import VueRouter from "vue-router";
import Shark from "../components/Shark.vue";
import Genre from "../components/Genre.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/shark",
    name: "Shark",
    component: Shark,
  },
  {
    path: "/genre",
    name: "Genre",
    component: Genre,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
