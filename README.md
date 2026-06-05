# I-TOP Growth & Marketing Transformation Hub

مركز تحول النمو والتسويق لشركة I-TOP Therm، مبني كعرض تنفيذي تفاعلي ثابت وجاهز للنشر على GitHub Pages أو Vercel.

## التشغيل محليًا

افتح `index.html` مباشرة في المتصفح.

## نظام الصور بالذكاء الاصطناعي

تمت إضافة ملف `ITOP_AI_VISUAL_SYSTEM.md` كدليل تشغيل لتوليد صور AI متوافقة مع صور المصنع، الكتالوجات، والشعار الرسمي.

الشعار الأصلي محفوظ داخل `assets/logo-itop-original.png` ويستخدم في الهيدر والهيرو الرئيسي.

كما يحتوي `assets/image-prompts.json` على مكتبة prompts عملية قابلة للاستخدام للـ hero، المنتجات، RFQ، CRM، LinkedIn، التوزيع، والمشاريع.

اختياريًا يمكن تشغيل خادم محلي:

```bash
python3 -m http.server 8080
```

ثم افتح:

```
http://localhost:8080
```

## النشر على GitHub Pages

1. ارفع الملفات إلى مستودع GitHub.
2. من إعدادات المستودع اختر Pages.
3. اختر الفرع الرئيسي والمجلد الجذر.
4. احفظ الإعدادات وانتظر رابط GitHub Pages.

## النشر على Vercel

1. اربط المستودع مع Vercel.
2. اختر المشروع كـ Static Site.
3. لا تحتاج build command.
4. اجعل output directory هو الجذر أو اتركه فارغًا.

## Folder Structure

```
/
  index.html
  styles.css
  script.js
  README.md
  ITOP_AI_VISUAL_SYSTEM.md
  assets/
    logo-itop-original.png
    image-prompts.json
    svg/
      hero-itop-factory.svg
      01-executive-case.svg
      ...
      15-executive-recommendation.svg
  pages/
    01-executive-case.html
    ...
    15-executive-recommendation.html
```
