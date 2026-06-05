# I-TOP Therm AI Visual Generation System

نظام توليد صور AI مخصص لهوية مشروع I-TOP Therm، مبني على مراجعة صور المصنع وكتالوجات المنتجات الموجودة محليًا.

الغرض من هذا الملف هو توحيد شكل كل الصور المستقبلية للمشروع: صور الموقع، العروض التنفيذية، LinkedIn، صفحات المنتجات، RFQ، CRM، التوزيع، والمشاريع.

## 1. مصدر الهوية البصرية

المراجع المحلية:

- `صور من المصنع/`: صور خطوط إنتاج، فنيين، معدات، منتجات، عبوات، مخزون، HDPE coils، UPVC pipes، PP-R fittings.
- `البروفايلات/`: كتالوجات PP-R وUPVC وUPVC/CPVC fittings.
- الشعار الرسمي: كلمة I-TOP بالأخضر الداكن مع دائرة برتقالية/ذهبية ولمسة أخضر فاتح، وأسفلها `THERM INDUSTRY CO.` والنص العربي.
- أصل الشعار الرسمي داخل المشروع: `assets/logo-itop-original.png`.

ملاحظات مستخلصة من الصور:

- المصنع حقيقي وعملي، وليس فخمًا أو دعائيًا بشكل مبالغ.
- البيئة نظيفة ومنظمة: أرضيات فاتحة، خطوط إنتاج طويلة، عمال بقبعات أمان وسترات، معدات بثلاثة ألوان رئيسية: أخضر، أبيض/رمادي، أسود/برتقالي.
- المنتجات البارزة:
  - PP-R fittings باللون الأخضر.
  - UPVC pipes باللون الأبيض/الرمادي.
  - HDPE pipes and coils باللون الأسود.
  - Orange corrugated coils للتطبيقات ذات الصلة.
  - عبوات I-TOP وpackaging حاضرة في الصور.
- أفضل اتجاه بصري: واقعية صناعية نظيفة، إضاءة مصنع، تكوين تنفيذي، لا دراما، لا زحام.

## 2. هوية الصور المعتمدة

### الشكل العام

- Photorealistic industrial executive visuals.
- Clean Saudi pipe manufacturing environment.
- Real production lines, product racks, packaging, safety workers, technical screens.
- Premium but practical, suitable for board presentation.
- Clear product evidence, not generic factory stock imagery.

### الألوان

- Off-white / warm ivory background.
- Deep logo green as the dominant brand color.
- Warm orange / golden orange accent from the logo.
- Fresh lime green as a small secondary accent only.
- Charcoal / dark grey technical elements.
- Product colors: PP-R green, UPVC white/grey, HDPE black, orange coils.

ألوان تقريبية قابلة للاستخدام في التصميم:

| الدور | اللون التقريبي |
|---|---|
| Logo deep green | `#0f3b20` |
| Industrial deep green | `#123c35` |
| Logo orange / gold | `#f0a21a` |
| Muted executive orange | `#c8753e` |
| Logo lime accent | `#b8d322` |
| Off-white | `#f6f1e8` |
| Charcoal | `#1c2421` |

### الإضاءة والكاميرا

- Soft bright factory lighting.
- Clean high-resolution DSLR look.
- 35mm to 50mm realistic lens.
- Slight depth of field, not blurry.
- Straight technical composition.
- No excessive cinematic mood.

### النبرة

- ثقة هندسية.
- جودة عملية.
- جاهزية إنتاج.
- توريد للموزعين.
- اعتماد للمشاريع.
- قياس وتحكم عبر RFQ / CRM.

## 3. قاعدة مهمة

لا نطلب من AI كتابة نص عربي أو إنجليزي داخل الصورة.

السبب: أغلب مولدات الصور تنتج نصًا غير دقيق. النصوص والعناوين والشعار تضاف لاحقًا داخل الموقع أو التصميم.

ينطبق ذلك على الشعار أيضًا: لا نطلب من AI رسم شعار I-TOP. نستخدم الشعار الحقيقي كطبقة تصميم لاحقة ونطلب من الصورة ترك مساحة نظيفة له.

استخدم دائمًا:

```text
no readable text, no logos, no watermark, leave clean space for later text overlay
```

استخدم عند الحاجة إلى مكان للشعار:

```text
leave a clean empty area in the top corner for placing the official I-TOP logo later
```

## 4. Master Prompt

استخدم هذا كقاعدة لأي صورة خاصة بـ I-TOP:

