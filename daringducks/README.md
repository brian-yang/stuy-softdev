# Stuydash - Team Daring Ducks
## Members

* Shaeq Ahmed <br>
* Brian Yang  <br>
* Karol Regula <br>
* Amy Xu       <br>

## Youtube Link
[StuyDash](https://www.youtube.com/watch?v=OTzorMQkPDg&feature=youtu.be)

## Overview
StuyDash is a website that allows students and teachers to coordinate assignments seamlessly. Teachers are allowed to create classes and assignments, as well as view their students' assignments. Students can join classes and submit assignments to their teachers through the website. Both the student and teacher dashboards come with a to-do list to help them keep track of their work and a calculator to scare away the math monsters.

## Installation and run instructions

###To install:

1. Type ```$ git clone https://github.com/brian-yang/daring-ducks``` into your terminal

2. Alternatively, you can download the repo as a ZIP file and unzip.

###To run:

1. Type ```$ python app.py``` into your terminal.

*note: our website does not need any external libraries or installations!*

## How to use our website
1. Create an account either as a teacher or a student on the registration page.
2. As a teacher, you can create classes on the homepage by clicking the Add Class button. Teachers can use whatever course code they like when they are creating classes. As long as the course code or course title is not taken, teachers can create as many courses as they like. The course codes must be given to students so they can join the class.
3. As a student, you can join classes given the class codes from your teachers by clicking the Join Class button on the home page.
4. Both teachers and students can see the classes they're a part of on their home pages.
5. Teachers can create assignments by clicking Create Assignment on the class page for a specific class. Teacher should give the assignment a description to help the students understand what they should do.
6. Students can submit assignments by clicking on the assignment on the class page, and they'll be directed to a submission box where they can submit their assignment.
7. Once students have submitted assignments, teachers can give students a grade by viewing the student submissions for an assignment after clicking on the assignment on the class page. The grades are visible to students on the assignment page where they submitted their assignments.
8. Both teachers and students have access to to-do lists and an online calculator (which makes a GET request to a calculator API).
