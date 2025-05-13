# استيراد المكتبات اللازمة
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

# قراءة البيانات من ملف CSV
data = pd.read_csv("ds_salaries.csv")

# طباعة عدد القيم الفارغة في كل عمود
print(data.isnull().sum())

# عرض أول 10 صفوف من البيانات
print(data.head(10))

# عرض الإحصائيات الوصفية للأعمدة الرقمية
print(data.describe())

# حساب وطباعة الوسيط للرواتب بالدولار الأمريكي
print(f"the median for the salaries is {data['salary_in_usd'].median()}")

# حساب وطباعة المتوسط الحسابي للرواتب بالدولار الأمريكي
print(f"the mean for the salaries is {data['salary_in_usd'].mean()}")

# حساب وطباعة الانحراف المعياري للرواتب بالدولار الأمريكي
print(f"the std for the salaries is {data['salary_in_usd'].std()}")

# حساب متوسط الرواتب لكل مسمى وظيفي
x = data.groupby("job_title")["salary_in_usd"].mean()

# ترتيب المتوسطات تنازلياً
x = x.sort_values(ascending=False)

# رسم شريطي لأعلى 10 مسميات وظيفية من حيث متوسط الرواتب
plt.bar(x[:10].index, x[:10])
plt.title("salaries depending on job_title")
plt.xlabel("job_title")
plt.ylabel("salary_in_usd")
plt.show()

# حساب متوسط الرواتب لكل دولة يقيم فيها الموظفون وترتيبها تنازلياً
y = data.groupby("employee_residence")["salary_in_usd"].mean().sort_values(ascending=False)

# رسم شريطي أفقي لأعلى 10 دول من حيث متوسط الرواتب
plt.barh(y[:10].index, y[:10])
plt.title("salaries depending on the country")
plt.xlabel("the country")
plt.ylabel("salary_in_usd")
plt.show()

# عرض عدد الموظفين في كل مستوى من مستويات الخبرة
print(data["experience_level"].value_counts())

# حساب متوسط الرواتب لكل مستوى من مستويات الخبرة
b = data.groupby("experience_level")["salary_in_usd"].mean()

# رسم شريطي لمتوسط الرواتب حسب مستوى الخبرة
plt.bar(b.index,b)
plt.title("the mean of the salaries depending on the level of the experience")
plt.xlabel("the experience level")
plt.ylabel("the mean of the salary_in_usd")
plt.show()

# عرض عدد الموظفين حسب نسبة العمل عن بعد
print(data["remote_ratio"].value_counts())

# حساب متوسط الرواتب لكل نسبة من نسب العمل عن بعد
n = data.groupby("remote_ratio")["salary_in_usd"].mean()

# طباعة المتوسطات بعد تقريبها
print(round(n))

# رسم شريطي لمتوسط الرواتب حسب نسبة العمل عن بعد
plt.bar(n.index,n,color=["red","orange","green"])
plt.title("the mean of the salary depending on the kind of your work")
plt.xlabel("remote_ratio")
plt.ylabel("salary_in_usd")

# حفظ الرسم كصورة
plt.savefig("project matplotlib.png")
plt.show()

# عرض عدد الشركات حسب موقعها
print(data["company_location"].value_counts())

# عرض عدد الشركات حسب حجمها
print(data["company_size"].value_counts())

# حساب متوسط الرواتب حسب حجم الشركة (ملاحظة: هنا يستخدم عمود salary وليس salary_in_usd)
l = data.groupby("company_size")["salary_in_usd"].mean()
print(l)
