"""from flask import Flask, render_template, request, redirect, url_for, flash, session, make_response
from flask_mysqldb import MySQL
from sqlalchemy import func
import psycopg2

app = Flask(__name__)  
conn = psycopg2.connect(user="postgres", password="lilian",
                        host="localhost", port="5432", database="crypto")
# Open a cursor to perform database operations
cur = conn.cursor()
app.config["SECRET_KEY"] = "#lilian"

# Intialize MySQL
mysql = MySQL(app)


class Profitloss(db.Model):
    __tablename__ = 'profitloss'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    investment = db.Column(db.Integer, nullable=False )
    buy_price = db.Column(db.Integer, nullable=False)
    sell_price = db.Column(db.Integer, nullable=False)
    investment_fee = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    
    def insert(self):
        db.add(self)
        db.commit()

        return self
db.create_all()


@app.route('/dashboard', methods=['GET', 'POST'])  
def dashboard():  
    #if 'username' in session:  
      #  username = session['username']  
        return render_template('index.html')  
    #else:  
     #   return redirect(url_for('login'))  
@app.route('/profitloss', methods=['GET', 'POST'] )
def profitloss():
    if request.method == 'POST':
        investment = request.form['investment']
        print (investment)
        buy_price= request.form['buy_price']
        print(buy_price)
        sell_price= request.form['sell_price']
        print(sell_price)
        investment_fee= request.form['investment_fee']
        print(investment_fee)
        exit_fee= request.form['exit_fee']
        print(exit_fee)
        profit= int(sell_price) - int(buy_price)
        print(profit)
        totalinv= int(investment) + int(buy_price)
        print(totalinv)
        totalexit= int(investment) + int(buy_price)
        print(sum)

        #total = total(investment=investment, buy_price=buy_price, sell_price=sell_price, investment_fee=investment_fee, exit_fee=exit_fee)
        #print(total)
        cur.execute(
            "INSERT INTO profitloss (investment,buy_price,sell_price,investment_fee,exit_fee) VALUES(%s,%s,%s,%s,%s)",
            (investment,buy_price,sell_price,investment_fee,exit_fee),
        )
        return redirect('/profitloss')
    else:
        return render_template('profitloss.html')  

     
if __name__ == '__main__':
    app.run(debug=True)

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")
        

# pip install tkinter
import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN
 
window = tk.Tk()
window.title('Calculator-GeeksForGeeks')
frame = tk.Frame(master=window, bg="skyblue", padx=10)
frame.pack()
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)
 
 
def myclick(number):
    entry.insert(tk.END, number)
 
 
def equal():
    try:
        y = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")
 
 
def clear():
    entry.delete(0, tk.END)
 
 
button_1 = tk.Button(master=frame, text='1', padx=15,
                     pady=5, width=3, command=lambda: myclick(1))
button_1.grid(row=1, column=0, pady=2)
button_2 = tk.Button(master=frame, text='2', padx=15,
                     pady=5, width=3, command=lambda: myclick(2))
button_2.grid(row=1, column=1, pady=2)
button_3 = tk.Button(master=frame, text='3', padx=15,
                     pady=5, width=3, command=lambda: myclick(3))
button_3.grid(row=1, column=2, pady=2)
button_4 = tk.Button(master=frame, text='4', padx=15,
                     pady=5, width=3, command=lambda: myclick(4))
button_4.grid(row=2, column=0, pady=2)
button_5 = tk.Button(master=frame, text='5', padx=15,
                     pady=5, width=3, command=lambda: myclick(5))
button_5.grid(row=2, column=1, pady=2)
button_6 = tk.Button(master=frame, text='6', padx=15,
                     pady=5, width=3, command=lambda: myclick(6))
button_6.grid(row=2, column=2, pady=2)
button_7 = tk.Button(master=frame, text='7', padx=15,
                     pady=5, width=3, command=lambda: myclick(7))
button_7.grid(row=3, column=0, pady=2)
button_8 = tk.Button(master=frame, text='8', padx=15,
                     pady=5, width=3, command=lambda: myclick(8))
button_8.grid(row=3, column=1, pady=2)
button_9 = tk.Button(master=frame, text='9', padx=15,
                     pady=5, width=3, command=lambda: myclick(9))
button_9.grid(row=3, column=2, pady=2)
button_0 = tk.Button(master=frame, text='0', padx=15,
                     pady=5, width=3, command=lambda: myclick(0))
button_0.grid(row=4, column=1, pady=2)
 
button_add = tk.Button(master=frame, text="+", padx=15,
                       pady=5, width=3, command=lambda: myclick('+'))
button_add.grid(row=5, column=0, pady=2)
 
button_subtract = tk.Button(
    master=frame, text="-", padx=15, pady=5, width=3, command=lambda: myclick('-'))
button_subtract.grid(row=5, column=1, pady=2)
 
button_multiply = tk.Button(
    master=frame, text="*", padx=15, pady=5, width=3, command=lambda: myclick('*'))
button_multiply.grid(row=5, column=2, pady=2)
 
button_div = tk.Button(master=frame, text="/", padx=15,
                       pady=5, width=3, command=lambda: myclick('/'))
button_div.grid(row=6, column=0, pady=2)
 
button_clear = tk.Button(master=frame, text="clear",
                         padx=15, pady=5, width=12, command=clear)
button_clear.grid(row=6, column=1, columnspan=2, pady=2)
 
button_equal = tk.Button(master=frame, text="=", padx=15,
                         pady=5, width=9, command=equal)
button_equal.grid(row=7, column=0, columnspan=3, pady=2)
 
window.mainloop()
"""