```text
Premium photorealistic industrial executive visual for a Saudi pipe manufacturing company.
Scene based on a real clean pipe factory: long extrusion production lines, organized warehouse racks, safety workers, PP-R green fittings, UPVC white/grey pipes, HDPE black pipes and coils, packaging materials, technical control screens, clean factory floor.
Visual identity: off-white and deep industrial green palette, muted orange accents, charcoal technical details.
Brand reference: inspired by the official I-TOP logo colors, dark green dominant with warm orange/gold accent and a very small lime green accent.
Mood: professional, practical, trustworthy, boardroom-ready, B2B industrial marketing.
Composition: clean whitespace, balanced framing, high-end presentation quality, realistic lighting, sharp product evidence, no clutter.
No readable text, no logos, no watermark, no fake brands, no exaggerated luxury, no random unrelated machinery.
```

## 5. Negative Prompt

استخدمه مع كل prompt:

```text
No readable text, no logo, no watermark, no fake brand names, no misspelled labels, no generic oil refinery, no construction skyscraper focus, no dirty factory, no unsafe workers, no crowded messy scene, no cartoon style, no illustration, no plastic toy look, no futuristic sci-fi factory, no excessive glow, no unrealistic pipe colors, no random cables, no low-resolution stock photo look.
```

## 5.1 Logo Usage Rules

- الشعار الحقيقي يضاف في التصميم النهائي، وليس داخل prompt توليد الصورة.
- لا تستخدم AI لإعادة رسم الشعار أو كتابة `I-TOP` داخل الصورة.
- عند تصميم hero أو غلاف عرض، اترك مساحة نظيفة للشعار في أعلى اليمين أو أعلى اليسار حسب التخطيط.
- لا تضع الشعار فوق منطقة مزدحمة أو فوق مواسير كثيرة.
- أفضل خلفية للشعار: off-white أو مساحة مصنع هادئة قليلة التفاصيل.
- في الصور الإعلانية، يجب أن يكون الشعار overlay مستقل بجودة أصلية.

## 6. Reference Image Strategy

عند استخدام مولد صور يدعم reference images:

- استخدم 3 إلى 5 صور من مجلد `صور من المصنع`.
- لا تستخدم كل الصور دفعة واحدة.
- اختر صورًا حسب الهدف:

| الهدف | نوع الصور المرجعية |
|---|---|
| Hero / factory | خطوط إنتاج واسعة، فنيين، أرضية المصنع |
| Product marketing | PP-R fittings، UPVC pipes، packaging |
| HDPE / infrastructure | HDPE coils، black pipes، outdoor pipe stacks |
| Distribution | عبوات، مخزون، رفوف، منتجات جاهزة |
| Technical / QA | فنيون على control screens، معدات، اختبار |

مراجع محلية مفيدة من contact sheet:

| الدور | ملفات مقترحة |
|---|---|
| خطوط إنتاج | `صور من المصنع/WhatsApp Image 2026-06-04 at 14.51.34 (1).jpeg`, `صور من المصنع/WhatsApp Image 2026-06-04 at 14.51.36.jpeg` |
| فنيون ومعدات | `صور من المصنع/WhatsApp Image 2026-06-04 at 14.53.13 (1).jpeg`, `صور من المصنع/WhatsApp Image 2026-06-04 at 15.07.12.jpeg` |
| UPVC pipes | `صور من المصنع/WhatsApp Image 2026-06-04 at 14.58.55 (1).jpeg`, `صور من المصنع/WhatsApp Image 2026-06-04 at 14.58.55.jpeg` |
| PP-R fittings / packaging | `صور من المصنع/WhatsApp Image 2026-06-04 at 14.58.55 (2).jpeg`, `صور من المصنع/WhatsApp Image 2026-06-04 at 14.58.55 (3).jpeg` |
| HDPE coils / pipes | `صور من المصنع/WhatsApp Image 2026-06-04 at 15.00.39 (1).jpeg`, `صور من المصنع/WhatsApp Image 2026-06-04 at 15.00.39 (2).jpeg`, `صور من المصنع/WhatsApp Image 2026-06-04 at 15.00.39 (3).jpeg` |

## 7. Image Format Rules

### Website hero

- Ratio: 16:9 or 21:9.
- Must contain factory/product evidence.
- Leave empty area for title overlay if needed.

### Executive card thumbnails

- Ratio: 4:3.
- One clear concept per image.
- No tiny unreadable dashboards.

### LinkedIn posts

- Ratio: 1:1 or 4:5.
- Product or factory proof first.
- Text overlay added later in design, not generated.

### Product visuals

- Ratio: 4:3 or 1:1.
- Product must be recognizable.
- Avoid artistic close-ups that hide the product function.

