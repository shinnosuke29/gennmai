# numstats コマンド

`numstats` は、標準入力から受け取った数値の統計情報（合計、平均、最大、最小、中央値、標準偏差）を計算するコマンドです。

## 使い方

以下のように標準入力を渡して統計情報を取得します。

```bash
$ echo -e "10\n20\n30\n40\n50" | python3 scripts/numstats.py --sum --avg --max --min --median --std
Sum: 150.0
Average: 30.00
Max: 50.0
Min: 10.0
Median: 30.0
Standard Deviation: 14.14

# 必要なソフトウェア

    Python（バージョン3.7〜3.10で動作確認済み）

# テスト環境

    OS: Ubuntu 24.04.1 LTS
    Python: 3.7 ~ 3.10
