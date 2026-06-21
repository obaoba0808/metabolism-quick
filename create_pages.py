import os
import json

BASE = r"C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\metabolism-quick"

CSS = """:root{--brown:#4b2610;--brown2:#6b3b17;--gold:#a66d22;--gold2:#d9a348;--cream:#fff7e9;--red:#d71920;--dark:#1f160f;--line:#ead2a7}
*{box-sizing:border-box} html{scroll-behavior:smooth} body{margin:0;font-family:'Noto Sans TC','Microsoft JhengHei',Arial,sans-serif;color:var(--dark);background:#fffaf1} img{max-width:100%;display:block}
.wrap{max-width:1180px;margin:auto;padding:0 20px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;background:linear-gradient(180deg,#ff3a36,#c40000);color:#fff;text-decoration:none;font-weight:900;border-radius:16px;padding:18px 38px;font-size:24px;box-shadow:0 14px 28px #c4000040;border:0;cursor:pointer}
.btn.gold{background:linear-gradient(180deg,#d9a348,#8b5416)}
header{position:sticky;top:0;z-index:99;background:#fffdf8e8;backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}
.nav{height:68px;display:flex;align-items:center;justify-content:space-between}.logo{font-size:28px;font-weight:900;color:var(--gold)}.nav a{margin-left:20px;text-decoration:none;color:var(--brown);font-weight:800}
section{padding:68px 0}.title{text-align:center;margin-bottom:34px}.title h2{font-size:42px;color:var(--brown);margin:0 0 10px}.title p{font-size:20px;color:#7b5a35;margin:0}
.bar{background:linear-gradient(90deg,#5a3215,#b77a25);color:#fff;padding:18px 0;text-align:center;font-size:24px;font-weight:900}
.grid4{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}.grid5{display:grid;grid-template-columns:repeat(5,1fr);gap:18px}.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.card{background:#fff;border:1px solid var(--line);border-radius:24px;padding:24px;box-shadow:0 12px 30px #9f6a1b18}.card h3{margin:0 0 10px;color:var(--gold);font-size:25px}.card p{margin:0;line-height:1.7;font-size:17px}
.offer{background:#fff;border:3px solid var(--gold2);border-radius:32px;padding:38px;text-align:center;box-shadow:0 20px 60px #9f6a1b28}.price{font-size:76px;color:var(--red);font-weight:900;margin:8px 0}
.plans{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:24px}.plan{background:#fff7e8;border:2px solid #e0b05c;border-radius:22px;padding:22px}.plan h3{font-size:28px;margin:0 0 10px;color:var(--brown)}
.faq details{background:#fff;border:1px solid var(--line);border-radius:18px;padding:18px;margin-bottom:12px}.faq summary{font-weight:900;color:var(--brown);cursor:pointer}footer{padding:38px 0 95px;text-align:center;color:#6a4a29}
@keyframes pop{0%,75%,100%{transform:translateY(0);opacity:1}82%{transform:translateY(-8px);opacity:.9}}
@media(max-width:900px){.grid5,.grid4{grid-template-columns:1fr 1fr}.grid3,.plans{grid-template-columns:1fr}.nav a{display:none}}
@media(max-width:520px){.grid5,.grid4{grid-template-columns:1fr}.btn{width:100%;font-size:20px}}
.article-wrap{max-width:820px;margin:0 auto;padding:40px 20px}
.article-wrap h1{font-size:42px;color:var(--brown);margin:0 0 20px;line-height:1.3}
.article-wrap .meta{color:#7b5a35;font-size:15px;margin-bottom:30px}
.article-wrap p{line-height:1.9;margin-bottom:18px;font-size:18px;color:#3d2a14}
.article-wrap h2{font-size:32px;color:var(--brown);margin:40px 0 16px;padding-bottom:12px;border-bottom:2px solid var(--gold2)}
.article-wrap h3{font-size:24px;color:var(--brown2);margin:28px 0 12px}
.article-wrap ul{padding-left:24px;line-height:2}
.article-wrap li{margin-bottom:8px}
.toc{background:#fff7e8;border:2px solid #ead2a7;border-radius:20px;padding:24px 32px;margin:24px 0}
.toc h3{color:var(--gold);margin:0 0 12px;font-size:20px}
.toc a{color:var(--brown);text-decoration:none;display:block;padding:4px 0}
.toc a:hover{color:var(--gold)}"""

NAV = '<header><div class="wrap nav"><div class="logo">代謝Quick</div><nav><a href="/">首頁</a><a href="/plant-ingredients.html">成分介紹</a><a href="/eating-out-nutrition.html">外食攻略</a><a href="/turmeric-guide.html">薑黃指南</a><a href="/#offer">優惠方案</a><a href="/#order">預約</a></nav></div></header>'

FOOTER_NAV = """<nav style="background:#fff7e8;border-top:1px solid var(--line);padding:18px 0;text-align:center"><div class="wrap" style="display:flex;flex-wrap:wrap;justify-content:center;gap:20px;font-size:15px;font-weight:700"><a href="/" style="color:var(--brown);text-decoration:none">首頁</a><a href="/plant-ingredients.html" style="color:var(--brown);text-decoration:none">成分介紹</a><a href="/eating-out-nutrition.html" style="color:var(--brown);text-decoration:none">外食攻略</a><a href="/turmeric-guide.html" style="color:var(--brown);text-decoration:none">薑黃指南</a><a href="/#offer" style="color:var(--brown);text-decoration:none">優惠方案</a><a href="https://line.me/ti/g/nYhzNZQNf3" target="_blank" rel="noopener" style="color:var(--brown);text-decoration:none">LINE 官方</a></div></nav>"""

FOOTER = FOOTER_NAV + '\n<footer><div class="wrap">© 2026 代謝Quick. 本產品為一般食品，非醫療用品。所有產品資訊僅供參考，實際效果因個人體質而異。<br><span style="font-size:13px;color:#8a5a21">代謝Quick — 植物來源日常營養補給品牌 | 外食族、上班族、久坐族的飲食管理好夥伴</span></div></footer>'

DISCLAIMER = '<div style="background:#fff7e8;border:1px solid #ead2a7;border-radius:18px;padding:18px;color:#6a4a29;line-height:1.8;font-weight:700;margin-top:18px">\n※ 本產品為一般食品，非醫療用品。<br>\n※ 本頁內容不涉及疾病診斷、治療、減輕或預防。<br>\n※ 本產品無法取代醫療行為、藥品或醫師建議。<br>\n※ 實際感受會因個人體質、飲食與生活習慣而異；均衡飲食及適量運動為維持健康之基本。\n</div>'

