import numpy as np



print("Paste Table Data here: ")
cip = input();




rowCount = cip.count("\n")+1
print(rowCount)

newArr = []

rows = cip.splitlines()
for row in rows:
    newArr.append(row.split("\t"))
#print(newArr)

colCount = len(newArr[0])

## Now we build the string containing the code needed


op = ""
op += "\\begin{table}[H] \n\\centering \n\\begin{tabular} \n"

op += "{|"
for i in range(colCount):
    op+= "c|"
op += "}\n\\hline\n"
firstdone = False

for row in newArr:
    for elt in row:
        op += elt
        op += " & "
    op = op[:-3]
    op += "\\\\ \n"
    if not firstdone:
        op+= "\\hline \n"
        firstdone = True
        
cap = input("Insert Table Caption: ")
print("")
print("")

op += "\\hline \n\\end{tabular}\n\\caption{" + cap + "} \n"
op += "\\label{tab:my-table}\n\\end{table}"
print(op);

#==============================================================================
# \begin{table}[H]
# \centering
# \begin{tabular}{|l|l|l|l|l|l|}
# \hline
# L (m) & $f_1$ (1) & $f_1$ (2) & $f_1$ (3) &$\bar f_1$ (Hz) & $\bar f_1 L$ (m/s) \\ \hline
# 0.3 & 212.3 & 212.3 & 212.3 & 212.3 & 63.69 \\
# 0.4 & 161.3 & 161.4 & 161.3 & 161.3 & 64.52 \\
# 0.5 & 127.4 & 127.4 & 127.4 & 127.4 & 63.7 \\
# 0.6 & 93.4 & 93.4 & 93.4 & 93.4 & 56.04 \\ \hline
# \end{tabular}
# \caption{Several readings of fundamental frequencies $f_1$ vs length $L$}
# \label{tab:my-table}
# \end{table}
#==============================================================================

#==============================================================================
# a	4	14	25.3	37	48.2	59.8	71.2	82.7
# v	4.1	14.1	25.4	37.2	48.4	60.1	71.6	82.5
# c	4.1	13.9	25.4	37	48.1	60.2	71.3	82.5
#==============================================================================