### Dashboard / CRM visuals

- Ratio: 16:9.
- Use abstract UI panels with charts, not readable labels.
- Keep the B2B factory context in background.

## 8. Prompt Templates

### 8.1 Homepage Hero

```text
Premium photorealistic hero image for I-TOP Therm executive strategy hub.
Scene: clean Saudi pipe manufacturing factory with long extrusion lines, organized UPVC white pipes, PP-R green fittings displayed in foreground, HDPE black coils in background, safety workers operating control screens.
Composition: centered executive presentation image, wide 16:9, clean whitespace, balanced factory depth, strong product evidence.
Palette: off-white factory floor, deep industrial green accents, muted orange safety/pipe accents, charcoal machinery.
Mood: credible, modern, practical, boardroom-ready.
No readable text, no logos, no watermark, no fake brands, no clutter.
```

### 8.2 Distribution Growth

```text
Premium photorealistic B2B distribution growth visual for a Saudi pipe manufacturing company.
Scene: organized warehouse and dealer-ready product area, stacked UPVC pipes, PP-R green fittings kits, packaging boxes, delivery preparation, regional supply readiness.
Include visual cues of trade distribution: palletized products, dealer kit materials without readable text, organized stock, clean logistics flow.
Mood: availability, speed, margin support, professional supply chain.
Palette: off-white, deep green, muted orange, charcoal.
No readable text, no logos, no watermark, no fake brands.
```

### 8.3 Project Acquisition

```text
Premium photorealistic project acquisition visual for a Saudi pipe manufacturing company.
Scene: contractor and MEP engineer reviewing technical pipe samples and approval documents in a clean factory meeting area, production line visible in background, UPVC and HDPE samples on table.
Show trust elements: technical documents, sample pipes, organized folders, factory proof, engineering discussion.
No readable text on documents, no logos, no watermark.
Mood: consultant approval, RFQ, BOQ support, technical reliability.
```

### 8.4 Product Marketing - PP-R

```text
Premium photorealistic product marketing image for PP-R piping systems.
Scene: clean arrangement of green PP-R fittings, elbows, tees, couplers, unions, threaded adaptors and pipe samples on a technical worktable inside a pipe factory.
Background: softly visible production line and worker with safety helmet.
Focus: product detail, clean surfaces, realistic plastic texture, technical credibility.
No readable text, no logos, no watermark.
```

### 8.5 Product Marketing - UPVC

```text
Premium photorealistic product marketing image for UPVC piping systems.
Scene: organized stack of white/grey UPVC pipes with fittings and clean product samples in a Saudi pipe factory warehouse.
Include subtle technical cues: measurement calipers, sample cut sections, clean catalog-like arrangement without readable text.
Mood: drainage, durability, supply readiness, technical clarity.
No readable text, no logos, no watermark.
```

### 8.6 Product Marketing - CPVC Fittings

```text
Premium photorealistic product marketing image for CPVC fittings SCH.80.
Scene: organized technical product display with CPVC elbows, tees, couplings, unions, male adaptors, reducing bushes and end caps on a clean workbench.
Include small blank tags or datasheet shapes with no readable text, factory background, controlled lighting.
Mood: precision, part numbers, pack readiness, technical specification.
No readable text, no logos, no watermark.
```

### 8.7 Product Marketing - HDPE

```text
Premium photorealistic product marketing image for HDPE pipe systems.
Scene: black HDPE pipe coils and straight pipe sections in a clean outdoor/warehouse factory area, organized for infrastructure supply, subtle orange accent coil in background.
Mood: strength, infrastructure, irrigation, drainage, durability.
Composition: wide, clean, realistic, executive-grade.
No readable text, no logos, no watermark.
```

### 8.8 RFQ Dashboard

```text
Premium photorealistic executive visual of an RFQ and BOQ workflow for a Saudi pipe manufacturing company.
Scene: clean desktop screen showing abstract dashboard cards, upload area, pipeline stages and charts, with pipe samples and factory background.
The UI must have no readable text, only abstract shapes and realistic dashboard structure.
Mood: measurable sales process, technical inquiry, fast response.
Palette: off-white, deep green, muted orange, charcoal.
No logos, no watermark, no readable text.
```

### 8.9 CRM KPI Dashboard

```text
Premium photorealistic CRM KPI dashboard visual for B2B industrial marketing.
Scene: boardroom screen with abstract CRM pipeline, RFQ count, BOQ count, conversion chart, lead source panels, factory and pipe samples visible subtly.
No readable text, only clean UI blocks and chart shapes.
Mood: executive control, measurable marketing, sales alignment.
Palette: off-white, deep green, muted orange, charcoal.
No logos, no watermark.
```