CTA = """<section><div class="wrap"><div class="offer">
<h2>限時體驗價</h2><p>原價 <s>$1,980</s></p><div class="price">$1,280<span style="font-size:24px"> / 盒</span></div>
<p style="color:#d71920;font-weight:900;font-size:22px">🔥 今日下單現省 $700</p>
<a class="btn" href="https://line.me/ti/g/nYhzNZQNf3" target="_blank" rel="noopener">立即預約優惠 ▶</a>
<div class="plans"><div class="plan"><h3>單盒體驗組</h3><p style="font-size:22px;font-weight:900;color:#d71920">$1,280 / 盒</p><p>適合第一次體驗</p></div><div class="plan"><h3>買3盒送1盒</h3><p style="font-size:22px;font-weight:900;color:#d71920">平均 $960 / 盒</p><p style="color:#a66d22;font-weight:900">現省 $1,280，等於多拿一盒</p></div></div>
<p style="margin-top:20px;color:#8a5a21;font-weight:800">數量有限，售完為止｜下單後1-2天出貨</p>
</div></div></section>"""

def make_head(title, description, canonical, keywords, og_image="https://metabolism-quick.com/img/og-image.jpg"):
    return f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="google-site-verification" content="LorI-dc5BJVLPcJCf9miD9stXtU25ywTSMkhVbKHrmI" />
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="keywords" content="{keywords}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:url" content="{canonical}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="代謝Quick">
<meta property="og:locale" content="zh_TW">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{og_image}">
<link rel="alternate" hreflang="zh-TW" href="{canonical}">
<link rel="alternate" hreflang="x-default" href="{canonical}">"""

def make_article_jsonld(title, description, canonical):
    obj = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": description,
        "url": canonical,
        "datePublished": "2026-06-21",
        "dateModified": "2026-06-21",
        "author": {"@type": "Organization", "name": "代謝Quick"},
        "publisher": {"@type": "Organization", "name": "代謝Quick", "url": "https://metabolism-quick.com/"},
        "mainEntityOfPage": canonical
    }
    return json.dumps(obj, ensure_ascii=False, indent=2)

def make_faq_jsonld(faqs):
    entities = []
    for q, a in faqs:
        entities.append({"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}})
    obj = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": entities}
    return json.dumps(obj, ensure_ascii=False, indent=2)

def make_faq_html(faqs):
    html = '<section class="faq"><div class="wrap"><div class="title"><h2>常見問題</h2></div>\n'
    for q, a in faqs:
        html += f'<details><summary>{q}</summary><p>{a}</p></details>\n'
    html += DISCLAIMER
    html += '\n</div></section>'
    return html

def build_page(head_title, desc, canonical, keywords, article_jsonld, faq_jsonld, body_content, faq_html_content):
    article_ld = make_article_jsonld(article_jsonld[0], article_jsonld[1], canonical)
    faq_ld = make_faq_jsonld(faq_jsonld)
    return f"""<!doctype html>
<html lang="zh-Hant">
<head>
{make_head(head_title, desc, canonical, keywords)}
<script type="application/ld+json">{article_ld}</script>
<script type="application/ld+json">{faq_ld}</script>
<style>{CSS}</style>
</head>
<body>
{NAV}
{body_content}
{CTA}
{faq_html_content}
{FOOTER}
</body></html>"""

# ============================================================
# PAGE 1: turmeric-guide.html
# ============================================================
turmeric_faqs = [
    ("薑黃素每天建議攝取多少？", "一般建議薑黃素的日常補給量約為每日 200 至 500 毫克（以萃取物計算）。具體用量應依產品標示與個人需求調整，建議從少量開始，搭配足量飲水食用。若有特殊健康狀況，請先諮詢醫師或營養師。"),
    ("薑黃素有副作用嗎？", "薑黃素為一般常見的植物來源成分，在正常建議用量下多數人食用無明顯不適。極少數人可能出現輕微腸胃不適。若正在服用抗凝血藥物或有膽囊問題，建議先諮詢醫師。孕婦與哺乳期女性亦建議先向專業醫療人員確認。"),
    ("薑黃素可以空腹吃嗎？", "薑黃素為脂溶性成分，建議搭配含適量脂肪的餐食食用，有助於吸收率提升。空腹食用不會造成危害，但吸收效果可能較差。若選擇添加胡椒素（Piperine）的配方，餐後食用更為理想。"),
    ("薑黃素與藥物會有衝突嗎？", "薑黃素可能與抗凝血藥物（如華法林）、糖尿病藥物及部分胃藥產生交互作用。若您正在服用上述藥物或有慢性疾病，建議在食用薑黃素補給品前先諮詢醫師，確認是否適合同時使用。"),
    ("孕婦可以吃薑黃素嗎？", "一般飲食中適量使用薑黃粉調味是安全的，但高濃度薑黃素萃取物補給品，目前尚無足夠研究確認對孕婦與胎兒的安全性。建議孕婦在食用任何營養補給品前，先諮詢婦產科醫師的專業意見。"),
    ("薑黃素的吸收率如何提升？", "薑黃素天然吸收率較低，但可透過三種方式提升：一、搭配黑胡椒中的胡椒素（Piperine），可顯著提升生物利用率；二、與含脂肪的食物一起食用，因薑黃素為脂溶性；三、選擇經過奈米化或微乳化技術處理的配方，提升溶解度與吸收率。"),
    ("薑黃和薑黃素一樣嗎？", "不一樣。薑黃（Turmeric）是一種植物的根莖，是常見的香料與傳統草本；薑黃素（Curcumin）則是薑黃中最主要的活性成分，約占薑黃粉末的 2% 至 5%。日常食用薑黃粉能攝取到的薑黃素有限，因此若以補給為目的，通常會選擇濃縮萃取的薑黃素產品。"),
    ("薑黃素需要吃多久才有效？", "每個人體質、飲食習慣與作息不同，實際感受因人而異。一般建議持續食用至少 4 至 8 週，搭配均衡飲食與規律作息，讓身體逐步適應並累積。營養補給是長期生活習慣的一部分，不應期待短期速效。"),
]

turmeric_body = """<div class="article-wrap">
<h1>薑黃素完整指南：抗氧化與日常補給的科學解析</h1>
<div class="meta">最後更新：2026 年 6 月 21 日｜閱讀時間約 15 分鐘</div>

<div class="toc">
<h3>📋 目錄</h3>
<a href="#what-is-turmeric">一、薑黃是什麼？</a>
<a href="#curcumin-science">二、薑黃素的科學認識</a>
<a href="#daily-supply">三、日常補給方式</a>
<a href="#how-to-choose">四、如何選擇薑黃補給品</a>
<a href="#metabolism">五、薑黃與代謝健康的關聯</a>
<a href="#faq">六、常見問題</a>
</div>

<img src="img/ingredient.jpg" alt="薑黃植物來源成分" style="border-radius:20px;margin:24px 0" loading="lazy">

<h2 id="what-is-turmeric">薑黃是什麼？</h2>
<p>薑黃（學名：Curcuma longa）是薑科（Zingiberaceae）薑黃屬的多年生草本植物，原產於印度南部與東南亞熱帶地區。薑黃的根莖經乾燥研磨後，成為我們熟悉的金黃色粉末——這種香料不僅是咖哩的靈魂角色，更是人類使用超過四千年的傳統草本。</p>

