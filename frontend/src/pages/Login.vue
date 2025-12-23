<template>
    <div class="login-container">
        <el-card class="login-card">
            <template #header>
                <div class="card-header">
                    <span>⚽ 足球管理系统登录</span>
                </div>
            </template>

            <el-form ref="formRef" :model="form" :rules="rules" @submit.prevent="handleLogin">
                <el-form-item label="用户名" prop="username">
                    <el-input v-model="form.username" placeholder="请输入用户名" @keyup.enter="handleLogin" />
                </el-form-item>

                <el-form-item label="密码" prop="password">
                    <el-input v-model="form.password" type="password" placeholder="请输入密码" @keyup.enter="handleLogin" />
                </el-form-item>

                <el-form-item>
                    <el-button type="primary" @click="handleLogin" :loading="loading" style="width: 100%">
                        登录
                    </el-button>
                </el-form-item>

                <el-form-item>
                    <el-button @click="handleRegister" style="width: 100%">
                        注册新账户
                    </el-button>
                </el-form-item>
            </el-form>
        </el-card>
    </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useUserStore } from "../stores/userStore";
import { ElMessage } from "element-plus";

const router = useRouter();
const userStore = useUserStore();

const form = ref({
    username: "",
    password: "",
});

const loading = ref(false);

const rules = {
    username: [
        { required: true, message: "用户名不能为空", trigger: "blur" },
    ],
    password: [
        { required: true, message: "密码不能为空", trigger: "blur" },
    ],
};

const handleLogin = async () => {
    loading.value = true;
    const success = await userStore.login(form.value.username, form.value.password);
    loading.value = false;

    if (success) {
        ElMessage.success("登录成功");
        router.push("/dashboard");
    } else {
        ElMessage.error("登录失败，请检查用户名和密码");
    }
};

const handleRegister = () => {
    ElMessage.info("注册功能开发中...");
};
</script>

<style scoped>
.login-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.login-card {
    width: 400px;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

.card-header {
    font-size: 20px;
    font-weight: bold;
}
</style>
