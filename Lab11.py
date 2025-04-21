import os
import matplotlib.pyplot as plt

students_file = open('data/students.txt', 'r')
assignments_file = open('data/assignments.txt', 'r')

def formatter(): # uses for loops to format the info into dictionaries
    s = {}
    a = {}
    a2 = {}
    a_list = []
    for i in students_file: # fills dict with names as keys and ids as values
        s[f'{i[3:-1]}'] = i[0:3]

    for i in assignments_file:
        a_list.append(i[:-1])

    for i in range(1,len(a_list),3):
        a[a_list[i]] = None

    for i in range(0,len(a_list),3):
        a[a_list[i+1]] = [str(a_list[i])]

    for i in range(2,len(a_list),3):
        a[a_list[i-1]] += [int(a_list[i])]

    for i in assignments_file:
        a_list.append(i[:-1])  # strips newline

    for i in range(0,len(a_list),3):
        a2[a_list[i]] = None  # initialize with assignment name as key

    for i in range(1,len(a_list),3):
        a2[a_list[i-1]] = [a_list[i]]  # add assignment id

    for i in range(2,len(a_list),3):
        a2[a_list[i-2]] += [a_list[i]] # add max points

    return s, a, a2

if __name__ == '__main__':
    students, assignments, assignments2 = formatter() # creates students/assignments dicts
    while True:
        print('1. Student grade')
        print('2. Assignment statistics')
        print('3. Assignment graph\n')
        sel = input('Enter your selection: ')

        if sel == '1':
            name = input("What is the student's name: ")
            counter = 0
            if name not in students.keys():
                print('Student not found.\n')
                continue
            submissions = os.path.join('data', 'submissions')
            score = 0
            for f_name in os.listdir(submissions):
                file_path = os.path.join(submissions, f_name)
                file = open(file_path, 'r')
                for line in file:
                    if students[name] == str(line[:3]):
                        assignment_id = line[4:9]
                        a_score = line[10:]
                        if assignment_id[-1] == '|':
                            assignment_id = line[4:8]
                            a_score = line[9:]
                        weight = (int(a_score)/100) * float(assignments[str(assignment_id)][1])
                        score += weight
            final = (score / 1000) * 100
            final = round(final)
            print(f'{final}%\n')

        if sel == '2':
            assignment = input("What is the assignment name: ")
            if assignment not in assignments2.keys():
                print('Assignment not found.\n')
                continue
            submissions = os.path.join('data', 'submissions')
            scores = []
            for f_name in os.listdir(submissions):
                file_path = os.path.join(submissions, f_name)
                file = open(file_path, 'r')
                for line in file:
                    assignment_id = line[4:9]
                    a_score = line[10:]
                    if assignment_id[-1] == '|':
                        assignment_id = line[4:8]
                        a_score = line[9:]
                    if assignments2[assignment][0] == assignment_id:
                        scores.append(round(int(a_score)))
            min_score = min(scores)
            max_score = max(scores)
            total = 0
            for score in scores:
                total += score
            average = total / len(scores)-1
            print(f'Min: {min_score}%')
            print(f'Avg: {round(average)}%')
            print(f'Max: {max_score}%\n')

        if sel == '3':
            assignment = input("What is the assignment name: ")
            if assignment not in assignments2.keys():
                print('Assignment not found.\n')
                continue
            submissions = os.path.join('data', 'submissions')
            scores = []
            for f_name in os.listdir(submissions):
                file_path = os.path.join(submissions, f_name)
                file = open(file_path, 'r')
                for line in file:
                    assignment_id = line[4:9]
                    a_score = line[10:]
                    if assignment_id[-1] == '|':
                        assignment_id = line[4:8]
                        a_score = line[9:]
                    if assignments2[assignment][0] == assignment_id:
                        scores.append(round(int(a_score)))
            min_score = min(scores)
            max_score = max(scores)
            total = 0
            for score in scores:
                total += score
            average = total / len(scores)
            plt.hist(scores, bins=6, color='black', edgecolor='yellow')
            plt.show()