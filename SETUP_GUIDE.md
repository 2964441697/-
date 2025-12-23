# 足球管理系统 - 完整安装与配置指南

## 📋 项目概述

本项目是一个完整的足球管理系统，采用现代化的前后端分离架构。

## 🚀 快速开始

### 前置要求

- Python 3.8+
- Node.js 14+
- MySQL 8.0+
- Redis (可选，用于缓存)

### 后端配置

```bash
# 1. 进入后端目录
cd backend

# 2. 创建虚拟环境
python -m venv venv

# 3. 激活虚拟环境
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# 4. 安装依赖
pip install -r requirements.txt

# 5. 配置环境变量
cp .env.example .env
# 编辑 .env 文件，配置数据库连接和其他参数

# 6. 初始化数据库（需确保MySQL已启动）
# 使用Alembic进行迁移（可选）
# alembic upgrade head

# 7. 运行应用
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

后端将运行在 `http://localhost:8000`
API 文档: `http://localhost:8000/docs`

### 前端配置

```bash
# 1. 进入前端目录
cd frontend

# 2. 安装依赖
npm install

# 3. 启动开发服务器
npm run dev
```

前端将运行在 `http://localhost:5173`

## 📦 项目结构详解

### 后端结构

```
backend/
├── app/
│   ├── core/              # 核心配置
│   │   ├── config.py     # 应用配置管理
│   │   └── security.py   # 认证与加密
│   ├── models/            # 数据库模型
│   │   ├── user.py       # 用户、角色、权限
│   │   ├── team.py       # 球队管理
│   │   ├── player.py     # 球员管理
│   │   ├── match.py      # 赛事管理
│   │   └── training.py   # 训练管理
│   ├── schemas/           # Pydantic Schema
│   │   ├── user.py
│   │   ├── team.py
│   │   └── player.py
│   ├── api/
│   │   ├── dependencies.py  # 依赖注入
│   │   └── v1/
│   │       └── endpoints/
│   │           ├── auth.py
│   │           ├── teams.py
│   │           ├── players.py
│   │           └── competitions.py
│   ├── db/                # 数据库配置
│   ├── utils/             # 工具函数
│   ├── services/          # 业务逻辑层
│   └── main.py            # 应用入口
├── requirements.txt       # 依赖列表
└── .env.example          # 环境变量示例
```

### 前端结构

```
frontend/
├── src/
│   ├── components/        # 可复用组件
│   ├── pages/             # 页面组件
│   │   ├── Login.vue     # 登录页
│   │   ├── Dashboard.vue # 仪表盘
│   │   ├── Teams.vue     # 球队管理
│   │   ├── Players.vue   # 球员管理
│   │   └── Competitions.vue # 赛事管理
│   ├── router/            # 路由配置
│   ├── stores/            # Pinia 状态管理
│   │   └── userStore.js  # 用户状态
│   ├── api/
│   │   └── client.js     # API 客户端
│   ├── assets/            # 静态资源
│   ├── styles/            # 全局样式
│   ├── App.vue            # 根组件
│   └── main.js            # 应用入口
├── package.json
├── vite.config.js
└── index.html
```

## 🔧 环境变量配置

在 `backend/.env` 中配置以下变量：

```env
# 数据库
DATABASE_URL=mysql+aiomysql://root:password@localhost:3306/football_db
REDIS_URL=redis://localhost:6379/0

# JWT
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

# 服务器
HOST=0.0.0.0
PORT=8000
DEBUG=True

# 系统
APP_NAME=足球管理系统
APP_VERSION=1.0.0
```

## 📊 数据库初始化

### MySQL 数据库创建

```sql
CREATE DATABASE football_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 表结构初始化

使用 SQLAlchemy ORM 自动创建表：

```python
# 在后端应用启动时，可自动创建所有表
from app.db.base import Base, engine

