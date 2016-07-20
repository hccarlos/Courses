"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        """
        This is an example of loading a model.
        Every controller has access to the load_model method.
        """
        self.load_model('CourseModel')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        """
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)
        """
        # Get data from all courses
        all_courses = self.models['CourseModel'].get_all_courses()
        return self.load_view('index.html', all_courses=all_courses)
    def add_course(self):
        # This function calls the model to add course
        # Get form data about course & call model >> INSERT
        course = {
                    'name': request.form['name'],
                    'description': request.form['description']
                }
        # Return to root for index rendering
        self.models['CourseModel'].add_course(course)
        return redirect('/')
    def remove(self, course_id):
        # This function takes you to the remove course confirmation page
        # Call model >> SELECT, given course_id
        course = self.models['CourseModel'].get_course_by_id(course_id)
        # Render confirmation page, passing the model data to the page
        return self.load_view('remove.html', course=course[0])
    def remove_course(self, course_id):
        # This function calls the model to remove course
        # Call model >> DELETE, given course_id
        self.models['CourseModel'].delete_course(course_id)
        # return to root
        return redirect('/')


