<template>
    <div class="dashboard">
        <h2>仪表盘</h2>
        <el-row :gutter="20">
            <el-col :xs="24" :sm="12" :md="6">
                <el-statistic title="球队总数" :value="stats.teams" />
            </el-col>
            <el-col :xs="24" :sm="12" :md="6">
                <el-statistic title="球员总数" :value="stats.players" />
            </el-col>
            <el-col :xs="24" :sm="12" :md="6">
                <el-statistic title="赛事总数" :value="stats.competitions" />
            </el-col>
            <el-col :xs="24" :sm="12" :md="6">
                <el-statistic title="比赛场次" :value="stats.matches" />
            </el-col>
        </el-row>

        <el-row :gutter="20" style="margin-top: 20px">
            <el-col :xs="24" :md="12">
                <el-card>
                    <template #header>
                        <div class="card-header">
                            <span>近期活动</span>
                        </div>
                    </template>
                    <el-empty description="暂无数据" />
                </el-card>
            </el-col>
            <el-col :xs="24" :md="12">
                <el-card>
                    <template #header>
                        <div class="card-header">
                            <span>系统信息</span>
                        </div>
                    </template>
                    <el-descriptions :column="1" border>
                        <el-descriptions-item label="系统名称">足球管理系统</el-descriptions-item>
                        <el-descriptions-item label="版本">1.0.0</el-descriptions-item>
                        <el-descriptions-item label="最后更新">
                            {{ new Date().toLocaleDateString() }}
                        </el-descriptions-item>
                    </el-descriptions>
                </el-card>
            </el-col>
        </el-row>
    </div>
</template>

<script setup>
import { ref } from "vue";

const stats = ref({
    teams: 15,
    players: 250,
    competitions: 8,
    matches: 42,
});
</script>

<style scoped>
.dashboard {
    padding: 20px;
}

.dashboard h2 {
    margin-bottom: 20px;
}

.card-header {
    font-weight: bold;
}
</style>
