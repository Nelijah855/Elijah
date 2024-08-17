"""
this is an experiment given data to the ai model to predict whether the answer is TRUE /FALSE

>>>>>THE EXPERIMENT IS TO PREDICT WHETHER THE STUDENT WILL PASS UNEB

               [VARIABLES]

               1...GIVEN THAT THE STUDENT ATTEND (CLASSES) 
               2...STUDENT HAS (NOTES) 
               3...STUDENT PASSED (PLE)
               4...STUDENT PAYS (SCHOOL) FEES IN TIME
               5...STUDENT (REVISES)


"""

"""
            >>>>>SOLUTION

             INPUT &WEIGHTS RESPECTIVELY
             (1,2)
             (1,.3)
             (2,.2)
             (1,5)
             (2,4)

             >>>>>THE NUERAL_NETWORK COMPUTES THE SUMMATION OF ALL INPUTS*WEIGHTS AND GETS THE TOTAL WHICH IS ==z
             THERE AFTER IT PASSES THE OUTPUT TO THE RECTILINEAR /LINEAR/RELU FUNCTION AND THEN ADD ABAIS OF 0.5 OR -O.5 TO CORRECT THE DOMAIN 
             AND THEN RECIEVE THE FINAL PREDICTION
             WHEN THE FINAL OUTPUT IS 0-0.49, THE ANSWER IS FALSE ; WHILE IF THE ANSWER IS 0.5-1 ,THE ANSWER IS TRUE
               
"""