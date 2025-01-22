# numstats コマンド

---

## 使用言語

- Python

---

## リポジトリの概要

### `numstats.py`

標準入力から受け取った数値の統計情報（合計、平均、最大、最小、中央値、標準偏差）を計算して出力します。

---

## リポジトリの使用方法

### 1. GitHub からリポジトリをクローン

```bash
git clone https://github.com/shinnosuke29/gennmai.git
```

### 2. リポジトリへ移動

```bash
cd gennmai
```

### 3. スクリプト実行環境の確認

```bash
python3 --version
```

### 4. スクリプトを実行

以下のように標準入力から数値を渡して実行してください。

```bash
echo -e "10\n20\n30\n40\n50" | python3 scripts/numstats.py --sum --avg --max --min --median --std
```
### 実行例

```bash
$ echo -e "10\n20\n30\n40\n50" | python3 scripts/numstats.py --sum --avg --max >
Sum: 150.0
Average: 30.00
Max: 50.0
Min: 10.0
Median: 30.0
Standard Deviation: 14.14
```

---

## numstats.py の機能

標準入力から数値を受け取り、以下の統計情報を出力します：

- **合計（sum）**
- **平均（average）**
- **最大値（max）**
- **最小値（min）**
- **中央値（median）**
- **標準偏差（standard deviation）**

---

## 必要なソフトウェア

- Python  
  - テスト済みバージョン: 3.7 ~ 3.10

---

## テスト環境

- OS: Ubuntu 24.04.1 LTS
- Python: 3.7 ~ 3.10

---

## LICENSE

- このソフトウェアパッケージは、BSD 3-Clause ICライセンスの下、再頒布および使用が許可されます。

- © 2024 Shinnosuke
