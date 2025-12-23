import { createRouter, createWebHistory } from "vue-router";
import { useUserStore } from "../stores/userStore";

const routes = [
    {
        path: "/",
        redirect: "/dashboard",
    },
    {
        path: "/login",
        name: "Login",
        component: () => import("../pages/Login.vue"),
    },
    {
        path: "/dashboard",
        name: "Dashboard",
        component: () => import("../pages/Dashboard.vue"),
        meta: { requiresAuth: true },
    },
    {
        path: "/teams",
        name: "Teams",
        component: () => import("../pages/Teams.vue"),
        meta: { requiresAuth: true },
    },
    {
        path: "/players",
        name: "Players",
        component: () => import("../pages/Players.vue"),
        meta: { requiresAuth: true },
    },
    {
        path: "/competitions",
        name: "Competitions",
        component: () => import("../pages/Competitions.vue"),
        meta: { requiresAuth: true },
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

// 路由守卫
router.beforeEach((to, from, next) => {
    const userStore = useUserStore();

    if (to.meta.requiresAuth && !userStore.user) {
        next("/login");
    } else {
        next();
    }
});

export default router;
