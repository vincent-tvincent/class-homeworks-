class fileAPI:

    def __init__(self,name,split,elements):
        self.name = name + ".txt"
        self.split = split
        self.elements = elements
        self.record_number = 0

    def write(self,items):
        file = open(self.name,"w")
        file.writelines()
        for i in items:
            file.write(i + self.split)
        file.close()
        self.record_number += 1

    def read(self,trace_back = 0):
        file = open(self.name, "r")
        record = ""
        record_list = [""]
        for i in self.record_number - trace_back:
            record = i

        for i in record:
            if i != self.split:
                record_list[len(record_list) - 1] += file.readline()
            record_list += ""
        file.close()
        return record_list

    def inject_data(self,dictionary,trace_back):
        record = self.read(trace_back)
        dictionary_keys = []
        for key in dictionary.keys():
            dictionary_keys += key
        for i in len(record) - 1:
            dictionary[dictionary_keys[i]] = record[i]





