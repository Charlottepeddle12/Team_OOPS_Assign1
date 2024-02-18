import csv
    
class Customer:
    
    def __init__(self,cust_id: int,first_name,last_name,company_name,address,city,state,zipt):
        self.cust_id=cust_id
        self.first_name=first_name
        self.last_name=last_name
        self.company_name=company_name
        self.address=address
        self.city=city
        self.state=state
        self.zipt=zipt
           
    def info():
        cust=[]
        with open('customers.csv') as customers:
             custs=csv.reader(customers)
             for i in custs:
                 cust.append(Customer(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
                 
     
        return cust

def main():
    c=Customer.info()
    f='y'
    while f=='y':
        choice=input('enter customer id: ')
        print()
        has_id=False
        for i in c:
              if choice == i.cust_id:
                  has_id=True
                  print('',i.first_name,i.last_name,'\n',i.company_name,i.address,'\n',i.city,i.state,i.zipt)
                  print()
        if has_id==False:
            print('No customer with that ID')
                  
        cont=input('Continue (Y/N): ')
        if cont=='N'or cont=='n':
            print('bye')
            break
                           
        
if __name__=="__main__":
    main()            
        