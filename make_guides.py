#!/usr/bin/env python3
"""Builds the SEO guide pages: guides/<slug>.html"""
import html, json, re
from pathlib import Path

BASE = "https://alaabashirsaijary.github.io/ayadati-site/"
WA = "https://wa.me/963984668063?text=" + "%D9%85%D8%B1%D8%AD%D8%A8%D9%8B%D8%A7%D8%8C%20%D8%A3%D8%B1%D9%8A%D8%AF%20%D8%B9%D8%B1%D8%B6%D9%8B%D8%A7%20%D9%85%D8%A8%D8%A7%D8%B4%D8%B1%D9%8B%D8%A7%20%D9%84%D8%AA%D8%B7%D8%A8%D9%8A%D9%82%20%D8%B9%D9%8A%D8%A7%D8%AF%D8%AA%D9%8A."
STYLE = re.search(r"<style>(.*?)</style>", Path("features.html").read_text(encoding="utf-8"), re.S).group(1)
EXTRA = """
  .crumbs{font-size:13px;color:var(--ink-faint);margin-bottom:18px}.crumbs a{color:var(--teal-deep);text-decoration:none}
  article{max-width:760px;margin-inline:auto}
  article h1{font-size:clamp(30px,4.6vw,46px);margin:0 0 14px}
  article h2{font-size:27px;margin:38px 0 10px}
  article h3{font-size:20px;margin:24px 0 8px}
  article p{font-size:17px;color:var(--ink-soft);margin:0 0 14px}
  article ul,article ol{padding-inline-start:22px;margin:0 0 16px;color:var(--ink-soft);font-size:17px}
  article li{margin-bottom:8px}
  .lead{font-size:19px;color:var(--ink)}
  .callout{background:var(--teal-wash);border:1px solid color-mix(in srgb,var(--teal) 30%,transparent);border-radius:16px;padding:18px 22px;margin:22px 0}
  .callout p{margin:0;font-size:15.5px}
  .cta{background:var(--paper-raised);border:1px solid var(--line);border-radius:20px;padding:26px;margin:40px 0;text-align:center;box-shadow:var(--shadow)}
  .cta h2{margin:0 0 6px;font-size:26px}.cta p{margin:0 0 16px}
  .btn{display:inline-block;font-weight:700;font-size:15px;padding:13px 26px;border-radius:999px;text-decoration:none;margin:4px}
  .btn.p{background:var(--teal);color:#fff}.btn.w{background:#1FA855;color:#fff}
  .faq details{background:var(--paper-raised);border:1px solid var(--line);border-radius:14px;margin-bottom:10px;padding:0 18px}
  .faq summary{cursor:pointer;font-weight:600;padding:14px 0;color:var(--ink)}
  .faq details p{margin:0 0 14px;font-size:15.5px}
  .related{display:grid;gap:10px;margin-top:10px}.related a{display:block;background:var(--paper-raised);border:1px solid var(--line);border-radius:14px;padding:14px 18px;color:var(--teal-deep);font-weight:600;text-decoration:none}
  table{width:100%;border-collapse:collapse;margin:0 0 18px;font-size:15px}th,td{border:1px solid var(--line);padding:10px 12px;text-align:start;color:var(--ink-soft)}th{background:var(--teal-wash);color:var(--ink)}
  .tbl{overflow-x:auto}
"""

