"""
绿氢 / 绿氨产量估算 - 简单版
口径：电耗 50 kWh/kg, 氨换算系数 5.67 (NH3/H2 质量比近似)
"""
import argparse

def calc(mw: float, hours: float = 5000, kwh_per_kg: float = 50):
    # MW * hours = MWh, *1000 = kWh, / kwh_per_kg = kg, /1000 = t
    h2_t = mw * hours * 1000 / kwh_per_kg / 1000
    h2_kt = h2_t / 1000
    nh3_kt = h2_kt * 5.67
    return h2_kt, nh3_kt

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="绿氢产量估算")
    parser.add_argument("--mw", type=float, default=200, help="电解槽功率 MW")
    parser.add_argument("--hours", type=float, default=5000, help="等效小时")
    args = parser.parse_args()

    for h in [4500, 5000, 5500] if args.hours == 5000 else [args.hours]:
        h2, nh3 = calc(args.mw, h)
        print(f"{args.mw:.0f} MW @ {h:.0f}h -> H2 {h2:.1f} kt/年, 绿氨 {nh3:.0f} kt/年")

    print("\n参考：200 MW 是做绿氨经济性成立的最小首块规模 (~100 kt/年合成列)")