<h3>產地與歷史</h3>
<p>印度是全球最大的薑黃生產國，佔世界總產量約 80%。印度南部克拉拉邦與泰米爾納德邦是主要產區，當地溫暖潮濕的氣候與肥沃的紅土為薑黃生長提供了絕佳條件。除了印度，孟加拉、巴基斯坦、斯里蘭卡及東南亞各國也有悠久的薑黃種植歷史。</p>
<p>薑黃的使用歷史可追溯至公元前 2500 年的印度河流域文明。在古代，薑黃不僅是珍貴的香料與染料，更被視為具有神聖意義的植物，廣泛用於宗教儀式與傳統醫學。阿拉伯商人將薑黃帶往歐洲，稱其為「印度番紅花」，而馬可波羅在遊記中也對薑黃的色澤與特性讚嘆不已。</p>

<h3>阿育吠陀中的薑黃</h3>
<p>在印度傳統醫學阿育吠陀（Ayurveda）中，薑黃被歸類為「萬靈草本」，意指用途廣泛的植物。阿育吠陀文獻記載薑黃可用於消化管理、皮膚保養、關節靈活度維持及日常體質調理等多個面向。阿育吠陀認為薑薑黃具有「溫熱」特性，適合用於平衡體內的能量流動，幫助維持身體的正常機能。</p>
<p>除了阿育吠陀，中國傳統本草學與泰國傳統醫學中也都有薑黃的記載。在中文古籍中，薑黃被稱為「郁金」，歸肝脾經，用於活血行氣。這種跨文化的共同使用經驗，反映出薑黃在不同文明中皆受到高度重視。日本沖繩的「鬱金」茶文化，更是薑黃在日常生活中扎根的例證。</p>

<h2 id="curcumin-science">薑黃素（Curcumin）的科學認識</h2>
<p>薑黃素（Curcumin）是薑黃中最具代表性的活性成分，也是賦予薑黃金黃色澤的主要物質。薑黃中約含有 2% 至 5% 的薑黃素類化合物，其中薑黃素佔最大比例（約 77%），其餘為去甲氧基薑黃素（Demethoxycurcumin）與雙去甲氧基薑黃素（Bisdemethoxycurcumin），三者合稱「薑黃素類化合物」（Curcuminoids）。</p>

<h3>抗氧化機制</h3>
<p>薑黃素的抗氧化特性是其在科學界最受關注的領域之一。抗氧化是指中和體內自由基、減少氧化壓力的過程。自由基是人體正常新陳代謝過程中產生的不穩定分子，當自由基過量累積時，可能對細胞造成氧化損傷，進而影響身體的正常功能與健康狀態。</p>
<p>研究指出，薑黃素能透過多種路徑發揮抗氧化作用：第一，薑黃素分子結構中的酚基團能直接捕捉自由基，中和其活性；第二，薑黃素能調節體內抗氧化酵素的活性，如超氧化物歧化酶（SOD）與麩胱甘肽過氧化酶（GPx），間接強化身體的抗氧化防禦系統；第三，薑黃素能螯合金屬離子，減少因金屬催化而產生的自由基鏈鎖反應。</p>
<p>值得注意的是，薑黃素的抗氧化能力在與其他植物成分搭配時，可能產生協同效應，即整體效果大於各成分單獨作用的總和。這也是為什麼代謝Quick選擇將薑黃與小茴香、肉桂、人參、三七等成分搭配組合的原因之一。</p>

<h3>抗發炎特性</h3>
<p>發炎反應是人體免疫系統的重要防禦機制，但當發炎反應持續過久或程度過強時，可能對身體組織造成負面影響。現代生活方式中，高壓力、不規律飲食、久坐不動等因素，都可能促使身體處於低度發炎狀態。</p>
<p>薑黃素在抗發炎領域的研究相當豐富。科學文獻指出，薑黃素能調節多種與發炎反應相關的分子路徑，包括抑制發炎介質的產生、調節細胞激素的表現，以及影響發炎相關酵素的活性。這些機制使薑黃素成為近年全球最受關注的植物來源成分之一。</p>
<p>根據 PubMed 資料庫統計，截至 2025 年，與薑黃素相關的科學論文已超過 20,000 篇，涵蓋抗氧化、抗發炎、代謝健康、腦部功能等多個研究領域。這些研究為薑黃素的日常補給價值提供了重要的科學基礎。美國化學學會（ACS）也將薑黃素列為最受研究的天然抗氧化劑之一。</p>

<h2 id="daily-supply">日常補給方式</h2>
<p>薑黃的日常補給方式多元，可依個人生活習慣與需求選擇最適合的方式。以下是三種常見的補給途徑：</p>

<h3>一、食品攝取</h3>
<p>最自然的方式是透過飲食攝取薑黃。薑黃粉是咖哩料理的核心香料，也可加入炒飯、湯品、燉菜等菜餚中。印度人平均每日飲食中約攝取 2 至 2.5 克薑黃，這也是印度被認為是薑黃使用最普及的國家的原因之一。然而，單靠飲食攝取的薑黃素含量有限（每 2 克薑黃粉約含 40 至 100 毫克薑黃素），且吸收率較低，對於有明確補給需求的人而言可能不足。</p>

<h3>二、茶飲方式</h3>
<p>薑黃茶（Golden Milk）是近年風靡全球的養生飲品，將薑黃粉與牛奶或植物奶混合，加入少許黑胡椒與肉桂調味。黑胡椒中的胡椒素能提升薑黃素吸收率達 2000%，而肉桂本身也是具有植化素的香料，搭配使用既美味又實用。薑黃茶適合在早晨或睡前飲用，是日常補給的溫和方式。</p>

<h3>三、營養補給品</h3>
<p>對於忙碌的外食族與上班族而言，營養補給品是最方便的選擇。市面上的薑黃補給品通常分為膠囊、錠劑與液態三種形式。優質的薑黃補給品會標示薑黃素含量、吸收率提升技術與第三方檢驗報告。代謝Quick 將薑黃與小茴香、肉桂、人參、三七搭配，以複方形式提供多元植物來源營養，適合日常規律食用。</p>

<h2 id="how-to-choose">如何選擇薑黃補給品</h2>
<p>市面上的薑黃補給品種類繁多，品質參差不齊。以下是選購時應注意的五個關鍵：</p>

<h3>一、薑黃素含量標示</h3>
<p>優質產品應清楚標示薑黃素（Curcuminoids）的實際含量，而非僅標示薑黃粉用量。薑黃粉與薑黃素萃取物的含量差異極大，消費者應確認產品標示的是有效成分含量，才能準確評估補給量。</p>

<h3>二、吸收率提升技術</h3>
<p>薑黃素天然吸收率偏低，好的產品會採用吸收率提升技術，如添加胡椒素（Piperine）、使用脂質體包覆技術、奈米化處理或微乳化技術。這些技術能顯著提升薑黃素的生物利用率，讓相同劑量發揮更好的效果。</p>

<h3>三、配方協同性</h3>
<p>單一成分的效果往往有限，研究顯示薑黃素與其他植物成分搭配時可能產生協同效應。例如薑黃素與肉桂搭配可強化抗氧化效果，與人參搭配則有助於活力支持。選擇複方產品時，應注意成分之間的搭配邏輯是否合理。</p>

