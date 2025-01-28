print('*'*20)
num=int(input('Enter the number of people:'))
print('*'*20)
for i in range(1,num+1):
    no=int(input('Enter the recipent number:'))
    name=input('Enter the recipent name:')
    ht=float(input('Enter the recipent height in cm:'))
    wt=float(input('Enter the recipent weight kg:'))
    ht_m=ht/100
    BMI=wt/ht_m**2
    if BMI<18.5:
        print(str(i)+')',name)
        print(name,'BMI is',BMI)
        print(name,'is underweight')
        choiceU=input('Enter the choices for your development[YES,NO]:')
        if choiceU=='YES':
            j=int(input('enter the age:'))
            if j>=3 and j<=10:
                print('''The diet you must follow are:
                          1.Eat fresh vegetables and meat
                          2.Include more  protein and fat rich foods
                          3.Always try to eat homemade food''')
            elif j>=11 and j<=30:
                print('''The diet you must follow are:
                          1.Heavy food items that are rich in calories
                          2.Avoid Gym
                          3.Intake of snacks,juices,etc frequently''')
            elif j>=31 and j<=90:
                print('''The diet you must follow are:
                          1.Try to include protein frequently
                          2.Try to intake energy foods
                          3.Get advice from specalised doctors for protein tablets''')
        if  choiceU=='NO':
            pass
        
    elif BMI>=18.5 and BMI<=24.9:
        print(str(i)+')',name)
        print(name,'BMI is',BMI)
        print(name,'is normal')
    elif BMI>=25.0 and BMI<=29.9:
        print(str(i)+')',name)
        print(name,'BMI is',BMI)
        print(name,'is overweight')
        choiceOV=input('Enter the choices for your development[YES,NO]:')
        if choiceOV=='YES':
            m=int(input('enter the age:'))
            if m>=3 and m<=10:
                print('''The diet you must follow are:
                         1.Eat vegetables,fruits and whole grain products
                         2.drink more water
                         3.avoid sugar drinks,cold drinks''')
            elif m>=11 and m<=30:
                print('''The diet you must follow are:
                         1.Eat vegetables,fruits atleat 3 times a day
                         2.running,yoga,gym recommended
                         3.avoid sugar drinks,cold  drinks''')
            elif m>=31 and m<=90:
                print('''The diet you must follow are:
                         1.walking recommended for 2km
                         2.avoid sugars and other empty calories
                         3.stay hydrated''')
            if choiceOV=='NO':
                pass
    elif BMI>30:
        print(str(i)+')',name)
        print(name,'BMI is',BMI)
        print(name,'is in obesity')
        choiceOB=input('Enter the choices for your development[YES,NO]:')
        if choiceOB=='YES':
            z=int(input('enter the age:'))
            if z>=3 and z<=10:
                  print('''The diet you must follow are:
                           1.intake of lean meat,pulses,fruits,eggs,milk
                           2.Avoid meat,cheese,vegetable oil
                           3.Excercise daily, yoga,running minimum 3km''')
            elif z>=11 and z<=30:
                print('''The diet you must follow are:
                         1.Don't skip meal
                         2.Don't eat more than two or three pieces of fruit
                         3.Avoid rice
                         4.drink more water
                         5.Excercise one hour a day''')
            elif z>=31 and z<=90:
                print('''The diet you must follow are:
                         1.Consult specialised doctor
                         2.eat vegetables,diary free products,lean meat,fish
                           poultry,beans and nuts
                         3.Excercise one and half  hour
                         4.walk maximum 5-10km''')
            sug=input('Would you like know info about obese surgery[YES,NO]:')
            if sug=='YES':
                print('Name of the surgery: bariatric surgery ')
                print('''The cost is: 2,93,000 rupess\nGeneral cost is:5,00,000 rupess''')
                print('success rate is 90%''')
                print('''risk  of (i)anesthetic\n\t(ii)infection\n\t(iii)bleeding''')
            if sug=='NO':
                pass
print('''********************************THANK YOU FOR LOGINING IN********************************''')

        
    





