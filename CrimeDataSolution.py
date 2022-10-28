#imports
import calendar



# functions
def month_from_number(month_in_number):
    for month in range(1,13):
        string_month = calendar.month_name[month_in_number]
    return string_month
        
def read_in_file(filename):
    contents_list = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            new_line = line.split(',')
            contents_list.append(new_line)
        return contents_list        
def create_reported_date_dict():
    count = 0
    dates = 0
    contents_list = read_in_file('CrimeDataVS.csv')
    for index in range(len(contents_list)):
        dates = contents_list[index+1][1])

        if contents_list[index+1][1] == dates_list[index]:
            count += count
            print(count)    
        
def create_offense_dict():
    pass
def create_offense_by_zip():
    pass


if __name__ == "__main__":

    # Main program
    print("KCPD Crime Data")
    create_reported_date_dict()
    

    
