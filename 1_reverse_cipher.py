msg=input("input your message:")
n=len(msg)
reverse_msg=''
i=n-1
while (i >= 0):
    reverse_msg=reverse_msg + msg[i]
    i= i - 1
print("Revers cipher of message is", reverse_msg)