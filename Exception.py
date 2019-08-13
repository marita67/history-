Total_marks=int(input(“enter total marks scored:”))
Num_of_sections=int(input(“enter num of sections:”))
Average=0;
Try:
   average=int(total_marks/num_of_sections)
Except ZeroDivisionError
     Print(“there has to be atleast 1 or more than 1 sections”)
Print(“average marks scored per section is :”,average)