<h3>四、品質認證與檢驗</h3>
<p>選擇有第三方檢驗報告的產品，確認無農藥殘留、重金屬超標或微生物污染。台灣製造的產品應符合衛福部食藥署的規範，消費者可查詢產品是否有 SGS、台美檢驗等機構的檢驗報告。代謝Quick 堅持台灣製造，每一批產品均經過嚴格檢驗把關。</p>

<h3>五、品牌信賴度</h3>
<p>品牌的透明度與售後服務也是重要考量。好的品牌會清楚標示所有成分、產地與製造資訊，並提供完善的客服管道。消費者可透過品牌官網、社群媒體評價與第三方平台了解品牌信譽。</p>

<h2 id="metabolism">薑黃與代謝健康的關聯</h2>
<p>代謝健康是現代人日益關注的議題。所謂代謝，是指人體將食物轉化為能量、維持各項生理機能運作的過程。良好的代謝狀態與均衡飲食、規律作息、適量活動密切相關。</p>
<p>薑黃素與代謝健康的關聯主要體現在三個方面：第一，薑黃素的抗氧化特性有助於減少代謝過程中的氧化壓力；第二，薑黃素調節發炎反應的能力，與代謝相關的發炎狀態有關聯；第三，部分研究探討薑黃素對胰島素敏感性與脂質代謝的潛在影響，但目前仍需更多臨床研究確認。</p>
<p>重要的是，薑黃素作為植物來源的營養補給成分，應視為日常健康管理的一部分，而非單一解決方案。搭配均衡飲食、規律運動與充足睡眠，才能建立完整的代謝健康管理模式。代謝Quick 以薑黃為核心，結合小茴香、肉桂、人參、三七等植物成分，提供外食族與上班族一個方便、安心的日常補給選擇。</p>
<p>對於經常外食、飲食不規律的上班族來說，薑黃素的日常補給可以作為飲食管理的重要輔助。每天固定時間食用，搭配均衡的三餐與足量飲水，讓植物來源營養成為生活節奏的一部分，長期累積才是日常健康管理的正確態度。</p>

<img src="img/m1.jpg" alt="薑黃素日常活力支持" style="border-radius:20px;margin:24px 0" loading="lazy">
</div>"""

turmeric_html = build_page(
    "薑黃素完整指南｜抗氧化與日常補給的科學解析 - 代謝Quick",
    "深入了解薑黃素（Curcumin）的抗氧化特性、抗發炎機制與日常補給方式。從產地到選購，完整解析薑黃素的科學基礎與實用知識。",
    "https://metabolism-quick.com/turmeric-guide.html",
    "薑黃素, 薑黃, Curcumin, 抗氧化, 抗發炎, 草本補給, 植物來源",
    ("薑黃素完整指南：抗氧化與日常補給的科學解析", "深入了解薑黃素（Curcumin）的抗氧化特性、抗發炎機制與日常補給方式。"),
    turmeric_faqs,
    turmeric_body,
    make_faq_html(turmeric_faqs)
)

# ============================================================
# PAGE 2: eating-out-nutrition.html
# ============================================================
eating_faqs = [
    ("外食族一定要吃保健食品嗎？", "不一定。如果外食時能刻意選擇均衡的餐點，多攝取蔬菜、適量蛋白質與全穀類，理論上可以從飲食中獲得足夠營養。但現實中，多數外食族的蔬果攝取量嚴重不足，且無法每天兼顧所有營養素。植物來源的營養補給品可以作為飲食的輔助，幫助補充日常飲食中可能缺乏的成分，但不能取代均衡飲食的重要性。"),
    ("便利商店怎麼選最健康？", "便利商店健康選購三原則：一、選擇原型食物優於加工品，如茶葉蛋優於熱狗、飯糰優於微波義大利麵；二、每餐至少搭配一份蔬菜，超商沙拉、關東煮蔬菜是方便選擇；三、注意鈉含量，盡量選擇鈉含量低於 600 毫克的餐點。飲料選擇無糖茶或黑咖啡，避免含糖飲料。"),
    ("午餐只吃麵會怎樣？", "單一食用麵食容易造成營養不均衡。一碗陽春麵或乾麵主要提供碳水化合物與少量蛋白質，缺乏蔬菜纖維與多種維生素礦物質。長期下來可能導致膳食纖維不足、維生素 B 群缺乏、血糖波動較大等問題。建議點麵時加點燙青菜與滷蛋，或搭配植物來源補給品補充日常飲食中不足的營養成分。"),
    ("外食族最容易缺乏哪些營養素？", "外食族最容易缺乏的五大營養素為：膳食纖維（蔬果攝取不足）、維生素 B 群（精緻澱粉為主食）、鈣質（乳製品攝取少）、鎂（深綠蔬菜不足）及 Omega-3 脂肪酸（魚類攝取少）。這些營養素的缺乏可能影響日常精神狀態、消化功能與代謝效率，建議透過飲食調整與適當補給雙管齊下。"),
    ("晚上加班吃宵夜怎麼辦？", "加班宵夜建議選擇低油低糖、容易消化的食物，如溫牛奶、無糖豆漿、全麥吐司或水果。避免油炸、高糖與高咖啡因的食物，以免影響睡眠品質。如果真的很餓，超商茶葉蛋配無糖豆漿是不錯的選擇。長期來說，建議調整晚餐時間與份量，減少宵夜的需求。"),
    ("自助餐怎麼夾才健康？", "自助餐健康夾法四步驟：一、先夾兩到三種蔬菜，佔餐盒一半面積；二、選擇一種優質蛋白質，如滷雞腿、蒸魚或豆腐；三、主食選白飯半碗或糙米飯，避免油炸主食；四、避免勾欠與重油烹調的菜色。記得少淋滷汁，減少鈉與油脂的攝取。"),
    ("上班族一天要喝多少水？", "一般建議成年人每日飲水量約為體重（公斤）乘以 30 至 35 毫升，例如 60 公斤的人每日建議飲水 1800 至 2100 毫升。上班族常因忙碌而忘記喝水，建議在桌面放置水壺，設定定時提醒。充足飲水有助於代謝正常運作，也幫助營養補給品的吸收與利用。"),
]

eating_body = """<div class="article-wrap">
<h1>外食族營養補給指南：上班族飲食管理完整攻略</h1>
<div class="meta">最後更新：2026 年 6 月 21 日｜閱讀時間約 16 分鐘</div>

<div class="toc">
<h3>📋 目錄</h3>
<a href="#dilemma">一、外食族的營養困境</a>
<a href="#smart-choices">二、外食聰明選擇指南</a>
<a href="#nutrient-gap">三、外食族最容易缺乏的 5 大營養素</a>
<a href="#plant-supplement">四、植物來源補給品的角色</a>
<a href="#weekly-plan">五、一週外食營養管理計畫表</a>
<a href="#faq">六、常見問題</a>
</div>

<img src="img/m2.jpg" alt="外食族飲食管理與營養補給" style="border-radius:20px;margin:24px 0" loading="lazy">

<h2 id="dilemma">外食族的營養困境</h2>
<p>根據衛福部國民營養健康調查，台灣成年人外食比例超過 65%，其中上班族更高達 80% 以上。外食雖然方便快速，卻潛藏著嚴重的營養失衡危機。以下解析外食族面臨的三大營養困境：</p>

