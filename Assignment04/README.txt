
Name - Ravi Lahare
Roll No. - 210101086
Assignment - 04


---------------------------------------------------------------------------------------------------------------------
Question - 01
---------------------------------------------------------------------------------------------------------------------
code file       : question1.py

command to run  : python3 question1.py

description of code    : 1.first taken the input amount of money.
                         2.then i calculated no. of notes for each units (logic written below)
                         3.then i printed the min no. of denomination and its composition also
                         4.if there are multiple composition with min no. of denomination i printed all.

Logic           : 1.first i find the no. of notes of 50 units
                    for min no. of denomination we use note of 50 units as much as possible
                    no. of notes of 50 units = value/50 (floor integer)
                  2.then calculated remaining value after use of notes of 50 units
                  3.for calculating no. of notes of 1 unit i used remaining_value%5
                    because for paying 1,2,3 or 4 units we can use 1 units only.
                  4.then calculated remaining value after use of notes of 1 unit
                  5.Now the remaining value will be 0,5,10,15,20,25,30,35,40 or 45 for this i created 
                    the cases and calculated their min. notes see list below
                        for 0  = 0 note
                        for 5  = 1 note (5)
                        for 10 = 1 note (10)
                        for 15 = 2 note (10+5)
                        for 20 = 1 note (20)
                        for 25 = 1 note (25)
                        for 30 = 2 note (20+10 or 25+5)
                        for 35 = 2 note (10+25)
                        for 40 = 2 note (20+20)
                        for 45 = 2 note (25+20)


-----------------------------------------------------------------------------------------------------------------------
Question - 02 : Part - (i)
-----------------------------------------------------------------------------------------------------------------------
code file       : question2_part1.tex

for getting output  : compile code in the online compiler
                      first create the account in overleaf -> https://www.overleaf.com/
                      website : https://www.overleaf.com/project
                      create new project in above link then copy and paste my code there in the online editor 
                      then compile it then see output.

description : documentclass - article
              packages used - amsmath , hyperref
              thing used in code :
                  \hypersetup{} -> for setting reference color
                  \begin{document} -> start document 
                  \end{document} -> end document 
                  \title{} -> for title
                  \author{} -> for author Name
                  \date{} -> for date
                  \maketitle -> for making title
                  \section{} -> for creating section
                  \textbf{} -> for bold text
                  \LaTeX{} -> for print "latex" in its unique style
                  \begin{equation} -> begin equation with adding equation no.
                  \begin{equation*} -> begin equation without adding equation no.
                  \end{equation or equation*} -> end equation
                  \begin{align} ..... \end{align} -> for allign texts or equation uses &,&& for alligning
                  \vec{} -> for vector symbol 
                  \nabla -> for printing ∇
                  \cdot -> for dot product symbol
                  \quad -> for space
                  \frac{}{} -> for printing fraction
                  \rho -> for printing ρ
                  \epsilon -> for printing ε
                  \label{} -> for creating label for reference
                  \times -> for cross product symbol
                  \partial{} -> for printing ∂
                  \mu -> for printing μ
                  \textquotedblleft , \textquotedblright -> for double qoute
                  \rq -> right single qoute
                  \ref{} -> call to reference
                  \begin{pmatrix or bmatrix or matrix} -> for printing matrix
                  \vdots -> verticle dots
                  \ddots -> diagonal dots
                  \dots -> horizontal dots
                  _{} -> for printing in down part
                  ^ -> for printing in power


-----------------------------------------------------------------------------------------------------------------------
Question - 02 : Part - (ii)
-----------------------------------------------------------------------------------------------------------------------
code file       : question2_part2.tex

for getting output  : compile code in the online compiler
                      first create the account in overleaf -> https://www.overleaf.com/
                      website : https://www.overleaf.com/project
                      create new project in above link then copy and paste my code there in the online editor 
                      then compile it then see output.

description : documentclass - article
              packages used - amsmath
              thing used in code : i not repeated that items which are shown in part (i) :
                  \iiint -> for triple integration symbol
                  \limits_ -> for adding limit to integtation symbol
                  \lim_{h \to 0} -> limit h tends to 0
                  \begin{cases} -> for begining cases
                  \sum_ -> summation symbol sigma
                  \pi -> for printing π
                  \sin{} -> for sin
                  \cos{} -> for cos
                  \prod -> for prod sign (multiplication)
                  \nu ->  for printing nu 
                  \alpha -> for printing α
                  \beta -> for printing β
                  \gamma -> for printing γ
                  \Gamma -> for printing Γ
                  \delta -> for printing δ
                  \Delta -> for printing ∆
                  \Pi -> for printing Π
                  \omega -> for printing ω
                  \Omega -> for printing Ω

-----------------------------------------------------------------------------------------------------------------------
