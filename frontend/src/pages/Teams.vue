<template>
    <div class="teams-container">
        <el-card>
            <template #header>
                <div class="card-header">
                    <span>球队管理</span>
                    <el-button type="primary" @click="showAddDialog">添加球队</el-button>
                </div>
            </template>

            <el-table :data="teams" stripe>
                <el-table-column prop="name" label="球队名称" width="150" />
                <el-table-column prop="home_ground" label="主场" width="150" />
                <el-table-column prop="founded_year" label="成立年份" width="120" />
                <el-table-column label="操作" width="200">
                    <template #default="{ row }">
                        <el-button size="small" @click="handleEdit(row)">编辑</el-button>
                        <el-button size="small" type="danger" @click="handleDelete(row.id)">删除</el-button>
                    </template>
                </el-table-column>
            </el-table>

            <el-pagination :current-page="pagination.page" :page-size="pagination.limit" :total="pagination.total"
                @current-change="handlePageChange" style="margin-top: 20px" />
        </el-card>

        <!-- 添加/编辑对话框 -->
        <el-dialog v-model="dialogVisible" :title="dialogTitle">
            <el-form :model="formData" label-width="100px">
                <el-form-item label="球队名称">
                    <el-input v-model="formData.name" />
                </el-form-item>
                <el-form-item label="主场">
                    <el-input v-model="formData.home_ground" />
                </el-form-item>
                <el-form-item label="成立年份">
                    <el-input-number v-model="formData.founded_year" />
                </el-form-item>
                <el-form-item label="简介">
                    <el-input v-model="formData.description" type="textarea" rows="3" />
                </el-form-item>
            </el-form>
            <template #footer>
                <span class="dialog-footer">
                    <el-button @click="dialogVisible = false">取消</el-button>
                    <el-button type="primary" @click="handleSave">保存</el-button>
                </span>
            </template>
        </el-dialog>
    </div>
</template>

<script setup>
import { ref } from "vue";
import { ElMessage, ElMessageBox } from "element-plus";

const teams = ref([
    {
        id: 1,
        name: "皇家马德里",
        home_ground: "圣地亚哥伯纳乌球场",
        founded_year: 1902,
    },
    {
        id: 2,
        name: "利物浦",
        home_ground: "安菲尔德球场",
        founded_year: 1892,
    },
]);

const dialogVisible = ref(false);
const dialogTitle = ref("");
const editingId = ref(null);

const formData = ref({
    name: "",
    home_ground: "",
    founded_year: null,
    description: "",
});

const pagination = ref({
    page: 1,
    limit: 10,
    total: teams.value.length,
});

const showAddDialog = () => {
    dialogTitle.value = "添加球队";
    editingId.value = null;
    formData.value = {
        name: "",
        home_ground: "",
        founded_year: null,
        description: "",
    };
    dialogVisible.value = true;
};

const handleEdit = (row) => {
    dialogTitle.value = "编辑球队";
    editingId.value = row.id;
    formData.value = { ...row };
    dialogVisible.value = true;
};

const handleSave = () => {
    if (editingId.value) {
        const index = teams.value.findIndex((t) => t.id === editingId.value);
        if (index !== -1) {
            teams.value[index] = { ...formData.value, id: editingId.value };
        }
    } else {
        teams.value.push({
            id: Math.max(...teams.value.map((t) => t.id), 0) + 1,
            ...formData.value,
        });
    }
    dialogVisible.value = false;
    ElMessage.success("保存成功");
};

const handleDelete = (id) => {
    ElMessageBox.confirm("确认删除此球队吗?", "警告", {
        confirmButtonText: "确认",
        cancelButtonText: "取消",
        type: "warning",
    })
        .then(() => {
            const index = teams.value.findIndex((t) => t.id === id);
            if (index !== -1) {
                teams.value.splice(index, 1);
                ElMessage.success("删除成功");
            }
        })
        .catch(() => {
            ElMessage.info("已取消删除");
        });
};

const handlePageChange = (page) => {
    pagination.value.page = page;
};
</script>

<style scoped>
.teams-container {
    padding: 20px;
}

.card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.dialog-footer {
    text-align: right;
}
</style>
