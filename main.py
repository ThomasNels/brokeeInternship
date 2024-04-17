##
# This program runs to check a cover letter. It does this by checking the cover letter for certain questions that are true or false, adding the values and taking
# an average to find the highest score. Closer to 1 means a better cover letter, further means a worse cover letter.
#

import subprocess
subprocess.check_call(["pip", "install", "-q", "-r", "requirements.txt"])
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
        for q in ["What past experience with artifical intelligence does this canditate have?", "What projects has this canditate worked on related to artificial intelligence?", "What has the canditate done in a team environment?"]:
            print(q)
            print(cover_letter(path, q)["answer"])
            
    elif position == "devops":
        for q in ["What past experience with devops does this canditate have?", "What projects has this canditate worked on related to devops?", "What has the canditate done in a team environment?"]:
            print(q)
            print(cover_letter(path, q)["answer"])
    
    elif position == "frontend":
        for q in ["What past experience with frontend development does this canditate have?", "What projects has this canditate worked on related to frontend development?", "What has the canditate done in a team environment?"]:
            print(q)
            print(cover_letter(path, q)["answer"])
    
    else:
        print("Invalid position, make sure you entered lowercase: ai, devops, or frontend.")


main()
