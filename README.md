# 足球管理系统

一个完整的前后端分离的足球管理系统，采用 Python FastAPI + Vue3 技术栈。

## 项目特性

- ✅ 完整的用户认证与权限管理（RBAC）
- ✅ 球队、球员、赛事全生命周期管理
- ✅ 比赛记录与积分榜自动更新
- ✅ 训练计划与健康管理
- ✅ 数据可视化与报表导出
- ✅ 前后端分离架构
- ✅ RESTful API 设计
- ✅ 异步数据库操作

## 技术栈

### 后端
- **框架**: FastAPI 0.104.1
- **数据库**: MySQL 8.0 + SQLAlchemy ORM
- **缓存**: Redis
- **认证**: JWT + Passlib
- **服务器**: Uvicorn + Gunicorn

### 前端
- **框架**: Vue 3 + Vite
- **状态管理**: Pinia
- **路由**: Vue Router 4
- **UI组件**: Element Plus
- **HTTP客户端**: Axios
- **数据可视化**: ECharts

## 项目结构

```
football-management-system/
├── backend/
│   ├── app/
│   │   ├── core/              # 核心配置与安全
│   │   ├── models/            # 数据库模型
│   │   ├── schemas/           # Pydantic 数据模型
│   │   ├── api/
│   │   │   └── v1/
│   │   │       └── endpoints/ # API 端点
│   │   ├── db/                # 数据库配置
│   │   ├── utils/             # 工具函数
│   │   ├── services/          # 业务逻辑
│   │   └── main.py            # 应用入口
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── components/        # 可复用组件
│   │   ├── pages/             # 页面组件
│   │   ├── router/            # 路由配置
│   │   ├── stores/            # Pinia 状态管理
│   │   ├── api/               # API 客户端
│   │   ├── assets/            # 静态资源
│   │   ├── styles/            # 全局样式
│   │   ├── App.vue
│   │   └── main.js
│   ├── package.json
│   ├── vite.config.js
│   └── index.html
└── README.md
```

## 快速开始

### 后端启动

```bash
# 1. 进入后端目录
cd backend

# 2. 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows

# 3. 安装依赖
pip install -r requirements.txt

# 4. 配置环境变量
cp .env.example .env
# 编辑 .env 文件，配置数据库连接

# 5. 运行应用
python app/main.py
# 或使用 uvicorn
uvicorn app.main:app --reload
```

访问 API 文档: http://localhost:8000/docs

### 前端启动

```bash
# 1. 进入前端目录
cd frontend

# 2. 安装依赖
npm install

# 3. 启动开发服务器
npm run dev
```

访问应用: http://localhost:5173

## 核心功能模块

### 1. 用户与权限管理
- 用户注册、登录、密码重置
- 基于 RBAC 的权限控制
- 角色与权限管理

### 2. 球队管理
- 球队信息增删改查
- 成员管理与阵容展示
- 荣誉记录管理

### 3. 球员管理
- 球员档案管理
- 数据统计与趋势分析
- 健康与伤病记录

### 4. 赛事管理
- 赛事配置与赛程编排
- 比赛记录与积分自动更新
- 积分榜与射手榜统计

### 5. 训练管理
- 训练计划创建与管理
- 训练记录与评分
- 资源库管理

### 6. 数据统计
- 仪表盘概览
- 多维度数据分析
- 报表导出

## API 端点

### 认证
- `POST /api/v1/auth/register` - 用户注册
- `POST /api/v1/auth/login` - 用户登录

### 球队
- `GET /api/v1/teams` - 获取球队列表
- `GET /api/v1/teams/{id}` - 获取球队详情
- `POST /api/v1/teams` - 创建球队
- `PUT /api/v1/teams/{id}` - 更新球队
- `DELETE /api/v1/teams/{id}` - 删除球队

### 球员
- `GET /api/v1/players` - 获取球员列表
- `GET /api/v1/players/{id}` - 获取球员详情
- `POST /api/v1/players` - 创建球员
- `PUT /api/v1/players/{id}` - 更新球员
- `DELETE /api/v1/players/{id}` - 删除球员

### 赛事
- `GET /api/v1/competitions` - 获取赛事列表
- `GET /api/v1/competitions/{id}` - 获取赛事详情
- `POST /api/v1/competitions` - 创建赛事

## 数据库设计

详见 `DATABASE_DESIGN.md`

## 部署

### Docker 部署

```bash
# 构建镜像
docker build -t football-system .

# 运行容器
docker run -p 8000:8000 football-system
```

### 生产环境

使用 Gunicorn + Nginx 部署：

```bash
gunicorn -w 4 -b 0.0.0.0:8000 app.main:app
```

## 贡献指南

欢迎提交 Issue 和 Pull Request！

## 许可证

MIT License

## 联系方式

如有问题，请提交 Issue 或联系开发者。
