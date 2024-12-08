from tkinter import *

def get_number():
    with open('next_number.txt', 'r') as f:
        current = int(f.read())
        f.close()
    return current

def write_next(current):
    with open('next_number.txt', 'w') as f:
        f.write(f"{current + 1}")
        f.close()

def create_log(title):
    try:
        with open(f'{title}.txt', 'x') as f:
            f.write(f"{title}:\n\n")
            f.close()
    except Exception as e:
        print(f"An <{e}> exception occurred when trying to create the log!")

def write_answer(title, qNum, qAnswer):
    with open(f'{title}.txt', 'a') as f:
        f.write(f'{qNum}: {qAnswer}\n')
        f.close()

def main():
    current = get_number()
    create_log(current)
    write_next(current)

    logged_answers = {}
    
    # tkinter gui handling
    root = Tk()
    root.title("Sparx Logger")
    root.geometry('385x100')
    
    padx = (5,0)
    pady = (2.5,0)
    
    #-# writing to log
    #-----# entering question number to log
    write_header = Label(root, text = "Log Answers").grid(row=0, columnspan=2)
    
    qNum_label = Label(root, text = "Number:")
    qNum_label.grid(row=1, sticky="w", padx=padx, pady=pady)
    
    qNum_entry = Entry(root, width = 20)
    qNum_entry.grid(column=1, row=1, padx=padx, pady=pady)
    
    #-----# entering question answer to log
    qAns_label = Label(root, text = "Answer:")
    qAns_label.grid(row=2, sticky="w", padx=padx, pady=pady)
    
    qAns_entry = Entry(root, width = 20)
    qAns_entry.grid(column=1, row=2, padx=padx, pady=pady)
    
    #-# searching log
    #-----# entering question number to search
    search_header = Label(root, text = "Search Logs").grid(row=0, column=2, columnspan=2)
    
    searchNum_label = Label(root, text = " Number:")
    searchNum_label.grid(column=2, row=1, sticky="w", padx=padx, pady=pady)
    
    searchNum_entry = Entry(root, width = 20)
    searchNum_entry.grid(column=3, row=1, sticky="w", padx=padx, pady=pady)
    
    outputTitle_label = Label(root, text = " Answer:")
    outputTitle_label.grid(column=2, row=2, sticky="w", padx=padx, pady=pady)
    
    outputRes_label = Label(root, text = "")
    outputRes_label.grid(column=3, row=2, sticky="w", padx=padx, pady=pady)
    
    
    def write():
        qNum = qNum_entry.get()
        qAns = qAns_entry.get()
        
        logged_answers[qNum] = qAns
        write_answer(current, qNum, qAns)
        
        print(logged_answers)
    
    def fetch():
        searchNum = searchNum_entry.get()
        outputRes_label.config(text=logged_answers[searchNum])
        return
        
    #-# button handling
    #-----# confirming log write
    writeLog_button = Button(root, text = "Write to file", command = write)
    writeLog_button.grid(column=1, row=3)
    
    #-----# confirming log search
    searchLog_button = Button(root, text = "Fetch answer", command = fetch)
    searchLog_button.grid(column=3, row=3)
    
    
    root.mainloop()
    
if __name__ == "__main__":
    main()