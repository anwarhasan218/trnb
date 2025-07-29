from django.db import models

# نموذج المعلم
class Teacher(models.Model):
    name = models.CharField(max_length=255, verbose_name="اسم المعلم")
    national_id = models.CharField(max_length=20, unique=True, verbose_name="الرقم القومي")
    record_number = models.CharField(max_length=20, unique=True, verbose_name="رقم السجل")
    subject = models.CharField(max_length=100, verbose_name="المادة")
    stage = models.CharField(max_length=50, verbose_name="المرحلة التعليمية")
    region = models.CharField(max_length=100, verbose_name="المنطقة", null=True, blank=True)
    administration = models.CharField(max_length=100, verbose_name="الإدارة", null=True, blank=True)
    institute = models.CharField(max_length=100, verbose_name="المعهد", null=True, blank=True)
    job_grade = models.CharField(max_length=100, verbose_name="الدرجة الوظيفية", null=True, blank=True)
    # يمكن إضافة حقول إضافية لاحقاً

    def __str__(self):
        return self.name

# نموذج البرنامج التدريبي
class TrainingProgram(models.Model):
    name = models.CharField(max_length=255, verbose_name="اسم البرنامج التدريبي")
    target_group = models.CharField(max_length=100, verbose_name="الفئة المستهدفة")
    stage = models.CharField(max_length=50, verbose_name="المرحلة التعليمية")
    start_date = models.DateField(verbose_name="تاريخ بداية التدريب")
    end_date = models.DateField(verbose_name="تاريخ نهاية التدريب")
    location = models.CharField(max_length=255, verbose_name="مكان إقامة البرنامج التدريبي", null=True, blank=True)
    room_number = models.CharField(max_length=50, verbose_name="رقم القاعة", null=True, blank=True)

    def __str__(self):
        return self.name

# انتساب معلم لتدريب
class Enrollment(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="المعلم")
    training_program = models.ForeignKey(TrainingProgram, on_delete=models.CASCADE, verbose_name="البرنامج التدريبي")
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")

    class Meta:
        unique_together = ("teacher", "training_program")
        verbose_name = "انتساب معلم لتدريب"
        verbose_name_plural = "انتسابات المعلمين للتدريبات"

    def __str__(self):
        return f"{self.teacher} -> {self.training_program}"
