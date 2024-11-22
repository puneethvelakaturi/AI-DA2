% Import CSV library to load data
:- use_module(library(csv)).

% Load student data from CSV
load_students(File) :-
    csv_read_file(File, Rows, [functor(student), arity(3)]),
    maplist(assert, Rows).

% Define eligibility for scholarship
eligible_for_scholarship(Student_ID) :-
    student(Student_ID, Attendance, CGPA),
    Attendance >= 75,
    CGPA >= 9.0.

% Define permission for exams
permitted_for_exam(Student_ID) :-
    student(Student_ID, Attendance, _),
    Attendance >= 75.


:- use_module(library(http/thread_httpd)).
:- use_module(library(http/http_dispatch)).
:- use_module(library(http/http_json)).
:- use_module(library(http/http_parameters)).

% Start the server
start_server(Port) :-
    http_server(http_dispatch, [port(Port)]).

% Define endpoints
:- http_handler(root(scholarship), check_scholarship, []).
:- http_handler(root(exam_permission), check_exam_permission, []).

% Scholarship Eligibility Endpoint
check_scholarship(Request) :-
    http_parameters(Request, [student_id(Student_ID, [integer])]),
    (eligible_for_scholarship(Student_ID) ->
        Reply = json{student_id: Student_ID, eligible: true};
        Reply = json{student_id: Student_ID, eligible: false}),
    reply_json(Reply).

% Exam Permission Endpoint
check_exam_permission(Request) :-
    http_parameters(Request, [student_id(Student_ID, [integer])]),
    (permitted_for_exam(Student_ID) ->
        Reply = json{student_id: Student_ID, permitted: true};
        Reply = json{student_id: Student_ID, permitted: false}),
    reply_json(Reply).
