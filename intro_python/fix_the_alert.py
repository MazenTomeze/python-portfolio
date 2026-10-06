# fix_the_alert.py
# This program prints a short login alert.
print("=== LOGIN ALERT ===")
# Syntax Error (مسافة غير متوقعه)
print("A new device signed in to your account.")
# Runtime Error (Print مش معرفه في لغه بايثون)
print("Time: 09:15")
# Syntax Error (نص غير مغلق)
print("If this was not you, change your password.")

# Syntax Error (عدم وجود قوس اغلاق)
print("Contact the IT team for help.")
#   أي أخطاء تظهرها بايثون أولاً، ولماذا؟
#  Syntax أول إشي.
# السبب إنه بايثون بتفحص القواعد وتنسيق الكود كامل قبل ما تبدأ تشغله
# وإذا لقت أي خطأ قواعدي بتوقف فوراً وما بتنفذ الكود
#  الخطا بكلمة Print
#  هو خطا  لأنه بايثون ما بتعرف هاي الكلمةوبتظهرلك بس وقت تشغيل السطر نفسه.
# لأنه بايثون ما بتكتشفه إلا وقت تشغيل السطر نفسه فعلياً.