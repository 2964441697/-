<template>
    <div class="players-container">
        <el-card>
            <template #header>
                <div class="card-header">
                    <span>球员管理</span>
                    <el-button type="primary" @click="showAddDialog">添加球员</el-button>
                </div>
            </template>

            <el-table :data="players" stripe>
                <el-table-column prop="name" label="姓名" width="120" />
                <el-table-column prop="position" label="位置" width="100" />
                <el-table-column prop="jersey_number" label="号码" width="80" />
                <el-table-column prop="height" label="身高(cm)" width="100" />
                <el-table-column prop="weight" label="体重(kg)" width="100" />
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
                <el-form-item label="姓名">
                    <el-input v-model="formData.name" />
                </el-form-item>
                <el-form-item label="位置">
                    <el-select v-model="formData.position" placeholder="选择位置">
                        <el-option label="门将" value="门将" />
                        <el-option label="后卫" value="后卫" />
                        <el-option label="中场" value="中场" />
                        <el-option label="前锋" value="前锋" />
                    </el-select>
                </el-form-item>
                <el-form-item label="号码">
                    <el-input-number v-model="formData.jersey_number" :min="1" :max="99" />
                </el-form-item>
                <el-form-item label="身高(cm)">
                    <el-input-number v-model="formData.height" :step="0.1" />
                </el-form-item>
                <el-form-item label="体重(kg)">
                    <el-input-number v-model="formData.weight" :step="0.1" />
                </el-form-item>
                <el-form-item label="国籍">
                    <el-input v-model="formData.nationality" />
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

const players = ref([
    {
        id: 1,
        name: "克里斯蒂亚诺·罗纳尔多",
        position: "前锋",
        jersey_number: 7,
        height: 187,
        weight: 83,
        nationality: "葡萄牙",
    },
    {
        id: 2,
        name: "莱昂内尔·梅西",
        position: "前锋",
        jersey_number: 10,
        height: 170,
        weight: 72,
        nationality: "阿根廷",
    },
]);

const dialogVisible = ref(false);
const dialogTitle = ref("");
const editingId = ref(null);

const formData = ref({
    name: "",
    position: "",
    jersey_number: null,
    height: null,
    weight: null,
    nationality: "",
});

const pagination = ref({
    page: 1,
    limit: 10,
    total: players.value.length,
});

const showAddDialog = () => {
    dialogTitle.value = "添加球员";
    editingId.value = null;
    formData.value = {
        name: "",
        position: "",
        jersey_number: null,
        height: null,
        weight: null,
        nationality: "",
    };
    dialogVisible.value = true;
};

const handleEdit = (row) => {
    dialogTitle.value = "编辑球员";
    editingId.value = row.id;
    formData.value = { ...row };
    dialogVisible.value = true;
};

const handleSave = () => {
    if (editingId.value) {
        const index = players.value.findIndex((p) => p.id === editingId.value);
        if (index !== -1) {
            players.value[index] = { ...formData.value, id: editingId.value };
        }
    } else {
        players.value.push({
            id: Math.max(...players.value.map((p) => p.id), 0) + 1,
            ...formData.value,
        });
    }
    dialogVisible.value = false;
    ElMessage.success("保存成功");
};

const handleDelete = (id) => {
    ElMessageBox.confirm("确认删除此球员吗?", "警告", {
        confirmButtonText: "确认",
        cancelButtonText: "取消",
        type: "warning",
    })
        .then(() => {
            const index = players.value.findIndex((p) => p.id === id);
            if (index !== -1) {
                players.value.splice(index, 1);
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
.players-container {
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
