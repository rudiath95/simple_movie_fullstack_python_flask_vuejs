import Vue from "vue";
import VueRouter from "vue-router";
import GenreList from "../components/GenreList.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/genre",
    name: "GenreList",
    component: GenreList,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
