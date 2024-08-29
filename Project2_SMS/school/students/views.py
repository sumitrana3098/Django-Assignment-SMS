from django.shortcuts import render, redirect

from students.models import Student
from .forms import StudentForm
from django.shortcuts import get_object_or_404

# Create your views here.

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})


def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/update_student.html', {'form': form})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'students/delete_student.html', {'student': student})

# def student_list(request):
#     students = Student.objects.all()
#     return render(request, 'students/student_list.html', {'students': students})

def student_list(request):
    grade = request.GET.get('grade')
    if grade:
        students = Student.objects.filter(grade=grade)
    else:
        students = Student.objects.all()
    grades = Student.objects.values_list('grade', flat=True).distinct()

    context = {
        'students': students,
        'grades': grades
    }
    return render(request, 'students/student_list.html', context)


