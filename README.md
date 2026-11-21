# news-image-20261121

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/yobrave/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/yobrave/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

这是 [make.fun](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) 悬赏 `news-image-20261121`（把 2026 年 11 月 21 日的世界新闻汇总成一张图）的参赛作品，由 AI agent 会话构建。

## 海报内容

`entry.png` 是一张 1024×1024 的报纸头版，把当日世界新闻压成 27 条编号条目：

- **报头**：黑色版次条 + 巨型日期 `SATURDAY 21 NOVEMBER 2026`（全图最大元素）+ 红色导语
  （COP31 化石燃料僵局 / 标普 500 跌 3.7% / 俄导弹落入波兰）+ 六格数字带（200 国 / −3.7% / 146,000 / 12 / $7.25bn / 1948）
- **三条主打**：`01` COP31 化石燃料僵局（安塔利亚会场）、`02` AI 抛售拖垮标普 500、`03` 俄导弹落入波兰与北约军演擦枪
- **12 幅插画卡**（3 列 × 4 行，编号 04–15）：英欧脱欧协议、利雅得拦截三枚胡塞导弹、联合国法院认定缅甸种族灭绝、
  深圳三方峰会、AI 证明黎曼猜想、法国抗议 146,000 人、帕里西兹火灾定罪、以军进攻努赛赖特、加纳在 COP31 控诉、
  卢拉守护亚马逊、秘鲁 6.7 级地震、墨尔本杯赛马殒命 —— **每张卡片一套独立配色与独立场景**
- **WHERE IT HAPPENED 世界地图**：15 枚编号图钉，对应 01–15 条，图例按洲色标注条数
- **ALSO ON SATURDAY**：12 条一句话简报（编号 16–27），粗体地点前缀
- **页脚**：来源署名（AP / BBC / DW / NPR / Washington Post / France 24 / Al Jazeera）+ 方法说明行

素材来自 Wayback Machine 当日快照，8 个源逐个通读后策展成 `notes.md`；`notes.md` 末尾的 **Art index** 表把
每一条故事映射成渲染器可直接使用的图形提示（图标 / 关键数字 / 是否量化走势 / 场景描述）。

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
