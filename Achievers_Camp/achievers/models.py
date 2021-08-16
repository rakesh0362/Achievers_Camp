from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.models import User
import os

# Create your models here.


class CurrentAffairs(models.Model):
    topic = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null=True, blank=True)
    NationalNews = models.TextField(max_length=2000, blank=True)
    InternationalNews = models.TextField(max_length=2000, blank=True)
    BooksAndAuthor = models.TextField(max_length=500, blank=True)
    AppointmentAndResignation = models.TextField(max_length=500, blank=True)
    AwardsAndHonours = models.TextField(max_length=500, blank=True)
    ImportantDays = models.TextField(max_length=500, blank=True)
    Obituary = models.TextField(max_length=500, blank=True)
    Sports = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.topic

    def save(self, *args, **kwargs):
        self.slug = slugify(self.topic)
        super().save(*args, **kwargs)


def save_subject_image(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.vocabulary_id:
        filename = 'Subject_Pictures/{}.{}'.format(instance.vocabulary_id, ext)
    return os.path.join(upload_to, filename)


class Vocabulary(models.Model):
    vocabulary_id = models.CharField(max_length=100, unique=True)
    word = models.CharField(max_length=100)
    partsofspeech = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    meaning = models.TextField(max_length=500)
    sentence = models.TextField(max_length=500)
    synonyms = models.CharField(max_length=100)
    antonyms = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to=save_subject_image, blank=True, verbose_name='Subject Image')
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.word

    def save(self, *args, **kwargs):
        self.slug = slugify(self.vocabulary_id)
        super().save(*args, **kwargs)


class ExamNotification(models.Model):
    exam_id = models.CharField(max_length=100, unique=True)
    topic = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    slug = models.SlugField(null=True, blank=True)
    subtopic = models.CharField(max_length=500)
    acivityDes = models.TextField(max_length=1000)
    footer = models.CharField(max_length=100)

    def __str__(self):
        return self.topic

    def save(self, *args, **kwargs):
        self.slug = slugify(self.exam_id)
        super().save(*args, **kwargs)


class ExamAnalysis(models.Model):
    examAnalysis_id = models.CharField(max_length=100, unique=True)
    topic = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    slug = models.SlugField(null=True, blank=True)
    examPattern = models.TextField(max_length=500)
    goodAttempt = models.TextField(max_length=1000)
    english = models.TextField(max_length=3000)
    maths = models.TextField(max_length=3000)
    reasoning = models.TextField(max_length=3000)
    generalAwareness = models.TextField(max_length=3000)
    generalStudies = models.TextField(max_length=3000)
    footer = models.CharField(max_length=100)

    def __str__(self):
        return self.topic

    def save(self, *args, **kwargs):
        self.slug = slugify(self.examAnalysis_id)
        super().save(*args, **kwargs)

# def save_lesson_files(instance, filename):
#     upload_to = 'Images/'
#     ext = filename.split('.')[-1]
#     # get filename
#     if instance.lesson_id:
#         filename = 'lesson_files/{}/{}.{}'.format(
#             instance.lesson_id, instance.lesson_id, ext)
#         if os.path.exists(filename):
#             new_name = str(instance.lesson_id) + str('1')
#             filename = 'lesson_images/{}/{}.{}'.format(
#                 instance.lesson_id, new_name, ext)
#     return os.path.join(upload_to, filename)


# class Lesson(models.Model):
#     lesson_id = models.CharField(max_length=100, unique=True)
#     Standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     subject = models.ForeignKey(
#         Subject, on_delete=models.CASCADE, related_name='lessons')
#     name = models.CharField(max_length=250)
#     position = models.PositiveSmallIntegerField(verbose_name="Chapter no.")
#     slug = models.SlugField(null=True, blank=True)
#     video = models.FileField(upload_to=save_lesson_files,
#                              verbose_name="Video", blank=True, null=True)
#     ppt = models.FileField(upload_to=save_lesson_files,
#                            verbose_name="Presentations", blank=True)
#     Notes = models.FileField(upload_to=save_lesson_files,
#                              verbose_name="Notes", blank=True)

#     class Meta:
#         ordering = ['position']

#     def __str__(self):
#         return self.name

#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.name)
#         super().save(*args, **kwargs)

#     def get_absolute_url(self):
#         return reverse('curriculum:lesson_list', kwargs={'slug': self.subject.slug, 'standard': self.Standard.slug})


# class Comment(models.Model):
#     lesson_name = models.ForeignKey(
#         Lesson, null=True, on_delete=models.CASCADE, related_name='comments')
#     comm_name = models.CharField(max_length=100, blank=True)
#     # reply = models.ForeignKey("Comment", null=True, blank=True, on_delete=models.CASCADE,related_name='replies')
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     body = models.TextField(max_length=500)
#     date_added = models.DateTimeField(auto_now_add=True)

#     def save(self, *args, **kwargs):
#         self.comm_name = slugify(
#             "comment by" + "-" + str(self.author) + str(self.date_added))
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return self.comm_name

#     class Meta:
#         ordering = ['-date_added']


# class Reply(models.Model):
#     comment_name = models.ForeignKey(
#         Comment, on_delete=models.CASCADE, related_name='replies')
#     reply_body = models.TextField(max_length=500)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     date_added = models.DateTimeField(auto_now_add=True)

# #     def __str__(self):
# #         return "reply to " + str(self.comment_name.comm_name)
