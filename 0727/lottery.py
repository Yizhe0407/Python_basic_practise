# 2023/07/28
import random                               

lotterys = sorted(random.sample(range(1,50), 6))    
specialNum = random.randint(1,8) 

print("第xxx期威力彩號碼 ")
print(f"特別號:{specialNum}")             
for lottery in sorted(lotterys):            
    print(lottery, end=" ")