PAGES = [
 dict(
  slug="offline-clinic-software",
  title="برنامج إدارة عيادة بدون إنترنت: ما الذي تحتاجه عيادتك فعلًا؟",
  short="برنامج إدارة عيادة بدون إنترنت",
  desc="دليل عملي لاختيار برنامج إدارة عيادة يعمل بدون إنترنت: ماذا يعني ذلك فعليًا، وما الذي يجب أن يوفره، وأسئلة تسألها قبل أن تشتري.",
  body="""
<p class="lead">الإنترنت غير المستقر مشكلة يومية في كثير من العيادات. وإذا كان برنامج عيادتك يتوقف عندما تنقطع الشبكة، فأنت تدفع ثمن الانقطاع من وقت مرضاك. هذا الدليل يساعدك على اختيار برنامج إدارة عيادة يعمل بدون إنترنت، وعلى معرفة ما الذي تحتاجه عيادتك منه فعلًا.</p>

<h2>ماذا يعني "بدون إنترنت" فعليًا؟</h2>
<p>كلمة "بدون إنترنت" تُستعمل بمعانٍ مختلفة، فانتبه للفرق:</p>
<ul>
<li><b>برنامج محلي بالكامل:</b> البيانات تُحفظ على جهازك، ويعمل كل شيء دون أي اتصال، ولا يعتمد على خادم عند أحد.</li>
<li><b>برنامج سحابي يتحمّل انقطاعًا قصيرًا:</b> يحفظ مؤقتًا ثم يزامن لاحقًا. يعمل أحيانًا، لكن بياناتك على خادم الشركة.</li>
</ul>
<p>"عيادتي" من النوع الأول: بيانات المرضى على جهاز الطبيب نفسه. الاستثناءات القليلة اختيارية: المساعد الذكي، وفحص التحديثات، وروابط الحجز عبر واتساب (تحتاج واتساب نفسه). عدا ذلك، يعمل التطبيق كله بلا اتصال.</p>

<h2>ما الذي يجب أن يوفره برنامج العيادة؟</h2>
<div class="tbl"><table>
<tr><th>الحاجة</th><th>لماذا تهم؟</th></tr>
<tr><td>ملف مريض كامل</td><td>بيانات المريض وزياراته وفحوصاته في مكان واحد بدل الإضبارات الورقية.</td></tr>
<tr><td>مواعيد</td><td>جدول واضح لكل يوم مع حالة كل موعد (مجدول، تمت الزيارة، ملغى).</td></tr>
<tr><td>وصفات وتقارير</td><td>طباعة أو مشاركة وصفة أو إجازة مرضية أو تقرير دون إعادة كتابة.</td></tr>
<tr><td>حسابات الكشفيات</td><td>معرفة ما دُفع وما بقي، وبالعملة التي تتعامل بها العيادة.</td></tr>
<tr><td>نسخ احتياطي</td><td>حماية بياناتك من ضياع الجهاز أو تلفه، وإمكانية الاستعادة.</td></tr>
<tr><td>حماية الخصوصية</td><td>رمز قفل للتطبيق، وبيانات لا تُرسل إلى أي خادم.</td></tr>
<tr><td>واجهة عربية كاملة</td><td>من اليمين لليسار وبمصطلحات تعرفها، لا ترجمة غريبة.</td></tr>
</table></div>

<h2>أسئلة اسألها قبل أن تشتري أي برنامج</h2>
<ol>
<li><b>على أي جهاز يعمل؟</b> إن كان يحتاج كمبيوتر وخادمًا وفنيًا، فاحسب كلفة ذلك أيضًا.</li>
<li><b>من يملك بياناتي؟</b> وأين تُحفظ؟ وهل أستطيع تصديرها إن غيّرت البرنامج؟</li>
<li><b>هل هناك اشتراك شهري؟</b> وماذا يحدث لبياناتي إن توقفت عن الدفع؟</li>
<li><b>هل أستطيع التجربة قبل الدفع؟</b> التجربة على عيادتك الحقيقية أهم من أي عرض.</li>
<li><b>ماذا لو احتجت سكرتيرة أو ممرضة؟</b> وهل أستطيع تحديد ما تفعله؟</li>
<li><b>هل يتعامل مع ما أحتاجه محليًا؟</b> مثل الحجز عبر واتساب والكشفية بأكثر من عملة.</li>
</ol>

<div class="callout"><p>نصيحة: جرّب أي برنامج ليوم عمل كامل في عيادتك قبل أن تقرر. سرعة تسجيل مريض جديد وفتح ملفه أثناء الكشف تكشف الكثير.</p></div>

<h2>كيف تعالج عيادتي هذه الاحتياجات؟</h2>
<ul>
<li>يعمل على <b>الآيباد وأجهزة أندرويد</b> بدون تنصيب على كمبيوتر أو خادم.</li>
<li>البيانات <b>على جهازك وحدك</b>، مع نسخ احتياطية قابلة للاستعادة وقفل برمز PIN.</li>
<li><b>نموذج فحص</b> يُجهَّز لاختصاصك تلقائيًا ويمكنك تعديله.</li>
<li><b>كشفية بالليرة والدولار</b> مع تسجيل الدفعات الجزئية وقائمة بالمبالغ المتبقية.</li>
<li><b>حجز عبر واتساب</b> برابط وQR، وربط جهاز سكرتيرة أو ممرضة بالواي فاي المحلي بصلاحيات تحددها.</li>
<li><b>تجربة 14 يومًا مجانًا</b>، ثم دفعة واحدة بلا اشتراك شهري أو سنوي.</li>
</ul>
<p>ولا نقول إنه يناسب كل جهة: إن كنت مركزًا طبيًا كبيرًا يحتاج مختبرًا وأشعة وصيدلية ومحاسبة متقدمة، فهذه الميزات ليست متوفرة في عيادتي الآن، وهو مصمم للطبيب المنفرد والعيادة الصغيرة.</p>
""",
  faq=[
   ("هل يعمل تطبيق عيادتي فعلًا بدون أي اتصال بالإنترنت؟","نعم، الاستخدام اليومي (المرضى والمواعيد والوصفات والتقارير والحسابات) يعمل بلا اتصال. الإنترنت مطلوب فقط لميزات اختيارية مثل المساعد الذكي وفحص التحديثات."),
   ("أين تُحفظ بيانات المرضى؟","على جهازك أنت، ولا تُرسل إلى خادم خارجي. ويمكنك إنشاء نسخ احتياطية واستعادتها."),
   ("هل أحتاج إلى كمبيوتر أو خادم؟","لا. يكفي آيباد أو جهاز أندرويد."),
   ("كم تكلفة البرنامج وهل هناك اشتراك؟","لا اشتراك شهري أو سنوي. تدفع مرة واحدة، ويُتفق على السعر بعد عرض مباشر. وهناك تجربة مجانية 14 يومًا."),
  ],
  related=["whatsapp-booking","exam-form-templates"],
 ),
 dict(
  slug="whatsapp-booking",
  title="كيف تجعل مرضاك يحجزون عبر واتساب؟ رابط حجز وQR لعيادتك",
  short="الحجز عبر واتساب للعيادات",
  desc="شرح خطوة بخطوة لإعداد حجز المرضى عبر واتساب برابط وQR، وكيف تتحول رسالة المريض إلى موعد في برنامج عيادتك بضغطة واحدة.",
  body="""
<p class="lead">أغلب المرضى في سوريا يتواصلون مع الطبيب عبر واتساب. وهذا يعني رسائل كثيرة: "متى عندك دوام؟"، "بدي موعد بكرا"، "الساعة ٥ فاضي؟". الحل ليس منع الرسائل، بل تنظيمها: أعطِ مريضك رابطًا يختار منه اليوم والوقت من أوقات دوامك، فتصلك رسالة واضحة جاهزة للتحويل إلى موعد.</p>

<h2>كيف تعمل فكرة الحجز عبر واتساب؟</h2>
<ol>
<li>تُنشئ <b>رابط حجز</b> لعيادتك يحمل رقم واتساب وأيام وساعات دوامك.</li>
<li>يفتح المريض الرابط من هاتفه، ولا يحتاج تطبيقًا ولا حسابًا.</li>
<li>يختار <b>اليوم والوقت</b> من الأوقات المتاحة فقط، ويكتب اسمه ورقمه وسبب الزيارة.</li>
<li>يضغط إرسال، فيفتح واتساب برسالة <b>منظّمة</b> إلى رقم العيادة.</li>
<li>تنسخ الرسالة في التطبيق فتتعبأ بيانات الموعد، وتحفظه بضغطة.</li>
</ol>

<h2>إعداد الرابط في عيادتي</h2>
<ol>
<li>من الإدارة اختر <b>"رابط الحجز عبر واتساب"</b>.</li>
<li>أدخل رقم واتساب العيادة.</li>
<li>حدّد أيام الدوام وساعاته.</li>
<li>يظهر لك الرابط ورمز <b>QR</b> جاهزان للنسخ والمشاركة أو للطباعة.</li>
</ol>

<h2>من الرسالة إلى الموعد</h2>
<p>الرسالة التي تصلك مكتوبة بصيغة ثابتة (الاسم، الهاتف، اليوم، الوقت، السبب)، ولذلك يقرؤها التطبيق مباشرة. استخدم <b>"حجز من رسالة واتساب"</b> في صفحة المواعيد: الصق الرسالة فتُستخرج البيانات وتُفتح شاشة الحجز معبّأة، وتبقى كل خانة قابلة للتعديل قبل الحفظ. ويفهم التطبيق أيضًا الرسائل الحرة بلهجات شائعة مثل "بكرا الساعة ٥".</p>

<div class="callout"><p>الطلب ليس موعدًا مؤكدًا حتى تحفظه أنت. صفحة الحجز لا ترى المواعيد المحجوزة، فقد يطلب مريض وقتًا مأخوذًا. وهنا ترد بتأكيد أو بوقت بديل.</p></div>

<h2>رسائل جاهزة للتأكيد والتذكير</h2>
<p>على كل موعد أيقونة واتساب بثلاث رسائل جاهزة: <b>تأكيد الموعد</b>، و<b>تذكير بالموعد</b>، و<b>طلب تغيير الموعد</b>. كما توجد قائمة <b>"تذكيرات الغد"</b> بمرضى اليوم التالي، وزر تذكير لكل مريض. واتساب لا يسمح بالإرسال التلقائي، فتضغط إرسال في كل محادثة، وهذا يبقي الرسالة منك ويحمي رقمك من الحظر.</p>

<h2>نصائح لتزيد عدد الحاجزين</h2>
<ul>
<li>ضع <b>رمز QR</b> مطبوعًا على باب العيادة وفي الاستقبال.</li>
<li>أضف الرابط في صفحة فيسبوك وإنستغرام وفي حالة واتساب.</li>
<li>اجعل ساعات الدوام في الرابط دقيقة، فالمريض لن يرى غيرها.</li>
<li>ردّ على الطلبات في نفس اليوم، فالرد السريع يرفع نسبة الحضور.</li>
</ul>
""",
  faq=[
   ("هل يحتاج المريض إلى تحميل تطبيق؟","لا. يفتح الرابط من متصفح هاتفه ويُرسل الطلب عبر واتساب."),
   ("هل تُرسل الرسائل تلقائيًا؟","لا. واتساب لا يسمح للتطبيقات بالإرسال بالنيابة عنك، فتضغط إرسال بنفسك في كل محادثة."),
   ("هل يعمل رابط الحجز بدون إنترنت؟","المريض يحتاج إنترنت ليفتح الصفحة ويرسل رسالة واتساب. أما التطبيق عندك فيعمل بلا إنترنت في معظم مهامه."),
   ("ماذا لو حجز مريضان نفس الوقت؟","التطبيق ينبّهك عند وجود موعد آخر في نفس الوقت قبل الحفظ، وتقرر أنت."),
  ],
  related=["offline-clinic-software","exam-form-templates"],
 ),
 dict(
  slug="exam-form-templates",
  title="نموذج فحص جاهز لعيادتك: عيون، أسنان، أطفال، نسائية وغيرها",
  short="نموذج فحص جاهز لكل اختصاص",
  desc="كيف يجهّز تطبيق عيادتي نموذج الفحص لاختصاصك تلقائيًا، وأمثلة على حقول عيادات العيون والأسنان والأطفال والنسائية، وكيف تعدّله ليناسب طريقتك.",
  body="""
<p class="lead">لكل اختصاص طريقته في تسجيل الفحص: عيادة العيون تسجّل قياسات لكل عين، وعيادة الأطفال تسجّل الوزن والطول، وعيادة الأسنان تسجّل السن المصاب والإجراء. برنامج يفرض نموذجًا واحدًا على الجميع يتعبك. لهذا يجهّز "عيادتي" نموذج الفحص لاختصاصك عند البدء، ثم تعدّله كما تشاء.</p>

<h2>كيف يعمل نموذج الفحص؟</h2>
<ul>
<li>عند إنشاء حسابك تختار <b>اختصاصك</b> فيُجهَّز النموذج بحقول مناسبة.</li>
<li>كل حقل يمكن أن يكون <b>قيمة واحدة</b> أو <b>له جانبان (يمين/يسار)</b> مثل العينين والأذنين والمفاصل.</li>
<li>الحقل قد يكون <b>نصًا طويلًا</b> لوصف الفحص السريري.</li>
<li>تضيف حقولًا وتحذفها وتعيد <b>ترتيبها</b> بالسحب، وتغيّر الاختصاص لاحقًا من "قوالب الاختصاصات".</li>
</ul>
<p>عند تطبيق قالب جاهز على نموذج موجود تستطيع <b>إضافة الحقول الناقصة فقط</b> دون تكرار، أو استبدال النموذج بالكامل (انتبه: الاستبدال يحذف القيم المسجلة سابقًا في الحقول القديمة).</p>

<h2>الاختصاصات المتوفرة</h2>
<p>طب العيون، طب الأسنان، طب الأطفال، النسائية والتوليد، الباطنية والطب العام، أمراض القلب، أنف وأذن وحنجرة، الجلدية، العظمية، الأعصاب، الجراحة العامة، إضافة إلى نموذج عام لأي اختصاص آخر.</p>

<h2>أمثلة على الحقول</h2>
<h3>عيادة العيون</h3>
<p>Auto، Cycl/Myder، Old Glass، Pers.Refract، Near، IOP، Anter.S، Lens، Poster.S، وكلها بجانبين (يمين/يسار).</p>
<h3>عيادة الأسنان</h3>
<p>السن المصاب، التشخيص السني، حالة اللثة، التسوس، الأشعة السنية، الإجراء المنفّذ، نوع التخدير، خطة العلاج.</p>
<h3>عيادة الأطفال</h3>
<p>الوزن، الطول، محيط الرأس، الحرارة، النبض، معدل التنفس، فحص الأذنين والحلق والصدر والبطن، النمو والتطور، التلقيحات، التغذية.</p>
<h3>النسائية والتوليد</h3>
<p>ضغط الدم، الوزن، تاريخ آخر دورة (LMP)، تاريخ الولادة المتوقع (EDD)، عمر الحمل، نبض الجنين، ارتفاع قاع الرحم، السونار، الفحص النسائي.</p>

<div class="callout"><p>هذه الحقول مقترحات عامة تساعدك على البدء، وليست بروتوكولًا طبيًا. راجعها وعدّلها لتناسب ممارستك.</p></div>

<h2>ما بعد الفحص</h2>
<p>إلى جانب حقول الفحص، تسجّل في كل زيارة <b>خلاصة الفحص</b> و<b>نتيجة المتابعة</b> و<b>الكشفية</b>، مع أزرار عبارات سريعة تتعلّم من استخدامك، وإملاء صوتي بالعربية في الحقول النصية. وتبقى زيارات المريض مرقّمة (معاينة أو مراجعة) في ملفه.</p>
""",
  faq=[
   ("هل أستطيع تعديل الحقول بعد اختيار الاختصاص؟","نعم، تضيف وتحذف وتعيد ترتيب أي حقل من صفحة نموذج الفحص."),
   ("ماذا لو اختصاصي غير مذكور؟","اختر النموذج العام ثم أضف الحقول التي تحتاجها."),
   ("هل تتغير بيانات الزيارات القديمة عند تغيير النموذج؟","إضافة حقول جديدة لا تمس القديمة. حذف حقل أو استبدال النموذج يحذف قيمه المسجلة في الزيارات السابقة، وهناك تحذير قبل التنفيذ."),
   ("هل يمكن إدخال قياس لكل عين على حدة؟","نعم، الحقول ذات الجانبين تسجّل اليمين واليسار بشكل منفصل."),
  ],
  related=["offline-clinic-software","whatsapp-booking"],
 ),
]
TITLES = {p["slug"]: p["short"] for p in PAGES}

