#! /usr/bin/env python

"""
The program get_assignments.py pulls assignments down from canvas with the course specified by the required command line argument "course". It can get the assignments due after the current day or all the assignments due after a date specified by the command line argument --date. If the specific id of the course is passed through the command line arguement --id, the program will not search for the course name. If no course id is given, the program will search in the user's current courses for the correct course with the given course name. The program will write a text file within the current directory that contains the assignment name, due date, submission types, description, and relevant urls.   

Author: Cate Lukner

"""

import argparse # Command line arguments
import sys # For exit() 
from datetime import datetime, date # For date references with assignments
import re # For finding regex patterns in the assignments

# Canvas API
from canvasapi import Canvas

# Belhaven's Canvas URL
API_URL = "https://belhaven.instructure.com/"
# Token generated on Canvas
# API_KEY = <Only authorized people will be given this key.> 
# My Canvas user ID (Catherine Lukner)
# USER_ID = <Only authorized people will be given this ID> 


def get_course_id(canvas_obj, course_name):
    """ Searches within the courses of the current user with the specified name and 
    returns the id number of the course. It will exit the program if no course is found. """
    
    # Create a user object
    user = canvas_obj.get_user(USER_ID)
    # Get the users's courses
    user_courses = user.get_courses(enrollment_status='active', state='published')
    
    for course in user_courses:
        # Test for the give course name in the user's courses
        try:
            match_name = re.findall(f'\s{course_name.lower()}+', course.name.lower())
            if match_name:
                print(f"{course_name} found in {course.name}")
                # Return the id of the course
                return course.id 
        # Pass over the course if no name available
        except AttributeError:
            continue

    print(f"No courses found with the name {course_name}. Check your spelling or the order of the words in the course's name, then try again.")
    # Exit if no course found
    sys.exit()


def get_assignments_due(canvas_obj, course_id, date, include_no_date=False):
    """ Returns a list of assignments due past the specified date. """

    # Create course object with given id
    course = canvas_obj.get_course(course_id) 
    # Create list of assignments within the course
    assignments = course.get_assignments()
    # Create list that will contain the assignments due after the given date
    assignments_to_return = list()

    for assignment in assignments:
        # If the assignment has a due date and no date assignments should not be included
        if (assignment.due_at != None) and not include_no_date:
            due_date = datetime.strptime(assignment.due_at[:10], '%Y-%m-%d')
            # Add all assignments due after the given date
            if due_date > date:
                assignments_to_return.append(assignment)
        # If the assignment has no due date and assignnments with no due date should be included
        elif (assignment.due_at == None) and include_no_date:
            assignments_to_return.append(assignment)

    return assignments_to_return


def write_assignments(course_name, course_id, assignment_list, date):
    """ For all assignments in the given assignment list, it writes the assignment name, 
    description, due date, submission types, and relevant files to a text file. """
    
    # Ensure date correctly formatted for file name
    date_formatted = f'{date.year}-{date.month}-{date.day}'
    # Create formatted file name
    file_name = f'assignments_{course_name}-{course_id}_from_{date_formatted}.txt'
    # Regular expression to find URLs in assignment description
    url_re = '(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})'

    # Write assignments to a text file 
    with open(file_name, 'w') as f:
        for assignment in assignment_list:
            # Get only the text portion of the description
            description = re.sub(r'<[^<]+?>', '', str(assignment.description))
            # Write the assignment name
            f.write(f"\n\n\n{assignment.name}\n")
            # Due date
            f.write(f"\nDue Date: {assignment.due_at}\n")
            # Submission types
            f.write(f"\nSubmission Types: {','.join(assignment.submission_types)}\n")
            # Text of the Description
            f.write(str(description))
            # Find URLS 
            relevant_urls = re.findall(url_re, str(assignment.description))
            if relevant_urls:
                f.write('\nRelevant URLS:\n')
                for url in relevant_urls:
                    f.write(f'\n{url}')
        f.write('\n\n')
        print(f"{file_name} created.")


def main():
    """ Main Function """

    # Create arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('course', nargs='+', help='Name of the course. Do not type as a string. ')
    parser.add_argument('--id', help='Course id')
    parser.add_argument('--date', '--d', help='Get all assignments due past this date')
    parser.add_argument('--include_no_due_date', '--nd', type=bool,  
            help='Include the assignments with no due date. Type: Boolean')

    # Parse arguments
    args = parser.parse_args()

    # Create course object
    canvas = Canvas(API_URL, API_KEY)
    
    # Assign reference date for assignments
    if args.date == None:
        assignment_date = datetime.now() 
    else:
        try:
            assignment_date = datetime.strptime(args.date, '%Y-%m-%d')
        # Include command line argument correctly formatted
        except ValueError:
            print("You must give your date in the form %Y-%m-%d, for example 2019-08-08")
            print("Reformat your date and try again.")
            sys.exit()

    # Create a joined course name
    course_name = ' '.join(args.course)
 
    # Assign course id
    if args.id != None:
        course_id = int(args.id)
    else:
        course_id = get_course_id(canvas, course_name)
    
    # Write the assignments file if authorized. 
    try:
        list_of_assignments = get_assignments_due(canvas, course_id, assignment_date, args.include_no_due_date)
        write_assignments(course_name, course_id, list_of_assignments, assignment_date)
    except:
        print(f"You are not allowed to get assignments for {course_name} via this program.") 


if __name__=='__main__':
    main()
