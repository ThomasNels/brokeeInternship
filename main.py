##
# This program runs to check a cover letter. It does this by checking the cover letter for certain questions that are true or false, adding the values and taking
# an average to find the highest score. Closer to 1 means a better cover letter, further means a worse cover letter.
#

from transformers import pipeline
import sys

def main():
    args = sys.argv
    cover_letter_eval(args[1], args[2])


def cover_letter_eval(path, position):
    """This is the function to evaluate the suitability for the canditate. 

    path -- the path to the file to analyze.
    position -- the position the person is applying for.
    """
    cover_letter = pipeline('document-question-answering')
    if position == "ai":
        for q in ["What past experience with artifical intelligence does this canditate have?", "Does this canditate have more than one internship?", "Does this canditate have internship experience? T/F"]:
            print(cover_letter(path, q))
            
    elif position == "devops":
        for q in ["Does this canditate have relavant devops experience? T/F", "How many internships has this canditate done?", "Does this canditate have internship experience? T/F"]:
            print(cover_letter(path, q))
    
    elif position == "frontend":
        for q in ["Does this canditate have relavant frontend development experience? T/F", "How many internships has this canditate done?", "Does this canditate have internship experience? T/F"]:
            print(cover_letter(path, q))
    
    else:
        print("Invalid position, make sure you entered lowercase: ai, devops, or frontend.")


main()
