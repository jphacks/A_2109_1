USE main;
INSERT INTO user VALUES
    (0, "ICHIZYOU",  "password", "fuga@test.hoge.jp"),
    (0, "NIZYOU",  "password", "fugafuga@test.hoge.jp"),
    (0, "SANZYOU", "password", "fugafugafuga@test.hoge.jp");

INSERT INTO book VALUES
    (0, "電子デバイス工学", "9784627705623", "古川静二郎/萩田陽一郎/浅野種正", "1990-3-12",  "https://www.amazon.co.jp/%E9%9B%BB%E5%AD%90%E3%83%87%E3%83%90%E3%82%A4%E3%82%B9%E5%B7%A5%E5%AD%A6-%E7%AC%AC2%E7%89%88-%E5%8F%A4%E5%B7%9D-%E9%9D%99%E4%BA%8C%E9%83%8E/dp/462770562X"),
    (0, "ソフトウェア工学", "9784764905092", "岸知二/野田夏子", "2016-7-31", "https://www.amazon.co.jp/%E3%82%BD%E3%83%95%E3%83%88%E3%82%A6%E3%82%A7%E3%82%A2%E5%B7%A5%E5%AD%A6-%E5%B2%B8-%E7%9F%A5%E4%BA%8C-ebook/dp/B01JFGM9LC/ref=sr_1_1?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&dchild=1&keywords=%E3%82%BD%E3%83%95%E3%83%88%E3%82%A6%E3%82%A7%E3%82%A2%E5%B7%A5%E5%AD%A6&qid=1634999774&s=books&sr=1-1"),
    (0, "月刊少女野崎くん", "9784757535664", "椿いづみ", "2012-4-20", "https://www.amazon.co.jp/%E6%9C%88%E5%88%8A%E5%B0%91%E5%A5%B3%E9%87%8E%E5%B4%8E%E3%81%8F%E3%82%93-1-%E3%82%AC%E3%83%B3%E3%82%AC%E3%83%B3%E3%82%B3%E3%83%9F%E3%83%83%E3%82%AF%E3%82%B9ONLINE-%E6%A4%BF-%E3%81%84%E3%81%A5%E3%81%BF/dp/475753566X/ref=tmm_other_meta_binding_swatch_0?_encoding=UTF8&qid=1634999980&sr=1-6");

INSERT INTO article VALUES
    (0, 1, 1, "電子デバイスの魅力に引き込まれたこれこそ神の書物　アーメン", "2021-10-12", NULL, NULL),
    (0, 2, 1, "CMOOSの境地に達した", "2021-10-20", 1, 23),
    (0, 3, 2, "softwareの基礎がここにあり", "2021-10-1", NULL, 34),
    (0, 1, 2, "テストの重要性に気付かされた", "2021-9-5", 1, NULL),
    (0, 2, 3, "仕事に込める生き様に感化", "2021-3-4", 1, 9),
    (0, 3, 3, "気づきの重要性を学んだ", "2020-10-2", 3, 10);

