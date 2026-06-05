# I-TOP Growth & Marketing Transformation Hub

مركز تحول النمو والتسويق لشركة I-TOP Therm، مبني كعرض تنفيذي تفاعلي ثابت وجاهز للنشر على GitHub Pages أو Vercel.

## التشغيل محليًا

افتح `index.html` مباشرة في المتصفح.

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
  assets/
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