<h3>高油高鹽低纖維</h3>
<p>外食餐點為了追求口感與風味，往往使用大量油脂與調味料。一碗看似簡單的滷肉飯，鈉含量可能超過每日建議攝取量的一半；一份炸排骨便當的油脂含量，可能達到一天建議量的 70%。更令人擔憂的是纖維攝取不足——多數外食餐點的蔬菜份量遠低於建議量，長期下來影響消化功能與腸道健康。</p>
<p>以便利商店的微波便當為例，一個炸雞排便當的熱量約 700 至 900 大卡，其中脂肪佔了將近 40%，而蔬菜份量通常不到一份。一碗牛肉麵的鈉含量更高達 2000 至 3000 毫克，接近每日建議上限。這些數據顯示，外食者在不知不覺中攝取了過多的油脂與與鈉，卻嚴重缺乏纖維與微量元素。</p>

<h3>蔬果嚴重不足</h3>
<p>世界衛生組織建議每日攝取至少 400 公克蔬果（約五份），但台灣成年人平均每日蔬果攝取量僅約 2.5 份，不到建議量的一半。外食族的狀況更為嚴重，許多上班族一整天只吃到一至兩份蔬菜。蔬果攝取不足意味著膳食纖維、維生素、礦物質與植化素的攝取量全面偏低，對日常健康與代謝功能造成長期影響。</p>
<p>蔬果不足的後果是全方位的：膳食纖維不足影響腸道蠕動與飽足感，維生素 C 不足影響免疫力與抗氧化能力，鉀離子不足影響血壓調節，而各種植化素的缺乏則讓身體少了來自植物的自然保護。這就是為什麼植物來源營養補給品對外食族格外重要的原因。</p>

<h3>蛋白質攝取不均</h3>
<p>外食族的蛋白質來源往往偏向單一，大多來自豬肉、雞肉等動物性蛋白質，缺乏植物性蛋白質的攝取。同時，蛋白質的攝取時間也常不均勻——早餐蛋白質不足，晚餐又過量。研究指出，均勻分配三餐蛋白質攝取，比集中在單一餐次更能有效支持肌肉維持與代謝功能。</p>
<p>另一個常被忽略的問題是蛋白質的品質。外食中的蛋白質多伴隨大量油脂（如炸排骨、滷肉），雖然總蛋白質量可能足夠，但同時也攝取了過多的飽和脂肪與膽固醇。理想的蛋白質攝取應兼顧動物性與植物性來源，且盡量選擇低脂的烹調方式。</p>

<h2 id="smart-choices">外食聰明選擇指南</h2>
<p>外食不代表只能將就，只要掌握正確的選擇技巧，即使在外用餐也能兼顧營養均衡。以下針對四種常見的外食場景提供實用建議：</p>

<h3>便利商店選擇技巧</h3>
<p>便利商店是上班族最常光顧的外食地點，雖然選擇有限，但仍有健康方案可尋。主食選擇飯糰或地瓜優於麵包；蛋白質來源以茶葉蛋、無糖豆漿、雞胸肉為佳；蔬菜則可搭配超商沙拉或關東煮的蘿蔔、海帶。避免選擇炸物、微波義大利麵與含糖飲料，這些都是高油高糖低營養密度的典型外食陷阱。</p>

<h3>便當店選擇技巧</h3>
<p>便當店的關鍵在於「客製化」。點餐時主動要求少飯多菜，選擇蒸、煮、滷的主菜取代油炸。若主菜只有炸的選項，可以剝去外皮減少油脂攝取。配菜盡量選擇深綠色蔬菜，避免勾欠類或重油炒製的菜色。湯品選擇清湯取代濃湯，飯後不要加滷汁拌飯。</p>

<h3>麵食店選擇技巧</h3>
<p>麵食最大的問題是蔬菜與蛋白質不足。點麵時務必加點燙青菜或滷白菜，再搭配一顆滷蛋或豆干增加蛋白質。麵條選擇上，湯麵優於乾麵（減少拌醬的油量），陽春麵優於牛肉麵（減少湯底的油脂）。如果可以，選擇較粗的麵條，血糖上升速度較慢。</p>

<h3>自助餐選擇技巧</h3>
<p>自助餐是外食族最能自主掌控營養的選項。核心原則是「蔬菜佔一半、蛋白質佔四分之一、主食佔四分之一」。蔬菜優先選深綠色，蛋白質選白肉或豆製品，主食可選糙米飯。避免所有勾欠菜色（代表添加了太白粉與額外油脂），滷汁少淋或不淋。</p>

<h2 id="nutrient-gap">外食族最容易缺乏的 5 大營養素</h2>
<p>根據國民營養調查與外食飲食分析，外食族最容易缺乏以下五種營養素：</p>

<h3>一、膳食纖維</h3>
<p>建議每日攝取 25 至 30 公克，外食族平均僅攝取 12 至 15 公克。膳食纖維不足影響腸道蠕動、消化功能與飽足感，也與血糖穩定度有關。補充方式：每餐至少吃一份蔬菜，選擇全穀類主食，搭配豆類與水果。若日常飲食難以達標，可透過含纖維的植物來源補給品輔助。</p>

<h3>二、維生素 B 群</h3>
<p>維生素 B 群是能量代謝的重要輔酶，外食族因精緻澱粉攝取多、全穀類攝取少，容易缺乏。B 群不足可能影響精神狀態與代謝效率。補充方式：選擇糙米飯、全麥麵包，搭配深綠蔬菜與豆類。植物來源補給品中的肉桂與人參也含有助於能量代謝的植物性成分。</p>

<h3>三、鈣質</h3>
<p>外食族乳製品攝取少，鈣質普遍不足。鈣質不僅關乎骨骼健康，也與肌肉收縮、神經傳導及代謝功能有關。補充方式：選擇加鈣豆漿、深綠蔬菜、傳統豆腐。避免過量咖啡因，以免加速鈣質流失。</p>

<h3>四、鎂</h3>
<p>鎂參與體內超過 300 種酵素反應，與能量代謝、肌肉放鬆及神經功能密切相關。深綠蔬菜、堅果與全穀類是鎂的主要來源，但外食族這些食物攝取偏少。補充方式：每天吃一小把堅果當零食，選擇糙米飯，多點深綠蔬菜。</p>

<h3>五、植物性植化素</h3>
<p>植化素是植物中特有的活性成分，如薑黃素、類黃酮、多酚類等，具有抗氧化與調節生理機能的作用。外食族因蔬果種類單一，植化素的攝取種類與數量都嚴重不足。補充方式：增加蔬果種類多樣性，搭配含有多種植物成分的營養補給品，如代謝Quick 的五大植物來源配方。</p>

