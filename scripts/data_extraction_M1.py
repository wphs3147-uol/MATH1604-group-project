def extract_answers_sequence(file_path):
    with open(file_path, 'r') as file:
        answers = file.readlines() # reads file in
        answers = answers.lower()
    boxlines = []
    for line in answers:
        line = line.strip()
        if '[ ]' in line or '[x]' in line:
            boxlines.append(line) # filters by line with check boxes
    boxes = []
    for line in boxlines:
        boxes.append(line[:3]) # generates list of only checkboxes
    ansnum = []
    for i in range(0, len(boxes), 4):
        qboxes = boxes[i:i+4]
        if '[x]' in qboxes:
            ansnum.append(qboxes.index("[x]")+1)
        else:
            ansnum.append(0) # iterates through boxes in chunks of 4 (for each question) generates list of answers with 0 if unanswered
    return ansnum

def write_answers_sequence(answers, id):
    with open('answers_list_' + str(id) + '.txt', 'w') as file:
        file.write(str(answers))