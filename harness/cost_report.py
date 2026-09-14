"""
Measured cost from logged token usage. Supply the list prices you were actually
billed at; the output replaces the plan's estimate with a measured figure for the
scale-up slide.

  python cost_report.py --price openai=2,12,0.010 --price gemini=0.75,3.75,0 --price anthropic=3,15,0.010

Each --price is provider=input_per_M,output_per_M,search_fee_per_call.
"""
import argparse
import csv
import glob
import os
from collections import defaultdict


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", default="results")
    ap.add_argument("--price", action="append", default=[], help="provider=in,out,search")
    a = ap.parse_args()
    prices = {}
    for p in a.price:
        prov, vals = p.split("=")
        i, o, s = (float(x) for x in vals.split(","))
        prices[prov] = (i, o, s)

    agg = defaultdict(lambda: {"calls": 0, "in": 0, "out": 0, "searches": 0, "errors": 0})
    for path in glob.glob(os.path.join(a.results, "*.csv")):
        for r in csv.DictReader(open(path, newline="", encoding="utf-8")):
            k = (r["provider"], r["model_id"], r["condition"])
            g = agg[k]
            if r.get("error"):
                g["errors"] += 1
                continue
            g["calls"] += 1
            g["in"] += int(float(r["input_tokens"] or 0))
            g["out"] += int(float(r["output_tokens"] or 0))
            g["searches"] += int(float(r["search_count"] or 0))

    total = 0.0
    print(f"{'provider':10} {'model':28} {'condition':11} {'calls':>6} {'in_tok':>9} {'out_tok':>9} {'searches':>8} {'errors':>6} {'cost':>8}")
    for (prov, model, cond), g in sorted(agg.items()):
        i, o, s = prices.get(prov, (0, 0, 0))
        cost = g["in"] / 1e6 * i + g["out"] / 1e6 * o + g["searches"] * s
        total += cost
        print(f"{prov:10} {model[:28]:28} {cond:11} {g['calls']:6} {g['in']:9} {g['out']:9} {g['searches']:8} {g['errors']:6} {cost:8.2f}")
    print(f"\nTotal at supplied prices: ${total:.2f}")
    if not prices:
        print("(no --price supplied; costs shown as 0)")


if __name__ == "__main__":
    main()