<h2 id="plant-supplement">植物來源補給品的角色</h2>
<p>很多人會問：「我已經盡量選健康的餐點了，還需要補給品嗎？」答案是——補給品不是取代飲食，而是補充飲食的不足。</p>
<p>植物來源補給品的核心價值在於三個方面：第一，補充外食中缺乏的植物性活性成分，如薑黃素、人參皂苷等植化素；第二，提供多種植物成分的協同搭配，單一食物難以同時涵蓋；第三，建立規律的日常補給習慣，讓健康管理成為生活的一部分。</p>
<p>代謝Quick 選擇薑黃、小茴香、肉桂、人參、三七五種植物來源成分，正是基於「多元協同」的理念。每一種成分都來自不同的植物傳統與活性成分類型，搭配使用可以提供更全面的植物性營養補給。對於每天只能將就外食的上班族而言，這種便利的補給方式是飲食管理的重要輔助。</p>
<p>當然，補給品不能取代均衡飲食。理想的模式是：盡可能在外食中做出健康選擇，同時以植物來源補給品補充飲食中不足的營養成分，雙管齊下，讓日常營養管理更完整。這也是代謝Quick 一直強調「搭配均衡飲食與規律作息」的原因——補給品是生活管理的一部分，不是速效的捷徑。</p>

<h2 id="weekly-plan">一週外食營養管理計畫表</h2>
<p>以下提供一週五天的工作日外食營養管理管理範例，幫助外食族在有限的選擇中做出更好的決定：</p>

<h3>星期一：調整日</h3>
<p>早餐：全麥吐司加蛋＋無糖豆漿。午餐：自助餐——半碗糙米飯＋兩份蔬菜＋滷雞腿。晚餐：便利商店——雞胸肉沙拉＋地瓜。補給：代謝Quick 搭配午餐食用。週一的重點是從週末的放縱中回歸規律，飲食盡量清淡，補充足夠蔬菜。</p>

<h3>星期二：穩定日</h3>
<p>早餐：燕麥飲＋茶葉蛋。午餐：便當店——少飯多菜＋清蒸魚排。晚餐：麵食店——湯湯麵＋燙青菜＋滷蛋。補給：代謝Quick 搭配午餐食用。維持穩定的飲食節奏，避免下午茶的誘惑。</p>

<h3>星期三：補強日</h3>
<p>早餐：飯糰＋無糖綠茶。午餐：自助餐——白飯半碗＋三份蔬菜＋豆腐。晚餐：便利商店——關東煮（蘿蔔、海帶、蛋）＋飯糰。補給：代謝Quick 搭配午餐食用。週三是一週的中點，容易因疲憊而放縱飲食，特別注意下午茶的選擇。</p>

<h3>星期四：維持日</h3>
<p>早餐：全麥三明治＋黑咖啡。午餐：麵食店——陽春湯麵＋燙青菜＋豆干。晚餐：便當店——滷排骨便當（去油炸皮）＋多加蔬菜。補給：代謝Quick 搭配午餐食用。持續維持前三天的飲食節奏，避免因接近週末而鬆懈。</p>

<h3>星期五：彈性日</h3>
<p>早餐：地瓜＋無糖豆漿。午餐：自助餐——半碗飯＋兩份蔬菜＋蒸魚。晚餐：聚餐或外食——適度享受，但控制份量。補給：代謝Quick 搭配午餐食用。週五可以有適度的彈性，但不要完全放棄飲食原則。</p>

<p>這個計畫表的核心理念是「規律中求均衡，彈性中不失原則」。不需要每天完美，但需要每天有意識地選擇。搭配代謝Quick 的植物來源營養補給，讓外食族的日常營養管理更加完整。</p>

<img src="img/m4.jpg" alt="外食族輕盈生活感" style="border-radius:20px;margin:24px 0" loading="lazy">
</div>"""

eating_html = build_page(
    "外食族營養補給指南｜上班族飲食管理完整攻略 - 代謝Quick",
    "外食族與上班族的營養補給完整攻略。破解外食營養困境，提供便利商店、便當店聰明選擇技巧，以及植物來源補給品的搭配建議。",
    "https://metabolism-quick.com/eating-out-nutrition.html",
    "外食族, 上班族, 營養補給, 飲食管理, 营养不均, 外食营养, 便当营养",
    ("外食族營養補給指南：上班族飲食管理完整攻略", "外食族與上班族的營養補給完整攻略。破解外食營養困境，提供聰明選擇技巧。"),
    eating_faqs,
    eating_body,
    make_faq_html(eating_faqs)
)

# ============================================================
# PAGE 3: plant-ingredients.html
# ============================================================
plant_faqs = [
    ("這些成分有科學根據嗎？", "代謝Quick 所使用的五種植物成分，每一種都有豐富的科學研究基礎。薑黃素相關論文超過 20,000 篇、人參皂苷超過 10,000 篇、肉桂多酚相關研究超過 5,000 篇，小茴香與三七也各有大量文獻支持。這些成分在各自的傳統醫學體系中已有數百年至數千年的使用歷史，現代科學研究則為其活性成分與作用機制提供了更深入的理解。"),
    ("這五種成分可以一起吃嗎？", "可以。代謝Quick 的配方設計正是基於五種成分的協同搭配理念。每種成分來自不同的植物科屬與活性成分類型，搭配使用時可以提供更全面的植物性營養補給。研究顯示，不同植物成分之間可能產生協同效應，即整體效果優於單一成分的加總。當然，建議依產品標示的建議用量食用。"),
    ("會不會過敏？", "薑黃、小茴香、肉桂、人參、三七都是常見的食用植物，一般人群食用過敏的機率很低。但每個人的體質不同，若您對上述任何一種成分有已知過敏史，建議避免食用。初次食用任何新的補給品時，建議從少量開始，觀察身體反應。若出現不適，請停止食用並諮詢醫師。"),
    ("小孩可以吃嗎？", "代謝Quick 主要針對成年人的日常營養補給需求設計，不建議 12 歲以下兒童食用。12 歲以上青少年如有補給需求，建議先諮詢小兒科醫師或營養師的專業意見，確認適合的食用量與方式。"),
    ("這些成分的產地來源是哪裡？", "薑黃主要來自印度及台灣在地種植；小茴香源自地中海區域的傳統產區；肉桂來自亞熱帶地區的香料產區；人參選用東亞地區的優質人參；三七則來自中國來自中國雲南、廣西等傳統產區。代謝Quick 堅持選用品質可靠的植物來源原料，並透過嚴格的檢驗把關確保產品品質。"),
    ("植物來源成分和合成成分有什麼差別？", "植物來源成分來自天然植物萃取，保留了植物中多種活性成分的天然比例與組合，這些成分之間可能存在協同作用。合成成分則是實驗室中合成的單一化合物，雖然純度高，但缺少了天然植物中複雜的成分組合。許多研究指出，天然植物萃取物的整體效果往往優於等量的單一合成成分，這可能與植物中其他微量成分的輔助作用有關。"),
]

plant_body = """<div class="article-wrap">
<h1>五大植物來源成分深度解析</h1>
<div class="meta">最後更新：2026 年 6 月 21 日｜閱讀時間約 18 分鐘</div>