### 8.10 LinkedIn B2B Content

```text
Premium photorealistic LinkedIn B2B content planning visual for a Saudi pipe manufacturing company.
Scene: marketing desk with factory photos, pipe samples, technical sheets without readable text, laptop showing abstract social content grid, factory production line visible through glass.
Mood: industrial content system, engineering confidence, professional communication.
No readable text, no logos, no watermark.
```

### 8.11 Technical Library

```text
Premium photorealistic technical library visual for pipe manufacturing.
Scene: organized digital and physical technical library with blank catalog covers, pipe samples, certification folders, product datasheets without readable text, clean engineering table.
Mood: approvals, specifications, documentation, consultant-ready.
Palette: off-white, deep green, muted orange, charcoal.
No readable text, no logos, no watermark.
```

### 8.12 Marketing Department

```text
Premium photorealistic executive visual for a lean marketing department in a Saudi industrial manufacturing company.
Scene: small professional team reviewing factory visuals, product samples, CRM dashboard shapes and content calendar on a boardroom table.
Background: clean factory context, pipe products, technical folders.
Mood: leadership, execution, weekly reporting, alignment with sales.
No readable text, no logos, no watermark.
```

## 9. Page-by-Page Visual Direction

| الصفحة | الصورة المناسبة |
|---|---|
| 01 Executive Case | مصنع حقيقي مع dashboard تنفيذي خفيف يوضح الفجوة بين الإنتاج والقياس |
| 02 Dual Market Model | مساران بصريان: مخزون/موزعين مقابل وثائق/مشاريع |
| 03 Digital Infrastructure | شاشة موقع/RFQ بجانب عينات مواسير |
| 04 SEO Growth Engine | بحث Google بشكل abstract مرتبط بصفحات منتجات |
| 05 Keyword Strategy | خريطة clusters مع عينات PP-R/UPVC/HDPE |
| 06 Social & LinkedIn | مكتب محتوى مع صور مصنع ومنتجات |
| 07 Paid Lead Generation | funnel بسيط من search إلى RFQ |
| 08 Brand Positioning | صورة مصنع ومنتجات تعكس ثقة بدون مبالغة |
| 09 Product Marketing | Product display واضح حسب خط المنتج |
| 10 Content & Media System | تصوير خطوط إنتاج وفنيين ومنتجات |
| 11 Retail Distribution | مخزون، packaging، dealer-ready kits |
| 12 Projects Acquisition | مهندس/استشاري مع وثائق واعتمادات وعينات |
| 13 CRM & KPI Dashboard | لوحة CRM مجردة بدون نص مقروء |
| 14 Department Roadmap | فريق صغير، جدول، منتجات، dashboard |
| 15 Executive Recommendation | boardroom approval مع مصنع ومنتجات في الخلفية |

## 10. Quality Checklist

قبل اعتماد أي صورة:

- هل تبدو من عالم تصنيع المواسير فعلًا؟
- هل يظهر منتج واحد واضح على الأقل؟
- هل الألوان قريبة من I-TOP: أخضر، أبيض، رمادي، أسود، برتقالي خفيف؟
- هل الصورة مناسبة لعرض إدارة؟
- هل لا يوجد نص مشوه أو شعار مزيف؟
- هل لا تبدو كصورة stock عامة؟
- هل يمكن استخدامها للموقع أو LinkedIn بدون تفسير طويل؟
- هل تخدم أحد المسارين: Distribution Growth أو Project Acquisition؟

## 11. Production Workflow

1. اختر الهدف: موقع، صفحة منتج، LinkedIn، إعلان، RFQ، CRM.
2. اختر 3 صور مرجعية من مجلد المصنع حسب الهدف.
3. استخدم Master Prompt + template مناسب.
4. أضف Negative Prompt.
5. ولد 2 إلى 4 نسخ.
6. اختر النسخة الأقرب للمصنع الحقيقي.
7. أضف النصوص والشعار لاحقًا في التصميم، لا داخل AI image.
8. احفظ الصورة باسم واضح:

```text
itop-hero-factory-v01.jpg
itop-ppr-product-display-v01.jpg
itop-rfq-dashboard-v01.jpg
itop-distribution-growth-v01.jpg
itop-project-acquisition-v01.jpg
```

## 12. Approved Core Message For Visuals

الصور يجب أن تخدم هذه الفكرة:

```text
I-TOP is a real Saudi pipe manufacturing company with products, production capacity, technical documents, distribution potential, and project readiness.
The visual system must convert factory proof into trust for projects and profitability for distributors.
```
