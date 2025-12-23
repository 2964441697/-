# 足球管理系统 - 数据库设计文档

## 数据库概述

本系统采用 MySQL 8.0 作为主数据库，使用 SQLAlchemy ORM 进行数据操作。

## ER 图

```
User(用户) ─────┬────── Role(角色) ─────── Permission(权限)
                │
            Team(球队)────┬─── Player(球员)─┬─── PlayerStatistics(球员统计)
                          │                 └─── HealthRecord(健康记录)
                          │
                      Honor(荣誉)

Competition(赛事) ─┬─── Schedule(赛程)─ MatchRecord(比赛记录)
                   └─── Standing(积分榜)

TrainingPlan(训练计划) ─┬─── TrainingRecord(训练记录)
                       └─── TrainingResource(训练资源)
```

## 详细表设计

### 1. 用户与权限管理

#### user 表 - 用户信息
| 字段 | 类型 | 约束 | 说明 |
|------|------|------|------|
| id | INT | PK, AI | 用户ID |
| username | VARCHAR(50) | UNIQUE, INDEX | 用户名 |
| email | VARCHAR(100) | UNIQUE, INDEX | 邮箱 |
| password | VARCHAR(255) | NOT NULL | 密码哈希 |
| full_name | VARCHAR(100) | NOT NULL | 全名 |
| phone | VARCHAR(20) | - | 电话 |
| avatar | VARCHAR(255) | - | 头像URL |
| is_active | BOOLEAN | DEFAULT TRUE | 是否激活 |
| is_superuser | BOOLEAN | DEFAULT FALSE | 是否超级管理员 |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | 创建时间 |
| updated_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | 更新时间 |
| last_login | DATETIME | - | 最后登录时间 |

#### role 表 - 角色
| 字段 | 类型 | 约束 | 说明 |
|------|------|------|------|
| id | INT | PK, AI | 角色ID |
| name | VARCHAR(50) | UNIQUE, INDEX | 角色名称 |
| description | VARCHAR(255) | - | 角色描述 |
| is_system | BOOLEAN | DEFAULT FALSE | 是否系统预设 |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | 创建时间 |

**预设角色:**
- 超级管理员: 所有权限
- 普通管理员: 除用户管理外的所有权限
- 教练: 球队、球员、训练、比赛权限
- 球员: 只读权限
- 游客: 仅查看权限

#### permission 表 - 权限
| 字段 | 类型 | 约束 | 说明 |
|------|------|------|------|
| id | INT | PK, AI | 权限ID |
| name | VARCHAR(50) | UNIQUE | 权限名称 |
| resource | VARCHAR(50) | INDEX | 资源(user/team/player等) |
| action | VARCHAR(50) | - | 操作(create/read/update/delete) |
| description | VARCHAR(255) | - | 权限描述 |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | 创建时间 |

#### user_role 表 - 用户角色关联
| 字段 | 类型 | 约束 | 说明 |
|------|------|------|------|
| user_id | INT | FK, PK | 用户ID |
| role_id | INT | FK, PK | 角色ID |

#### role_permission 表 - 角色权限关联
| 字段 | 类型 | 约束 | 说明 |
|------|------|------|------|
| role_id | INT | FK, PK | 角色ID |
| permission_id | INT | FK, PK | 权限ID |

### 2. 球队管理

#### team 表 - 球队信息
| 字段 | 类型 | 约束 | 说明 |
|------|------|------|------|
| id | INT | PK, AI | 球队ID |
| name | VARCHAR(100) | UNIQUE, INDEX | 球队名称 |
| logo | VARCHAR(255) | - | 队徽URL |
| home_ground | VARCHAR(100) | - | 主场 |
| founded_year | INT | - | 成立年份 |
| description | TEXT | - | 球队介绍 |
| phone | VARCHAR(20) | - | 联系电话 |
| email | VARCHAR(100) | - | 联系邮箱 |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | 创建时间 |
| updated_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | 更新时间 |

#### honor 表 - 荣誉记录
| 字段 | 类型 | 约束 | 说明 |
|------|------|------|------|
| id | INT | PK, AI | 荣誉ID |
| team_id | INT | FK | 球队ID |
| title | VARCHAR(100) | NOT NULL | 荣誉名称 |
| description | TEXT | - | 荣誉描述 |
| image | VARCHAR(255) | - | 荣誉图片URL |
| year | INT | NOT NULL | 获奖年份 |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | 创建时间 |

### 3. 球员管理

