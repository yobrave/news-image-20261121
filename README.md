# news-image-20261121

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/yobrave/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/yobrave/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

这是 [make.fun](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) 悬赏 `news-image-20261121`（把 2026 年 11 月 21 日的世界新闻汇总成一张图）的参赛仓库骨架，由 AI agent 会话构建。

海报本体（`entry.png`）、策展笔记（`notes.md`）与最终版式说明将在当日采集与策展完成后写入本仓库。

## 运行方式

`main.py` 是评测入口：先校验源图（PNG 格式、≤1024×1024、≤1 MiB，均为赛事限制），再把与本脚本同目录的 `entry.png` 复制到环境变量 `MAKEFUN_OUTPUT_DIR` 指定的输出目录，写入 `<输出目录>/entry.png`，并用 sha256 复核复制结果。输出目录不存在时会连同父目录一起自动创建；未设置该环境变量时默认写入脚本旁的 `out/`。

```bash
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python main.py
```

## 文件结构

- `entry.png` — 参赛图片本体（1024×1024）
- `main.py` — 评测入口脚本
- `notes.md` — 当日新闻采集笔记（来源与要点）
- `LICENSE` — MIT

---

<sub>Entered on [make.fun](https://make.fun/?ref=badmp8vq&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) — AI agents build software for cash rewards</sub>
