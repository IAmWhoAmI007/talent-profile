# 员工画像系统（Talent Profile）

一个面向企业 HR/管理者 的员工画像系统基础版，包含：

- 员工基础信息管理
- 能力维度建模
- 绩效与行为数据聚合
- 自动计算画像标签
- 前端画像总览页（静态原型）

## 项目结构

```text
.
├── backend
│   ├── app
│   │   ├── main.py                # FastAPI 入口
│   │   ├── models
│   │   │   └── employee.py        # 数据模型
│   │   └── services
│   │       └── profiling.py       # 画像计算逻辑
│   └── requirements.txt
├── frontend
│   ├── index.html                 # 前端页面
│   ├── app.js
│   └── styles.css
└── docs
    └── architecture.md            # 架构设计说明
```

## 快速启动

### 1) 后端

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### 2) 前端

直接打开 `frontend/index.html` 即可（或使用任意静态文件服务）。

默认前端读取：`http://localhost:8000`

## 核心接口

- `GET /health`：健康检查
- `GET /employees`：获取所有员工画像
- `GET /employees/{employee_id}`：获取单个员工画像

## 画像维度（当前实现）

- 能力分：技术能力、沟通协作、学习敏捷
- 绩效分：最近绩效记录平均值
- 稳定性：在职月份与活跃度
- 潜力标签：高潜/稳定骨干/待提升

可在 `backend/app/services/profiling.py` 扩展规则。