#### player 表 - 球员档案
| 字段 | 类型 | 约束 | 说明 |
|------|------|------|------|
| id | INT | PK, AI | 球员ID |
| team_id | INT | FK | 球队ID |
| jersey_number | INT | - | 球衣号码 |
| name | VARCHAR(100) | INDEX | 球员姓名 |
| position | VARCHAR(50) | INDEX | 场上位置 |
| height | FLOAT | - | 身高(cm) |
| weight | FLOAT | - | 体重(kg) |
| birth_date | DATE | - | 出生日期 |
| nationality | VARCHAR(50) | - | 国籍 |
| photo | VARCHAR(255) | - | 球员照片URL |
| biography | TEXT | - | 球员简介 |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | 创建时间 |
| updated_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | 更新时间 |

#### player_statistics 表 - 球员统计
| 字段 | 类型 | 约束 | 说明 |
|------|------|------|------|
| id | INT | PK, AI | 统计ID |
| player_id | INT | FK | 球员ID |
| season | VARCHAR(20) | INDEX | 赛季 |
| appearance | INT | DEFAULT 0 | 出场次数 |
| goals | INT | DEFAULT 0 | 进球数 |
| assists | INT | DEFAULT 0 | 助攻数 |
| yellow_cards | INT | DEFAULT 0 | 黄牌数 |
| red_cards | INT | DEFAULT 0 | 红牌数 |
| minutes_played | INT | DEFAULT 0 | 出场时间(分钟) |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | 创建时间 |

#### health_record 表 - 健康记录
| 字段 | 类型 | 约束 | 说明 |
|------|------|------|------|
| id | INT | PK, AI | 记录ID |
| player_id | INT | FK | 球员ID |
| record_type | VARCHAR(50) | INDEX | 记录类型(伤病/体检/康复) |
| description | TEXT | NOT NULL | 详细描述 |
| start_date | DATE | NOT NULL | 开始日期 |
| end_date | DATE | - | 结束日期 |
| status | VARCHAR(50) | - | 状态(进行中/已完成/已取消) |
| notes | TEXT | - | 备注 |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | 创建时间 |

### 4. 赛事管理

#### competition 表 - 赛事配置
| 字段 | 类型 | 约束 | 说明 |
|------|------|------|------|
| id | INT | PK, AI | 赛事ID |
| name | VARCHAR(100) | UNIQUE, INDEX | 赛事名称 |
| competition_type | VARCHAR(50) | INDEX | 赛事类型(联赛/杯赛) |
| season | VARCHAR(20) | - | 赛季 |
| description | TEXT | - | 赛事描述 |
| start_date | DATE | NOT NULL | 开始日期 |
| end_date | DATE | NOT NULL | 结束日期 |
| rules | TEXT | - | 赛事规则 |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | 创建时间 |
| updated_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | 更新时间 |

#### schedule 表 - 赛程
| 字段 | 类型 | 约束 | 说明 |
|------|------|------|------|
| id | INT | PK, AI | 赛程ID |
| competition_id | INT | FK, INDEX | 赛事ID |
| round_number | INT | NOT NULL | 轮次 |
| match_date | DATE | NOT NULL | 比赛日期 |
| match_time | TIME | - | 比赛时间 |
| home_team_id | INT | FK | 主队ID |
| away_team_id | INT | FK | 客队ID |
| venue | VARCHAR(100) | - | 比赛场地 |
| status | VARCHAR(50) | - | 比赛状态(待定/进行中/已完成/已取消) |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | 创建时间 |

#### match_record 表 - 比赛记录
| 字段 | 类型 | 约束 | 说明 |
|------|------|------|------|
| id | INT | PK, AI | 记录ID |
| schedule_id | INT | FK, UNIQUE | 赛程ID |
| home_team_id | INT | FK | 主队ID |
| away_team_id | INT | FK | 客队ID |
| home_goals | INT | DEFAULT 0 | 主队进球 |
| away_goals | INT | DEFAULT 0 | 客队进球 |
| status | VARCHAR(50) | - | 比赛状态(进行中/已完成) |
| event_details | JSON | - | 事件详情(进球/红黄牌等) |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | 创建时间 |
| updated_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | 更新时间 |

#### standing 表 - 积分榜
| 字段 | 类型 | 约束 | 说明 |
|------|------|------|------|
| id | INT | PK, AI | 记录ID |
| competition_id | INT | FK, INDEX | 赛事ID |
| team_id | INT | FK, INDEX | 球队ID |
| rank | INT | NOT NULL | 排名 |
| played | INT | DEFAULT 0 | 比赛场数 |
| won | INT | DEFAULT 0 | 胜场数 |
| drawn | INT | DEFAULT 0 | 平局次数 |
| lost | INT | DEFAULT 0 | 负场数 |
| goals_for | INT | DEFAULT 0 | 进球数 |
| goals_against | INT | DEFAULT 0 | 失球数 |
| goal_difference | INT | DEFAULT 0 | 净胜球 |
| points | INT | DEFAULT 0 | 积分 |
| updated_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | 更新时间 |

