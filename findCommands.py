#!/usr/bin/python3

import sys

class command():
    def __init__(self, string, integer):
        self.command_string = string
        self.count = integer

class command_list():
    # Default constructor for the command_list object
    def __init__(self):
        self.command_array = []

    """
        Precondition: Takes in the value to add
        Postcondition: Constructs a new command object and appends to the command array
    """
    def add_value(self, value):
        new_command = command(value, 1)
        self.command_array.append(new_command)

    """
        Precondition: Takes in the value to locate
        Postcondition: Returns the index of the located value in the array
    """
    def find_value(self, value):
        index = -1
        for instance in self.command_array:
            index += 1
            if(value == instance.command_string):
                return index
        return -1

    """
        Precondition: Takes in the indices of commands to swap
        Postcondition: Swaps the commands at the specified locations
    """
    def swap(self, index1, index2):
        temp_command = self.command_array[index1]
        self.command_array[index1] = self.command_array[index2]
        self.command_array[index2] = temp_command

    """
        Precondition: The index to increment
        Postcondition: Increments the command count at command_array[index]
    """
    def increment(self, index):
        self.command_array[index].count += 1

    """
        Precondition: n/A
        Postcondition: Exports the data in the command_array to an output file
    """
    def export(self, form):
        if(form == "text"):
            text = open("output.txt", "w+")
        elif(form == "csv"):
            text = open("output.csv", "w+")
            text.write("Command, Instances\n")
        for value in self.command_array:
            text.write(value.command_string + ", " + str(value.count) + '\n')

    """
        Precondition: n/A
        Postcondition: Sorts the command_array into descending order using Selection Sort
    """
    def sort(self):
        for i in range(len(self.command_array)):
            max_val = i
            for j in range(i+1, len(self.command_array)):
                if self.command_array[max_val].count < self.command_array[j].count:
                    max_val = j
            self.swap(i, max_val)


if __name__ == "__main__":
    #Opens the file
    if(len(sys.argv) == 3):
        file = open(sys.argv[1])
        if(sys.argv[2] != "text" or sys.argv[2] != "csv"):
            print("Error! None supported output type!")
            exit()

        #Initialize command array
        godList = command_list()

        #Traverses every line of the file
        line_count = 1
        for line in file:
            line_array = line.split()
            if len(line_array) != 0:
                if line_array[0][0] != '.':
                    if(len(godList.command_array) == 0):
                        godList.add_value(line_array[0])
                    else:
                        index = godList.find_value(line_array[0])
                        if(index >= 0):
                            godList.increment(index)
                        else:
                            godList.add_value(line_array[0])
            line_count += 1

        godList.sort()
        godList.export(sys.argv[2])
    else:
        print("Error! Correct syntax for this program is: ./findCommands.py <file to read> <'csv' or 'text'>")