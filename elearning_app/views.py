from django.shortcuts import render, get_object_or_404
from .models import Course, Category, Lesson, Review
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'elearning/course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lessons = course.lesson_set.all()
    reviews = course.review_set.all()
    return render(request, 'elearning/course_detail.html', {
        'course': course,
        'lessons': lessons,
        'reviews': reviews,
    })

def create_course(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category_id = request.POST.get('category_id')
        category = get_object_or_404(Category, id=category_id)
        instructor = request.user

        Course.objects.create(
            title=title,
            description=description,
            price=price,
            category=category,
            instructor=instructor
        )
        return HttpResponseRedirect(reverse('course_list'))

    categories = Category.objects.all()
    return render(request, 'elearning/create_course.html', {'categories': categories})

def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        course.delete()
        return HttpResponseRedirect(reverse('course_list'))

    return render(request, 'elearning/delete_course.html', {'course': course})

def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    return render(request, 'elearning/lesson_detail.html', {'lesson': lesson})


def create_lesson(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        video_url = request.POST.get('video_url')

        Lesson.objects.create(
            course=course,
            title=title,
            content=content,
            video_url=video_url
        )
        return HttpResponseRedirect(reverse('course_detail', args=[course_id]))

    return render(request, 'elearning/create_lesson.html', {'course': course})


from .models import Enrollment


def enroll_in_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        Enrollment.objects.create(
            user=request.user,
            course=course,
            status='enrolled'
        )
        return HttpResponseRedirect(reverse('course_detail', args=[course_id]))

    return render(request, 'elearning/enroll_in_course.html', {'course': course})


def view_enrollments(request):
    enrollments = Enrollment.objects.filter(user=request.user)
    return render(request, 'elearning/view_enrollments.html', {'enrollments': enrollments})


def create_review(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        Review.objects.create(
            course=course,
            user=request.user,
            rating=rating,
            comment=comment
        )
        return HttpResponseRedirect(reverse('course_detail', args=[course_id]))

    return render(request, 'elearning/create_review.html', {'course': course})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'elearning/category_list.html', {'categories': categories})


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    courses = category.courses.all()
    return render(request, 'elearning/category_detail.html', {
        'category': category,
        'courses': courses,
    })

from .models import Payment


def make_payment(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        amount = course.price
        Payment.objects.create(
            user=request.user,
            amount=amount,
            status='successful'
        )
        return HttpResponseRedirect(reverse('course_detail', args=[course_id]))

    return render(request, 'elearning/make_payment.html', {'course': course})


def payment_history(request):
    payments = Payment.objects.filter(user=request.user)
    return render(request, 'elearning/payment_history.html', {'payments': payments})

from .models import Quiz, QuizQuestion


def quiz_list(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    quizzes = course.quizzes.all()
    return render(request, 'elearning/quiz_list.html', {'course': course, 'quizzes': quizzes})


def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    return render(request, 'elearning/quiz_detail.html', {'quiz': quiz, 'questions': questions})


def submit_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)

    if request.method == 'POST':
        return JsonResponse({'message': 'Quiz submitted successfully!'})

    return render(request, 'elearning/submit_quiz.html', {'quiz': quiz})

from .models import UserProgress


def view_progress(request):
    progress = UserProgress.objects.filter(user=request.user)
    return render(request, 'elearning/view_progress.html', {'progress': progress})