### 5. 训练管理

#### training_plan 表 - 训练计划
| 字段 | 类型 | 约束 | 说明 |
|------|------|------|------|
| id | INT | PK, AI | 计划ID |
| team_id | INT | FK | 球队ID |
| coach_id | INT | FK | 教练ID |
| title | VARCHAR(100) | NOT NULL | 计划标题 |
| topic | VARCHAR(100) | - | 训练主题 |
| description | TEXT | - | 计划描述 |
| scheduled_date | DATE | NOT NULL | 计划日期 |
| scheduled_time | TIME | - | 计划时间 |
| duration | INT | - | 时长(分钟) |
| location | VARCHAR(100) | - | 训练地点 |
| category | VARCHAR(50) | - | 分类(体能/技术/战术/恢复) |
| status | VARCHAR(50) | DEFAULT 'scheduled' | 状态 |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | 创建时间 |
| updated_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | 更新时间 |

#### training_record 表 - 训练记录
| 字段 | 类型 | 约束 | 说明 |
|------|------|------|------|
| id | INT | PK, AI | 记录ID |
| training_plan_id | INT | FK | 计划ID |
| player_id | INT | FK | 球员ID |
| attendance | VARCHAR(50) | - | 参与情况(出席/缺席/迟到) |
| completion_rate | INT | - | 完成度(百分比) |
| performance_score | INT | - | 表现评分(1-10) |
| coach_comment | TEXT | - | 教练评论 |
| recorded_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | 记录时间 |

#### training_resource 表 - 训练资源
| 字段 | 类型 | 约束 | 说明 |
|------|------|------|------|
| id | INT | PK, AI | 资源ID |
| team_id | INT | FK | 球队ID |
| resource_type | VARCHAR(50) | - | 类型(教案/视频/器材/其他) |
| name | VARCHAR(100) | NOT NULL | 资源名称 |
| description | TEXT | - | 资源描述 |
| file_path | VARCHAR(255) | - | 文件路径 |
| file_url | VARCHAR(255) | - | 文件URL |
| category | VARCHAR(50) | - | 分类 |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | 创建时间 |
| updated_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | 更新时间 |

## 索引设计

为了提高查询性能，设计以下关键索引：

```sql
-- 用户表
CREATE INDEX idx_user_username ON user(username);
CREATE INDEX idx_user_email ON user(email);

-- 球队表
CREATE INDEX idx_team_name ON team(name);

-- 球员表
CREATE INDEX idx_player_team_id ON player(team_id);
CREATE INDEX idx_player_position ON player(position);
CREATE INDEX idx_player_name ON player(name);

-- 赛事表
CREATE INDEX idx_competition_type ON competition(competition_type);
CREATE INDEX idx_schedule_competition_id ON schedule(competition_id);
CREATE INDEX idx_standing_competition_id ON standing(competition_id);

-- 训练表
CREATE INDEX idx_training_plan_team_id ON training_plan(team_id);
CREATE INDEX idx_training_record_plan_id ON training_record(training_plan_id);
```

## 约束设计

### 主键约束
所有表都有主键，采用自增整数ID。

### 外键约束
- player.team_id → team.id
- training_plan.team_id → team.id
- training_plan.coach_id → user.id
- schedule.home_team_id → team.id
- schedule.away_team_id → team.id
- 等等...

### 唯一约束
- user.username
- user.email
- team.name
- competition.name
- schedule(competition_id, home_team_id, away_team_id, match_date)

## 数据初始化

系统启动时应初始化以下数据：

### 预设角色
```sql
INSERT INTO role (name, description, is_system) VALUES
('超级管理员', '系统管理员，拥有所有权限', TRUE),
('普通管理员', '普通管理员', TRUE),
('教练', '教练人员', TRUE),
('球员', '球员人员', TRUE),
('游客', '游客，只读权限', TRUE);
```

### 预设权限
根据资源和操作组合生成权限。

## 数据库备份与恢复

### 备份
```bash
mysqldump -u root -p football_db > backup.sql
```

### 恢复
```bash
mysql -u root -p football_db < backup.sql
```

## 性能优化建议

1. **查询优化**: 使用适当的 WHERE 条件和 JOIN 优化查询
2. **缓存策略**: 将常访问的数据(如积分榜)缓存到 Redis
3. **分区**: 对大表进行分区，如按赛季分区 match_record
4. **数据清理**: 定期清理过期数据(如旧赛季数据)
5. **连接池**: 使用数据库连接池管理连接

## SQL 初始化脚本

详见 `backend/sql/init.sql`
