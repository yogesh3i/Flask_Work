# Here i am understanding the if __name__== "__main__" concept why it is used ?

# See the app can be run using app.run(debug=True) only but we are giving if __name__== "__main__"  before it. 
# Because it acts as safe key for the app it will run only when the main matches the name which only happen within the scopre only. 

print(f"Hello Boys-({__name__})") # here the __name__ acting like main of the mod1.py 
