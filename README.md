# N1 日语学习翻翻卡

> N1 真题词汇 + 语法翻翻卡 — 零构建、纯前端、本地部署

## 功能特性

### 📖 真题词汇（1576 词 · 27 章）
- 历年真题词汇，按年份章节分组
- 4 种翻转模式：日→中 / 中→日 / 音→义 / 🎲 随机
- 侧边栏章节选择器，支持多选/全选
- 搜索功能（汉字/读音/释义/章节）
- 仅生疏模式、随机打乱、进度追踪

### 📇 语法翻翻卡（205 条 · 20 单元）
- 205 条 N1 核心语法，每 10 条一个单元
- 4 种翻转模式：日→中 / 中→日 / 接→用 / 🎲 随机
- 侧边栏单元选择器，支持多选/全选
- 搜索功能（语法/接续/例句）
- 仅生疏模式、随机打乱、进度追踪

### ⚡ 技术特点
- **零构建部署** — 纯 HTML + CDN React + Babel 浏览器端转译
- **响应式设计** — 桌面/平板/手机全适配
- **本地进度** — localStorage 自动保存学习进度
- **骨架屏** — 页面加载时立即显示占位，不等 React
- **快捷键** — ← → 切换 · 空格翻转 · M 标记掌握

## 快速开始

### 方式一：本地服务器（推荐）

```bash
# 启动服务器（0.0.0.0:8080，带 no-cache 响应头）
cd /tmp/n1-study
python3 server.py

# 访问
# http://localhost:8080/          — 主页
# http://localhost:8080/vocab/    — 词汇
# http://localhost:8080/grammar/  — 语法
```

### 方式二：直接打开

直接用浏览器打开 `vocab/index.html` 或 `grammar/index.html`。

### 方式三：systemd 自启服务

```bash
# 服务已配置（如需要）
sudo systemctl enable --now n1-study.service
```

## 项目结构

```
n1-study/
├── index.html              # 主页导航
├── server.py               # Python 静态服务器（no-cache）
├── vocab/
│   ├── index.html          # 词汇翻翻卡（React + Babel）
│   └── vocab.js            # 词汇数据（1576 词，JSON 格式）
├── grammar/
│   ├── index.html          # 语法翻翻卡（React + Babel）
│   └── grammar.js          # 语法数据（205 条，数组格式）
└── backups/                # 版本备份
```

## 快捷键

| 按键 | 功能 |
|------|------|
| `←` | 上一张卡片 |
| `→` | 下一张卡片 |
| `Space` | 翻转卡片 |
| `M` | 标记已掌握/生疏 |

## 数据存储

所有学习进度保存在浏览器 `localStorage`：

| Key | 说明 |
|-----|------|
| `n1_vocab_mastered_ids` | 词汇已掌握记录 |
| `n1_vocab_selected_chapters` | 词汇已选章节 |
| `n1_grammar_mastered_ids` | 语法已掌握记录 |
| `n1_grammar_selected_chapters` | 语法已选单元 |
| `n1_flip_mode` | 翻转模式偏好 |

## 数据规模

| 类型 | 数量 | 分组 |
|------|------|------|
| 词汇 | 1576 条 | 27 章（按真题年份） |
| 语法 | 205 条 | 20 单元（每 10 条一组） |
| **总计** | **1781 条** | — |

## 技术栈

- **前端框架**：React 18（CDN）
- **转译**：Babel Standalone（浏览器端）
- **样式**：Tailwind CSS（CDN）
- **图标**：Lucide（CDN）
- **后端**：Python SimpleHTTPServer（仅本地开发）
- **部署**：零构建，纯静态文件

## License

MIT