def page(p):
    url = f"{BASE}guides/{p['slug']}.html"
    faq_html = "".join(f"<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>" for q, a in p["faq"])
    related = "".join(f'<a href="{s}.html">{html.escape(TITLES[s])}</a>' for s in p["related"])
    ld = [
      {"@context":"https://schema.org","@type":"Article","headline":p["title"],"description":p["desc"],"inLanguage":"ar",
       "datePublished":"2026-10-26","dateModified":"2026-10-26","mainEntityOfPage":url,
       "author":{"@type":"Organization","name":"عيادتي","url":BASE},"publisher":{"@type":"Organization","name":"عيادتي","url":BASE,"logo":{"@type":"ImageObject","url":BASE+"assets/logo-96.png"}},
       "image":BASE+"assets/og-image.png"},
      {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"عيادتي","item":BASE},
        {"@type":"ListItem","position":2,"name":"أدلة للأطباء","item":BASE+"guides/"},
        {"@type":"ListItem","position":3,"name":p["short"],"item":url}]},
      {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in p["faq"]]},
    ]
    return f"""<!doctype html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<title>{html.escape(p['title'])} | عيادتي</title>
<meta name="description" content="{html.escape(p['desc'])}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{url}">
<link rel="icon" href="../assets/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="../assets/apple-touch-icon.png">
<meta property="og:type" content="article"><meta property="og:locale" content="ar_SY">
<meta property="og:title" content="{html.escape(p['title'])}"><meta property="og:description" content="{html.escape(p['desc'])}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{BASE}assets/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Markazi+Text:wght@500;600;700&family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&display=swap">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>{STYLE}{EXTRA}</style>
</head>
<body>
<div class="wrap">
<nav class="crumbs" aria-label="مسار التنقل"><a href="../">عيادتي</a> › <a href="../features.html">المزايا</a> › {html.escape(p['short'])}</nav>
<article>
<h1>{html.escape(p['title'])}</h1>
{p['body']}
<div class="cta">
<h2>جرّب عيادتي مجانًا ١٤ يومًا</h2>
<p>عرض مباشر لمدة ١٠ دقائق على جهازك، ثم تجربة كاملة المزايا.</p>
<a class="btn w" href="{WA}" rel="noopener">راسلنا على واتساب</a>
<a class="btn p" href="../">اعرف المزيد عن التطبيق</a>
</div>
<h2>أسئلة شائعة</h2>
<div class="faq">{faq_html}</div>
<h2>اقرأ أيضًا</h2>
<div class="related">{related}<a href="../features.html">كل ميزات عيادتي</a></div>
</article>
</div>
<footer class="wrap">عيادتي (Ayadati) · برنامج إدارة عيادة بدون إنترنت للآيباد وأندرويد.</footer>
</body>
</html>
"""

