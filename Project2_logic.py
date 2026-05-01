from PyQt6.QtWidgets import *
from Project2 import *
import csv

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        """
        This is the initialization function which is in charge of initializing the submit button
        as well as hiding the three scores until an input is given.
        """

        super().__init__()
        self.setupUi(self)
        self.Submit_button.clicked.connect(self.submit)
        self.score1_label.hide()
        self.score2_label.hide()
        self.score3_label.hide()
        self.score1_inp.hide()
        self.score2_inp.hide()
        self.score3_inp.hide()

    def submit(self):
        """
        The submit function is in charge of basically everything due to the fact that there is only one
        button
        :return:
        """
        self.Warning_label.setStyleSheet("color: red;")
        #This hides all of the labels at the start until they press the little submit button for the test taken

        total_tests = self.test_input.text().strip()
        #The code below is in charge of ensuring that the input for the amount of tests is a number
        # and that its between 1 and 3
        if total_tests.isdigit():
            total_tests = int(total_tests)
        else:
            self.Warning_label.setText("Please enter a number 1-3!")
            return
        if total_tests > 3 or total_tests < 1:
            self.Warning_label.setText("Please enter a number 1-3!")
            return
        name = self.name_input.text()

        #this goes through each position looking for a digit in name
        # also checks if name is empty and ensures that if either occurs that it doesn't
        #break the program
        if any(char.isdigit() for char in name):
            self.Warning_label.setText("Sorry, no numbers in names!")
            return
        elif name == "":
            self.Warning_label.setText("Please enter a name!")
            return
        # Below is revealing the number of labels based off total tests
        if total_tests == 1:
            self.score1_label.show()
            self.score1_inp.show()
        elif total_tests == 2:
            self.score1_label.show()
            self.score1_inp.show()
            self.score2_label.show()
            self.score2_inp.show()
        elif total_tests == 3:
            self.score1_label.show()
            self.score1_inp.show()
            self.score2_label.show()
            self.score2_inp.show()
            self.score3_label.show()
            self.score3_inp.show()
            #Below gets the score and assigns it
        score1 = self.score1_inp.text().strip()
        score2 = self.score2_inp.text().strip()
        score3 = self.score3_inp.text().strip()

        #The following is AI the reason for me using this was because i was stuck for a while as it kept crashing over and over and over
        # so this will ensure that even if the scores are empty they wont brick my code as it tests each score to see if its there.
        #I also talk more about it in the video please let me know if im missing anything because even though I
        # rushed through the video and retook it several times it still came out to seven minutes
        scores = []
        try:
            score1 = int(self.score1_inp.text().strip())
        except ValueError:
            self.Warning_label.setText("Enter valid number for Score 1!")
            return
        scores.append(score1)
        if total_tests >= 2:
            try:
                score2 = int(self.score2_inp.text().strip())
            except ValueError:
                self.Warning_label.setText("Enter valid number for Score 2!")
                return
            scores.append(score2)
        if total_tests >= 3:
            try:
                score3 = int(self.score3_inp.text().strip())
            except ValueError:
                self.Warning_label.setText("Enter valid number for Score 3!")
                return
            scores.append(score3)
        for s in scores:
            if s < 0 or s > 100:
                self.Warning_label.setText("Scores must be 0–100!")
                return
        #-------------------------------------------------------------


        #this just gets the highest score
        highest_score = max(scores)

        #This is in charge of setting the heading each time the program runs as well as
        #sending the data over to the csv file
        with open("dataaa.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Score1", "Score2", "Score3", "Highest Score"])
            writer.writerow([name,*scores,highest_score])
        #this changes the warning label at the very end once everything is cleared
        self.Warning_label.setText("Submitted!")



