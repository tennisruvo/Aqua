num=int(raw_input())
devisors=[]
num_temp=num
mark=True
while mark:
        for devisor in range(2,num_temp+1):
                if num_temp%devisor==0 and devisor==num_temp:
                        devisors.append(str(devisor))
                        mark=False
                        break
                if num_temp%devisor==0:
                        devisors.append(str(devisor))
                        num_temp=num_temp/devisor
                       
print " ".join(sorted(devisors))
