<template>
    <div class="competitions-container">
        <el-card>
            <template #header>
                <div class="card-header">
                    <span>赛事管理</span>
                    <el-button type="primary" @click="showAddDialog">创建赛事</el-button>
                </div>
            </template>

            <el-table :data="competitions" stripe>
                <el-table-column prop="name" label="赛事名称" width="150" />
                <el-table-column prop="competition_type" label="类型" width="100" />
                <el-table-column prop="season" label="赛季" width="100" />
                <el-table-column prop="start_date" label="开始日期" width="120" />
                <el-table-column prop="end_date" label="结束日期" width="120" />
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
                <el-form-item label="赛事名称">
                    <el-input v-model="formData.name" />
                </el-form-item>
                <el-form-item label="赛事类型">
                    <el-select v-model="formData.competition_type" placeholder="选择类型">
                        <el-option label="联赛" value="联赛" />
                        <el-option label="杯赛" value="杯赛" />
                    </el-select>
                </el-form-item>
                <el-form-item label="赛季">
                    <el-input v-model="formData.season" placeholder="例如: 2023-2024" />
                </el-form-item>
                <el-form-item label="开始日期">
                    <el-date-picker v-model="formData.start_date" type="date" />
                </el-form-item>
                <el-form-item label="结束日期">
                    <el-date-picker v-model="formData.end_date" type="date" />
                </el-form-item>
                <el-form-item label="赛事规则">
                    <el-input v-model="formData.rules" type="textarea" rows="3" />
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

const competitions = ref([
    {
        id: 1,
        name: "英超联赛",
        competition_type: "联赛",
        season: "2023-2024",
        start_date: "2023-08-01",
        end_date: "2024-05-31",
    },
    {
        id: 2,
        name: "欧冠杯",
        competition_type: "杯赛",
        season: "2023-2024",
        start_date: "2023-09-19",
        end_date: "2024-06-01",
    },
]);

const dialogVisible = ref(false);
const dialogTitle = ref("");
const editingId = ref(null);

const formData = ref({
    name: "",
    competition_type: "",
    season: "",
    start_date: null,
    end_date: null,
    rules: "",
});

const pagination = ref({
    page: 1,
    limit: 10,
    total: competitions.value.length,
});

const showAddDialog = () => {
    dialogTitle.value = "创建赛事";
    editingId.value = null;
    formData.value = {
        name: "",
        competition_type: "",
        season: "",
        start_date: null,
        end_date: null,
        rules: "",
    };
    dialogVisible.value = true;
};

const handleEdit = (row) => {
    dialogTitle.value = "编辑赛事";
    editingId.value = row.id;
    formData.value = { ...row };
    dialogVisible.value = true;
};

const handleSave = () => {
    if (editingId.value) {
        const index = competitions.value.findIndex((c) => c.id === editingId.value);
        if (index !== -1) {
            competitions.value[index] = { ...formData.value, id: editingId.value };
        }
    } else {
        competitions.value.push({
            id: Math.max(...competitions.value.map((c) => c.id), 0) + 1,
            ...formData.value,
        });
    }
    dialogVisible.value = false;
    ElMessage.success("保存成功");
};

const handleDelete = (id) => {
    ElMessageBox.confirm("确认删除此赛事吗?", "警告", {
        confirmButtonText: "确认",
        cancelButtonText: "取消",
        type: "warning",
    })
        .then(() => {
            const index = competitions.value.findIndex((c) => c.id === id);
            if (index !== -1) {
                competitions.value.splice(index, 1);
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
.competitions-container {
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