<div class="toc">
<h3>📋 目錄</h3>
<a href="#why-plant">一、為什麼選擇植物來源？</a>
<a href="#turmeric">二、薑黃深度解析</a>
<a href="#fennel">三、小茴香深度解析</a>
<a href="#cinnamon">四、肉桂深度解析</a>
<a href="#ginseng">五、人參深度解析</a>
<a href="#notoginseng">六、三七深度解析</a>
<a href="#synergy">七、五成分協同搭配的科學</a>
<a href="#faq">八、常見問題</a>
</div>

<img src="img/ingredient.jpg" alt="五大植物來源成分" style="border-radius:20px;margin:24px 0" loading="lazy">

<h2 id="why-plant">為什麼選擇植物來源？</h2>
<p>在營養補給品的領域中，成分來源可分為植物來源（天然萃取）與合成來源（化學合成）兩大類。代謝Quick 選擇植物來源成分，不僅是因為消費者對天然成分的偏好，更是基於科學研究的支持。</p>
<p>植物來源成分與合成成分之間存在幾個關鍵差異：第一，天然植物萃取物保留了多種活性成分的天然比例，這些成分之間可能存在協同作用，使整體效果優於單一成分的加總；第二，植物來源成分通常伴隨其他微量植化素，這些微量成分雖然不是主要活性成分，卻可能在人體中發揮輔助作用；第三，植物來源成分的生物相容性通常較好，人體的吸收與利用效率可能更佳。</p>
<p>合成成分的優勢在於純度高、成本較低、品質穩定。但越來越多的研究指出，天然植物萃取物在整體效果上往往優於等量的純化合成成分，這個現象被稱為「植物基質效應」（Phytomatrix Effect）。正因如此，代謝Quick 堅持使用植物來源成分，為消費者提供更貼近自然、更全面的營養補給選擇。</p>
<p>此外，植物來源成分的永續性也是考量之一。透過選擇來自可持續農業的植物原料，不僅能確保產品品質，也減少對環境的負擔。每一種植物都有其獨特的生長環境與採收方式，代謝Quick 在原料篩選時，會綜合考量產地品質、農法可持續性與成分活性等多重因素。</p>

<h2 id="turmeric">薑黃深度解析</h2>
<p><strong>學名：</strong>Curcuma longa<br>
<strong>科屬：</strong>薑科（Zingiberaceae）薑黃屬<br>
<strong>主要產地：</strong>印度、台灣、東南亞<br>
<strong>核心活性成分：</strong>薑黃素（Curcumin）、去甲氧基薑黃素、雙去甲氧基薑黃素</p>
<p>薑黃是代謝Quick 五大成分中最受全球科學界關注的植物。薑黃素（Curcumin）是薑黃中含量最豐富的薑黃素類化合物，約佔薑黃素的 77%。薑黃素的分子結構中含有兩個酚基團與一個β-二酮基團，這些結構特徵賦予了薑黃素強大的抗氧化能力。</p>
<p>在印度阿育吠陀醫學中，薑黃被稱為「印度黃金」，已有超過四千年的使用歷史。印度人平均每日飲食中攝取約 2 至 2.5 克薑黃，這也是印度在全球薑黃消費量中居首的原因。台灣也有種植薑黃的傳統，主要產區集中在花蓮、台東等地，台灣薑黃因品質優良而受到關注。</p>
<p>截至 2025 年，PubMed 資料庫中與薑黃素相關的科學論文已超過 20,000 篇，研究範圍涵蓋抗氧化、抗發炎、代謝健康、腦部功能、關節保健等多個領域。這些研究為薑黃素作為日常營養補給成分提供了堅實的科學基礎。美國國家衛生研究院（NIH）也將薑黃素列為重點研究的高潛力天然成分。</p>

<h2 id="fennel">小茴香深度解析</h2>
<p><strong>學名：</strong>Foeniculum vulgare<br>
<strong>科屬：</strong>繖形科（Apiaceae）茴香屬<br>
<strong>主要產地：</strong>地中海區域、中東、印度<br>
<strong>核心活性成分：</strong>茴香精油（Anethole）、黃酮類化合物、酚酸類</p>
<p>小茴香是地中海與中東料理中不可或缺的芳香草本，其使用歷史可追溯至古埃及時代。古希臘人稱小茴香為「Marathon」，意指「變瘦」，反映了古人對小茴香與體態管理的關聯認識。在歐洲草本醫學傳統中，小茴香被廣泛用於消化管理與日常體質調理。</p>
<p>小茴香的主要活性成分茴香精油（反式茴香腦，trans-Anethole）具有獨特的芳香風味，同時也展現出抗氧化特性。小茴香中的黃酮類化合物（如槲皮素、山奈酚）與酚酸類成分也具有清除自由基的能力，這使得小茴香在植物來源營養補給中扮演重要角色。</p>
<p>小茴香與薑黃的搭配特別值得關注。研究顯示，小茴香中的活性成分可能強化薑黃素的抗氧化效果，形成協同作用。地中海飲食之所以被公認為全球最健康的飲食模式之一，其中小茴香等香草的貢獻不容忽視。代謝Quick 將小茴香與薑黃搭配使用的科學基礎，正源自這種傳統智慧與現代研究的交匯。</p>

<h2 id="cinnamon">肉桂深度解析</h2>
<p><strong>學名：</strong>Cinnamomum spp.<br>
<strong>科屬：</strong>樟科（Lauraceae）樟屬<br>
<strong>主要產地：</strong>斯里蘭卡、中國南方、越南、印尼<br>
<strong>核心活性成分：</strong>肉桂醛（Cinnamaldehyde）、肉桂酸、原花青素、多酚類</p>
<p>肉桂是全球最受歡迎的香料之一，在東西方的烹飪與傳統醫學中都有重要地位。肉桂主要分為兩大品種：錫蘭肉桂（Ceylon Cinnamon，又稱真肉桂）與中國肉桂（Cassia，又稱桂皮）。兩者在活性成分比例與風味上有所差異，但都含有豐富的植化素。</p>
<p>肉桂中最具代表性的活性成分是肉桂醛（Cinnamaldehyde），佔肉桂精油的 60% 至 80%。肉桂醛具有獨特的溫暖香氣，同時在研究中展現出抗氧化與調節生理機能的潛力。此外，肉桂中的原花青素（Proanthocyanidins）與多酚類化合物也是重要的活性成分，這些植化素與薑黃素的抗氧化作用可能形成互補。</p>
<p>在傳統應用上，肉桂在東亞被歸為「溫裡藥」，用於驅寒溫中；在歐洲中世紀，肉桂是比黃金更珍貴的貿易商品。現代研究則聚焦於肉桂多酚在代謝健康領域的潛力，相關科學論文已超過 5,000 篇。肉桂與薑黃的搭配，在 Golden Milk 等傳統飲品中已有悠久歷史，兩者的協同效應也得到越來越多科學關注。</p>