for p in PAGES:
    Path("guides", f"{p['slug']}.html").write_text(page(p), encoding="utf-8")
    print("built", p["slug"])

# --- guides index (the breadcrumb target) ---
cards = "".join(
  f'<a href="{p["slug"]}.html"><b>{html.escape(p["title"])}</b><span>{html.escape(p["desc"])}</span></a>' for p in PAGES)
idx = page(dict(slug="", title="أدلة لأطباء العيادات", short="أدلة للأطباء",
  desc="أدلة عملية قصيرة لأطباء العيادات: برنامج بدون إنترنت، الحجز عبر واتساب، ونماذج الفحص الجاهزة.",
  body='<p class="lead">أدلة عملية قصيرة لأطباء العيادات الصغيرة، من فريق تطبيق عيادتي.</p><div class="related" style="margin-top:18px">' + cards + '</div>',
  faq=[("ما هو تطبيق عيادتي؟","تطبيق عربي لإدارة العيادة يعمل بدون إنترنت على الآيباد وأندرويد: ملف المريض والمواعيد والوصفات والحسابات والحجز عبر واتساب.")],
  related=[]))
idx = idx.replace(f'{BASE}guides/.html', f'{BASE}guides/').replace('<a href="../features.html">كل ميزات عيادتي</a>','<a href="../features.html">كل ميزات عيادتي</a>')
idx = re.sub(r'<h2>اقرأ أيضًا</h2>.*?</div>\s*</article>', '</article>', idx, flags=re.S)
Path("guides", "index.html").write_text(idx, encoding="utf-8")
print("built index")
