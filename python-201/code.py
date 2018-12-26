# --------------
##File path for the file 
#file_path 


#Code starts here
def read_file(path):
    file = open(file_path,'r')
    sentence = file.readline();
    file.close();
    return sentence;

sample_message = read_file(file_path)
print(sample_message)    



# --------------
#Code starts here


def read_file(file_path_1):
    file1 = open(file_path_1)
    message_1 = file1.readline()
    print(message_1)
    return message_1

def fuse_msg(message_a,message_b):
    j =int(message_a)
    i =int(message_b)
    quotient= int(i/j)
    return str(quotient)

message_1 = read_file(file_path_1)
message_2 = read_file(file_path_2)
secret_msg_1 = fuse_msg(message_1,message_2)
#print(secret_msg_1)


# --------------
#Code starts here


def substitute_msg(message_c):
    #print('mc'+message_c)
    sub = ''
    if(message_c is 'Red'):
        return 'Army General'
    if(message_c == 'Green'):
        return 'Data Scientist'
    if(message_c is 'Blue'):
        return 'Marine Biologist'        

message_3 = read_file(file_path_3)
print(message_3)
secret_msg_2 = substitute_msg(message_3)  
print(secret_msg_2)


# --------------
# File path for message 4  and message 5
#file_path_4
#file_path_5

#Code starts here
message_4 = read_file(file_path_4)
message_5 = read_file(file_path_5)
print(message_4)
print(message_5)

def compare_msg(message_d,message_e):
    a_list = message_d.split()
    b_list = message_e.split()
    c_list = []
    for element in a_list:
            if element not in b_list:
                c_list.append(element) 
            
    final_msg = ' '.join(c_list)
    print(final_msg)
    return final_msg

secret_msg_3 = compare_msg(message_4,message_5)


# --------------
#Code starts here

message_6 = read_file(file_path_6)
even_word = lambda x : len(x)%2==0

def extract_msg(message_f):
    a_list = message_6.split()
    b_list=list(filter(even_word,a_list))
    return ' '.join(b_list)

secret_msg_4 = extract_msg(message_6);    


# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]


final_path= user_data_dir + '/secret_message.txt'

#Code starts here
secret_msg = ' '.join(message_parts)

def write_file(secret_msg,path):
    file = open(path,'a+')
    file.write(secret_msg)
    file.close()

write_file(secret_msg,final_path)    
print(secret_msg)