<h2 id="ginseng">人參深度解析</h2>
<p><strong>學名：</strong>Panax ginseng<br>
<strong>科屬：</strong>五加科（Araliaceae）人參屬<br>
<strong>主要產地：</strong>韓國、中國東北、俄羅斯遠東<br>
<strong>核心活性成分：</strong>人參皂苷（Ginsenosides）、多醣體、多肽</p>
<p>人參是東亞地區最重要的傳統滋補草本，被譽為「百草之王」，使用歷史超過兩千年。人參屬的學名 Panax 來自希臘文「Panakos」，意為「萬靈丹」，反映了古人對人參的高度評價。</p>
<p>人參中最受關注的活性成分是人參皂苷（Ginsenosides），目前已分離出超過 150 種不同的人參皂苷，每一種都有其獨特的結構與作用特性。人參皂苷可分為達瑪烷型（Dammarane）與齊墩果酸型（Oleanane）兩大類，其中達瑪烷型中的 Rb1、Rg1、Rd 等是研究最廣泛的成分。</p>
<p>人參在東亞傳統醫學中被歸類為「補氣」藥材，用於增強體力、恢復精神與調節生理機能。現代研究則探討人參皂苷在活力支持、認知功能、免疫調節與代謝健康等領域的潛力。截至 2025 年，人參皂苷相關的科學論文已超過 10,000 篇，是人參科學研究的重要基石。</p>
<p>人參與三七同屬五加科，兩者在活性成分上有共通之處（都含有人參皂苷），但各自的皂苷種類與比例不同，搭配使用時可以提供更全面的皂苷譜，這也是代謝Quick 將兩者搭配的科學考量之一。在東亞傳統醫學中，人參與三七的配伍由來已久，兩者的搭配被認為能夠互補長短，提供更全面的草本營養補給。</p>

<h2 id="notoginseng">三七深度解析</h2>
<p><strong>學名：</strong>Panax notoginseng<br>
<strong>科屬：</strong>五加科（Araliaceae）人參屬<br>
<strong>別名：</strong>田七、金不換、血參<br>
<strong>主要產地：</strong>中國雲南、廣西<br>
<strong>核心活性成分：</strong>三七皂苷（Notoginsenosides）、人參皂苷、三七素、黃酮類</p>
<p>三七又稱田七，是中國雲南、廣西地區的道地草本，與人參同屬五加科人參屬。三七的名稱由來有多種說法，一說因其葉片多為三小葉、七片複葉而得名；另一說指其需要種植三至七年才能採收。三七在雲南文山州有「金不換」之稱，反映出其在當地的珍貴地位。</p>
<p>三七含有獨特的三七皂苷（Notoginsenosides），這是人參中所沒有或含量極低的特殊皂苷種類。三七皂苷 R1、R2、R3、R4、R6 等是三七最具代表性的活性成分。此外，三七還含有三七素（Dencichine），這是一種具有止血作用的氨基酸類化合物。</p>
<p>在中國傳統本草學中，三七被歸為「活血化瘀」類藥材，明代李時珍在《本草綱目》中記載三七「止血散血定痛」。現代研究則探討三七皂苷在循環健康、抗氧化與代謝功能等領域的潛力。三七與人參的搭配，提供了五加科植物中更完整的皂苷譜，是代謝Quick 複方配方的亮點之一。</p>
<p>三七的種植條件非常嚴格，需要高海拔、適當蔭蔽與特殊土壤條件，這也是優質三七產量有限的原因之一。雲南文山被譽為「三七之鄉」，當地的風土條件為三七提供了理想的生長環境，也使得文山三七在品質上享有盛譽。</p>

<h2 id="synergy">五成分協同搭配的科學</h2>
<p>代謝Quick 選擇薑黃、小茴香、肉桂、人參、三七五種植物來源成分，不是隨機組合，而是基於「協同效應」的科學理念。協同效應是指多種成分搭配使用時，整體效果大於各成分單獨效果的加總，即 1+1>2。</p>

<h3>抗氧化協同</h3>
<p>薑黃素、肉桂多酚、小茴香黃酮、人參皂苷與三七皂苷都各自具有抗氧化能力，但它們的作用機制不盡相同。薑黃素主要透過酚基團捕捉自由基，肉桂醛透過調節抗氧化酵素，人參皂苷透過活化細胞內的抗氧化路徑。多種抗氧化機制同時作用，可以提供更全面的抗氧化保護網，覆蓋更多類型的自由基與氧化壓力源。</p>

<h3>傳統醫學的協同理論</h3>
<p>有趣的是，五成分的搭配也呼應了傳統醫學中的配伍理念。在中國傳統本草學中，「君臣佐使」的配伍原則強調多種藥材搭配使用時的分工與協作；在印度阿育吠陀中，「Triphala」等複方也體現了多種植物成分協同使用的傳統智慧。代謝Quick 的五成分配方，某種程度上承襲了這種「整體大於部分之和」的東方醫學哲學。</p>

<h3>成分之間的具體協同</h3>
<p>薑黃與小茴香的搭配，可能有助於薑黃素的吸收與抗氧化效果的強化；肉桂的溫性特質與人參的補氣作用形成互補，提供日常活力支持；人參與三七同屬五加科，兩者的皂苷譜互相補充，提供更全面的人參皂苷種類。薑黃與肉桂在 Golden Milk 中的經典搭配已有數百年歷史，現代科學正逐步揭示其背後的協同機制。</p>
<p>代謝Quick 的五大植物來源成分配方，正是「多元協同」理念的具體實踐。每一種成分都不是可有可無的點綴，而是整體配方中不可或缺的一環，共同為外食族與上班族的日常營養補給提供更全面、更安心的選擇。這種複方思維也符合現代營養學中「食物矩陣」的概念——營養素不是孤立存在的，而是在複雜的食物基質中相互影響、共同作用的。</p>

<img src="img/m3.jpg" alt="五大植物來源成分營養平衡支持" style="border-radius:20px;margin:24px 0" loading="lazy">
</div>"""

plant_html = build_page(
    "五大植物來源成分解析｜薑黃小茴香肉桂人參三七 - 代謝Quick",
    "深入解析薑黃、小茴香、肉桂、人參、三七五大植物來源成分的活性物質、傳統應用與現代研究，探討五成分協同搭配的科學基礎。",
    "https://metabolism-quick.com/plant-ingredients.html",
    "植物來源成分, 薑黃, 小茴香, 肉桂, 人參, 三七, 植萃配方, 天然成分",
    ("五大植物來源成分深度解析", "深入解析薑黃、小茴香、肉桂、人參、三七五大植物來源成分的活性物質與協同效應。"),
    plant_faqs,
    plant_body,
    make_faq_html(plant_faqs)
)

# Write all HTML files
for name, content in [("turmeric-guide.html", turmeric_html), ("eating-out-nutrition.html", eating_html), ("plant-ingredients.html", plant_html)]:
    path = os.path.join(BASE, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    size = os.path.getsize(path)
    print(f"Written: {path} ({size} bytes)")

# Write sitemap.xml
sitemap = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://metabolism-quick.com/</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://metabolism-quick.com/turmeric-guide.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://metabolism-quick.com/eating-out-nutrition.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://metabolism-quick.com/plant-ingredients.html</loc>
    <lastmod>2026-06-21</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>"""

sitemap_path = os.path.join(BASE, "sitemap.xml")
with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write(sitemap)
print(f"Written: {sitemap_path}")

print("\nAll 4 files created successfully!")
