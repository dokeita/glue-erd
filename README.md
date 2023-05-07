## なにこれ
* Glueデータカタログに登録されているデータベース、テーブルを指定してmermaid形式のER図を作成します。

## 使い方
* glue_erd-1.0.0-py3-none-any.whl をpip installします。
* `glueerd` で実行します。コマンドは `glueerd --help` をご確認ください。
* 実行フォルダに .mdファイルが生成されます。

## help
```
% glueerd --help        
Usage: glueerd [OPTIONS]

Options:
  -d, --db_name TEXT    database name  [required]
  -table_name, -t TEXT  table name
  -out_dir, -o TEXT     output directory. default: current directory
  --help                Show this message and exit.
```

## ライセンス
[MITライセンス](./LICENSE)です。


## 参考:MermaidでER図を書く
* 公式サイト : https://mermaid.js.org/syntax/entityRelationshipDiagram.html
* VSコードでプレビューする: https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid

``` mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    CUSTOMER {
        string name
        string custNumber
        string sector
    }
    ORDER ||--|{ LINE-ITEM : contains
    ORDER {
        int orderNumber
        string deliveryAddress
    }
    LINE-ITEM {
        string productCode
        int quantity
        float pricePerUnit
    }
```

``` mermaid
erDiagram
    LINE-ITEM {
        string productCode
        int quantity
        float pricePerUnit
    }
```
