### 基本事項

##### 戻り値について

どのURLも戻り値として

```json
{message: "ログメッセージ"}
```

をjsonファイルとして返します。

※これ以外に戻り値がない場合は**なし**と記述してあります。

##### 本ドキュメントの形式

- URL [Method]
    - 引数
    - 戻り値

### ログイン系処理

##### /login [POST]

ログインします。
このURLのみ非ログイン状態でもアクセスすることができます。

- 引数
    - `mail`
    - `password`
- 戻り値
    - なし

##### /logout [GET]

ログアウトします

- 引数
  - なし
- 戻り値
  - なし

##### /signin [POST]

サインインします

- 引数
  - `name`
  - `mail`
  - `password`
  - `image`　ユーザーの画像(base64) nullable
- 戻り値
  - なし

### トップ
##### /top [GET]

おすすめとピン留め本をそれぞれ最大10冊返します

- 引数
  - なし
- 戻り値
  - `recommendBook` おすすめ本
  - `pinnedBook`　ピン留め本

### 記事関連

##### /article [GET]

 ある本に関する記事の一覧を取得します

- 引数
  - `bookID` 対象とする本のID
- 戻り値
  - `ID` 記事のID
  - `context` 記事の中身 
  - `chapter` 章番号 (nullable)
  - `page` ページ番号 (nullable)
  - `isLiked` ログインしているユーザーにいいねされているか(true or false)
  - `isBookmarked` ログインしているユーザーにブックマークされているか(true or false)
  - `updatedDate` 記事が最後にアップデートされた日
  - `userID` 記事を投稿したユーザーのID

##### /article [POST]

新規記事を登録します

- 引数
  - `bookID` 対象とする本のID
  - `context` 記事の中身
  - `chapter` 章番号 (nullable)
  - `page` ページ番号 (nullable)
- 戻り値
  - なし

##### /article [DELETE]

記事を削除します

- 引数
  - `articleID` 記事のID
- 戻り値
  - なし

##### /article [PUT]

既存の記事の編集をします

- 引数
  - `articleID` 記事のID
- 戻り値
  - なし

##### /like [POST]

記事をいいねします

- 引数
  - `articleID` 記事のID
- 戻り値
  - なし

##### /bookmark

記事をブックマークします

- 引数
  - `articleID` 記事のID
- 戻り値
  - なし

### 書籍

##### /search [GET]

本に関する情報を検索します。

- 引数
  - `isbn` 対象の本のISBNコード(string)
- 戻り値
  - `ID` 本のID
  - `title`本のタイトル
  - `isbn` ISBNコード
  - `author`著者名(複数人の場合は/n区切り)
  - `imageLink`本の画像のリンク
  - `amazonLink` アマゾンの購入リンク
  - `isPinned` ログインしているユーザーにピン留めされているか(true or false)

##### /book [POST]

本の新規登録をします

- 引数
  - `isbn` ISBNコード
- `戻り値`
  - なし

### ユーザー画面

##### /user [GET]

ログイン中のユーザーに関する情報を取得します

- 引数
  -  なし
- 戻り値
  - `name` ユーザー名
  - `image` ユーザーの画像(base64)
  - `likes` いいねした記事一覧(Array)
    - `ID` 記事ID
    - `bookID`
    - `userID`
    - `context`
    - `updatedDate`
    - `chapter`
    - `page`
  - `bookmarks` ブックマークした記事一覧
    - `ID` 記事ID
    - `bookID`
    - `userID`
    - `context`
    - `updatedDate`
    - `chapter`
    - `page`
  - `posted` 投稿した記事一覧
    - `ID` 記事ID
    - `bookID`
    - `userID`
    - `context`
    - `updatedDate`
    - `chapter`
    - `page`
