import { defineStore } from "pinia";
import { ref } from "vue";
import api from "../api/client";

export const useUserStore = defineStore("user", () => {
    const user = ref(null);
    const token = ref(localStorage.getItem("access_token") || null);

    const setUser = (userData) => {
        user.value = userData;
    };

    const setToken = (accessToken) => {
        token.value = accessToken;
        localStorage.setItem("access_token", accessToken);
    };

    const login = async (username, password) => {
        try {
            const response = await api.post("/auth/login", {
                username,
                password,
            });
            setToken(response.data.access_token);
            setUser({ username });
            return true;
        } catch (error) {
            console.error("登录失败:", error);
            return false;
        }
    };

    const logout = () => {
        user.value = null;
        token.value = null;
        localStorage.removeItem("access_token");
    };

    const loadUser = () => {
        if (token.value) {
            setUser({ username: localStorage.getItem("username") || "User" });
        }
    };

    return {
        user,
        token,
        setUser,
        setToken,
        login,
        logout,
        loadUser,
    };
});