# 创建所有表
Base.metadata.create_all(bind=engine)
```

## 🔐 认证与授权

### 用户注册

```bash
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "password123",
    "full_name": "Test User"
  }'
```

### 用户登录

```bash
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "password123"
  }'
```

响应包含 `access_token` 和 `refresh_token`。

### API 认证

在请求头中包含 Token：

```bash
curl -H "Authorization: Bearer <access_token>" \
  http://localhost:8000/api/v1/teams
```

## 📝 API 端点示例

### 球队管理

- `GET /api/v1/teams` - 获取球队列表
- `POST /api/v1/teams` - 创建球队
- `GET /api/v1/teams/{id}` - 获取球队详情
- `PUT /api/v1/teams/{id}` - 更新球队
- `DELETE /api/v1/teams/{id}` - 删除球队

### 球员管理

- `GET /api/v1/players` - 获取球员列表
- `POST /api/v1/players` - 创建球员
- `GET /api/v1/players/{id}` - 获取球员详情
- `PUT /api/v1/players/{id}` - 更新球员
- `DELETE /api/v1/players/{id}` - 删除球员

### 赛事管理

- `GET /api/v1/competitions` - 获取赛事列表
- `POST /api/v1/competitions` - 创建赛事

## 🐳 Docker 部署

### 构建镜像

```bash
docker build -t football-system:latest .
```

### 运行容器

```bash
docker run -d \
  --name football-system \
  -p 8000:8000 \
  -e DATABASE_URL=mysql://user:pass@db:3306/football_db \
  football-system:latest
```

## 🔄 开发工作流

### 后端开发

1. 修改模型或API后，使用 Alembic 生成迁移：
   ```bash
   alembic revision --autogenerate -m "description"
   alembic upgrade head
   ```

2. 遵循以下代码结构：
   - Models: 数据库模型定义
   - Schemas: API 请求/响应模型
   - Endpoints: API 端点实现
   - Services: 业务逻辑（可选）

### 前端开发

1. 组件开发规范：
   - 使用组合式 API (Composition API)
   - 使用 Pinia 管理状态
   - 使用 Axios 调用 API

2. 构建项目：
   ```bash
   npm run build
   ```

## 📚 关键功能说明

### 用户认证流程

1. 用户注册 → 创建用户账户
2. 用户登录 → 获取 JWT Token
3. 请求受保护的资源 → 在请求头中携带 Token
4. 后端验证 Token → 返回数据

### 权限控制

系统采用 RBAC（基于角色的访问控制）：
- 用户 → 角色 → 权限
- 预设5种角色：超级管理员、普通管理员、教练、球员、游客
- 每个角色拥有不同的权限集合

### 数据关联关系

```
用户 ← → 角色 ← → 权限
球队 ← → 球员 ← → 统计/健康记录
赛事 ← → 赛程 ← → 比赛记录 → 积分榜
训练计划 ← → 训练记录
```

## 🐛 故障排除

### MySQL 连接错误

确保 MySQL 已启动并配置正确的连接字符串。

### CORS 错误

检查前端和后端的 CORS 配置，确保前端请求源在允许列表中。

### Token 过期

Token 过期后使用 `refresh_token` 重新获取 `access_token`。

## 📖 更多资源

- 完整 API 文档：`http://localhost:8000/docs`
- 数据库设计：见 `DATABASE_DESIGN.md`
- 项目说明：见 `README.md`

## ✅ 检查清单

启动前请确认：

- [ ] Python 虚拟环境已激活
- [ ] 依赖已安装 (requirements.txt)
- [ ] MySQL 已启动
- [ ] 数据库已创建
- [ ] .env 文件已配置
- [ ] 后端可在 http://localhost:8000 访问
- [ ] 前端可在 http://localhost:5173 访问

## 📞 支持

如遇问题，请：
1. 查看日志输出
2. 检查 API 文档 `/docs`
3. 提交 Issue 或联系开发者

祝你使用愉快！⚽
