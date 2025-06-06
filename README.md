
# 🗓️ Timetable Management System

## 👨‍💻 Team Members

| Name           | Roll Number | LinkedIn | GitHub |
|----------------|-------------|----------|--------|
| Haris Shahzad | 23P-0573    | [LinkedIn](https://www.linkedin.com/in/haris-shahzad-7b8746291/) | [GitHub](https://github.com/Zenvila) |
| Abdul Rafy     | 23P-0560    | [LinkedIn](https://www.linkedin.com/in/abdul-rafy-b11829315/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app) | [GitHub](https://github.com/Abdul-Rafy2005) |
| Muhammad Taha  | 23P-0559    | [LinkedIn](https://www.linkedin.com/in/muhammad-taha-57713b247/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app) | [GitHub](https://github.com/BoltTaha) |

---

## 🎯 Project Purpose

Managing class schedules via PDFs can be very tedious for students. Often, students have to scroll through long documents just to find their weekly class schedules. This project aims to eliminate that hassle by providing a digital, **web-based Timetable Management System**.

We propose a system with **two interfaces**:

### 👤 Student Interface
- Students can **enter their roll number** and view their personalized timetable.
- Features include:
  - Search by **Time**
  - Search by **Day**
  - Search by **Class**

### 🛠️ Admin Interface
- Admin has control over the system and can:
  - Add/Edit/Delete students
  - Manage teachers, courses, rooms, and schedules
  - Configure overall timetable data

---

## 💻 Technologies Used

| Component            | Technology      |
|----------------------|-----------------|
| **Programming Language** | Python            |
| **Database**         | SQLite3          |
| **Frontend GUI**     | Tkinter (Python GUI Library) |
| **Database Management** | SQL Scripts embedded in Python |
| **ER Diagram**       | Drawn using draw.io / dbdiagram.io |
| **IDE**              | VS Code / PyCharm |
| **Version Control**  | Git & GitHub     |
| **Browser**          | LQIEt Browser for embedded student view |

---

## 🚀 Installation & Run Instructions

To run the Timetable Management System on your local machine:

### ✅ Prerequisites

Make sure you have Python 3 installed. You can download it from [https://www.python.org/downloads/](https://www.python.org/downloads/)

Install required libraries:
```bash
pip install tk sqlite3  sqlitebrowser  
```

> **Note:** Tkinter comes pre-installed with Python in most distributions. If not, install manually depending on your OS.

---

### 📂 Run Order

1. **Create the Database Schema** (only once):
```bash
python schema.py
```

2. **Launch the Application**:
```bash
python main.py
```

The system will launch with both **Admin** and **Student** access panels.

---
## 📊 Tables & Their Purpose

| Table Name              | Purpose |
|-------------------------|---------|
| **Admins**              | Stores admin credentials for secure access. |
| **Students**            | Holds student records, roll numbers, and section IDs. |
| **Teachers**            | Contains teacher details including name, email, and department. |
| **Courses**             | Stores course data such as code, name, and credit hours. |
| **Sections**            | Groups students into logical classes (sections). |
| **Departments**         | Maintains information about academic departments. |
| **Rooms**               | Contains physical room data like capacity and type. |
| **Days**                | Represents weekdays. |
| **TimeSlots**           | Defines individual time slots for scheduling. |
| **ClassTimes**          | Binds course offerings with time, room, and slot. |
| **ClassTypes**          | Categorizes the types of classes (e.g., Lecture, Lab). |
| **CourseOfferings**     | Links courses to sections, teachers, and semesters. |
| **Semesters**           | Stores data for academic semesters. |
| **class_schedule**      | Main schedule table mapping students to teachers, courses, and timing. |
| **DeletedStudents**     | Archive table to track students removed by an admin. |
| **TeacherOfficeAssignments** | Links teachers to their assigned office rooms. |
| **TeacherOfficeRooms**  | Stores information about teacher office rooms. |

---

## 🎓 FAST NUCES
Project developed under the Department of Computer Science at FAST National University of Computer and Emerging Sciences.

---

