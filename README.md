# My First Repo - 绿氢产量小计算器

Hui 的第一个 GitHub 练习仓库：一个简单的绿氢 / 绿氨产量估算工具。

## 它能算什么

输入电解槽功率，就能估算：
- 年产氢量 (kt/年)
- 对应绿氨产量 (kt/年，按 H2 × 5.67 换算)
- 对应合成氨装置规模是否经济

计算口径（和 Hyport Duqm 项目用的同一套）：
- 电耗：~50 kWh/kg H2
- 等效运行小时：4,500 - 5,500 小时/年
- 例：200 MW → 氢 18-22 kt/年 → 绿氨 100-120 kt/年

## 怎么运行

```bash
python hydrogen_calc.py
```

或者改参数运行：
```bash
python hydrogen_calc.py --mw 350 --hours 5000
```

## 文件说明

- `hydrogen_calc.py` - 计算脚本
- `README.md` - 本说明文件（GitHub 首页会自动显示它）

## 下一步可以加的

- [ ] 液氢产量估算（20 MW 试点约 9.6 t/d）
- [ ] 电解槽 OEM 对比表
- [ ] 成本估算：$/kg

---
Created with Muse - 2026-10-23 练习版
这是我亲手改的第一行 - 2026-10-23
