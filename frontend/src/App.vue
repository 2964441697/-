<template>
    <el-container class="app-container">
        <el-header class="app-header">
            <div class="header-content">
                <h1>⚽ 足球管理系统</h1>
                <div class="header-actions">
                    <el-dropdown v-if="userStore.user">
                        <span class="el-dropdown-link">
                            {{ userStore.user.username }}
                            <el-icon class="el-icon--right">
                                <arrow-down />
                            </el-icon>
                        </span>
                        <template #dropdown>
                            <el-dropdown-menu>
                                <el-dropdown-item @click="logout">退出登录</el-dropdown-item>
                            </el-dropdown-menu>
                        </template>
                    </el-dropdown>
                    <el-button v-else type="primary" @click="$router.push('/login')">登录</el-button>
                </div>
            </div>
        </el-header>
        <el-container>
            <el-aside v-if="userStore.user" width="200px" class="app-aside">
                <el-menu :default-active="$route.path" @select="handleMenuSelect" class="el-menu-vertical">
                    <el-menu-item index="/dashboard">
                        <el-icon>
                            <Management />
                        </el-icon>
                        <span>仪表盘</span>
                    </el-menu-item>
                    <el-menu-item index="/teams">
                        <el-icon>
                            <Grid />
                        </el-icon>
                        <span>球队管理</span>
                    </el-menu-item>
                    <el-menu-item index="/players">
                        <el-icon>
                            <User />
                        </el-icon>
                        <span>球员管理</span>
                    </el-menu-item>
                    <el-menu-item index="/competitions">
                        <el-icon>
                            <Trophy />
                        </el-icon>
                        <span>赛事管理</span>
                    </el-menu-item>
                </el-menu>
            </el-aside>
            <el-main class="app-main">
                <router-view />
            </el-main>
        </el-container>
    </el-container>
</template>

<script setup>
import { useRouter } from "vue-router";
import { useUserStore } from "./stores/userStore";

const router = useRouter();
const userStore = useUserStore();

const handleMenuSelect = (index) => {
    router.push(index);
};

const logout = () => {
    userStore.logout();
    router.push("/login");
};
</script>

<style scoped>
.app-container {
    height: 100vh;
}

.app-header {
    background-color: #1f2937;
    color: white;
    padding: 0 20px;
    display: flex;
    align-items: center;
}

.header-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
}

.header-content h1 {
    margin: 0;
    font-size: 24px;
}

.header-actions {
    display: flex;
    gap: 10px;
}

.el-dropdown-link {
    cursor: pointer;
    color: white;
}

.app-aside {
    background-color: #f5f7fa;
    border-right: 1px solid #dcdfe6;
}

.app-main {
    padding: 20px;
    background-color: #f5f7fa;
}
</style>
