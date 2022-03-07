# Mohamed Mahmoud
# Social Media Friends Program

# - Start of the Program -

def get_all_friends(fb, target):
    result=set()
    
    for i in fb.items():
        username=i[0]
        friends=i[1]
        if username==target:
            new_user=fb[target]
            if new_user==set():
                exception_case=set()
                return exception_case
            else:
                for j in new_user:
                    other_user=fb[j]
                    result.add(j)
                    for z in other_user:
                        result.add(z)
    result.remove(target)
    return result

# ---------------------------- Testing ----------------------------
        
# friendships={'dominiquedoucet':{'menardmaurice','philippecharron'},
#              'juliette52':{'gabriel95','josephlachance','menardmaurice'},
#              'gabriel95':{'juliette52'},
#              'josephlachance':{'juliette52','menardmaurice'},
#              'philippecharron':{'dominiquedoucet'},
#              'lcote':set(),
#              'menardmaurice':{'dominiquedoucet','josephlachance','juliette52'}
#              }
 
# friends=get_all_friends(friendships, "gabriel95")
# print(friends)
 
# friends=get_all_friends(friendships, "menardmaurice")
# print(friends)
 
# # # example1=get_all_friends(friendships, "josephlachance")
# # # print(example1)
 
# # # example2=get_all_friends(friendships, "dominiquedoucet")
# # # print(example2)
 
# # # example3=get_all_friends(friendships, "juliette52")
# # # print(example3)
 
# # # example4=get_all_friends(friendships, "philippecharron")
# # # print(example4)
 
# # # example5=get_all_friends(friendships, "lcote")
# # # print(example5)

# - End of the Program -